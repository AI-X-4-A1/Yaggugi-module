# conda create -n LLM python=3.12
# conda activate LLM
# conda install pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia
# pip install transformers
# pip install fastapi uvicorn
# pip install "accelerate>=0.26.0"
# pip install python-multipart

# step 1 : import moduleb
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# step 2 : create inference object(instance)
app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_id = 'Bllossom/llama-3.2-Korean-Bllossom-3B'
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)


# step 3 : prepare data
def generate_response(instruction: str) -> str:
    prompt = f"질문: {instruction}\n답변:"

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    eos_token_id = tokenizer.eos_token_id

    # step 4 : instance
    outputs = model.generate(
        inputs["input_ids"],
        max_new_tokens=50,
        eos_token_id=eos_token_id,
        do_sample=True,
        temperature=0.6,
        top_p=0.9,
        pad_token_id=eos_token_id
    )

    # step 5 : Post-process the output to obtain the final answer
    result = tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
    return result.strip()


# FastAPI 엔드포인트 생성
@app.post("/chat")
async def generate(text: str = Form(...)):
    response = generate_response(text)
    return {"result": response}
