import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# FastAPI 앱 생성 및 CORS 설정
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 서비스 시에는 허용할 도메인을 명시하는 것이 안전합니다.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Hugging Face API 토큰 설정 및 모델, 토크나이저 로드
api_token = os.getenv("HUGGINGFACE_API_TOKEN")
if not api_token:
    raise ValueError("HUGGINGFACE_API_TOKEN 환경 변수가 설정되지 않았습니다.")

try:
    model = AutoModelForCausalLM.from_pretrained(
        "LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct",
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        device_map="auto",
        token=api_token
    )
    tokenizer = AutoTokenizer.from_pretrained(
        "LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct",
        token=api_token 
    )
except Exception as e:
    raise RuntimeError(f"모델을 로드하는 중 오류가 발생했습니다: {e}")

# 요청 데이터 모델 정의
class PromptRequest(BaseModel):
    prompt: str

def extract_assistant_response(response: str) -> str:
    assistant_marker = "[|assistant|]"
    start_index = response.find(assistant_marker)
    
    if start_index != -1:
        start_index += len(assistant_marker)
        assistant_response = response[start_index:].strip()
        return assistant_response
    else:
        # 마커를 찾지 못한 경우 전체 응답을 반환하거나 빈 문자열을 반환할 수 있습니다.
        return response.strip()

@app.post("/generate")
async def generate_text(request: PromptRequest):
    prompt = request.prompt
    
    # 메시지 구성
    messages = [
        {"role": "system", "content": "당신은 약국이 이며, 영양제 전문가로서 사용자에게 도움이 되는 조언을 한국어로 제공하는 역할을 합니다. 영양제에 대한 질문에만 답변하며, 간결하고 직관적인 대답을 합니다."},
        {"role": "user", "content": prompt}
    ]
    
    # 입력 텍스트 생성
    try:
        input_text = ""
        for message in messages:
            role = message["role"]
            content = message["content"]
            if role == "system":
                input_text += f"[|system|]{content}\n"
            elif role == "user":
                input_text += f"[|user|]{content}\n"
            elif role == "assistant":
                input_text += f"[|assistant|]{content}\n"
        input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"토크나이징 오류: {e}")

    # 모델 추론 수행
    try:
        output = model.generate(
            input_ids.to(model.device),
            eos_token_id=tokenizer.eos_token_id,
            max_new_tokens=128
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    # 결과 디코딩
    response_text = tokenizer.decode(output[0], skip_special_tokens=True)
    
    # 후처리: '[|assistant|]' 이후의 텍스트만 추출
    assistant_response = extract_assistant_response(response_text)
    
    return {"response": assistant_response}