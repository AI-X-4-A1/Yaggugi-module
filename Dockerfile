# syntax=docker/dockerfile:1.4

# 빌드 단계: 모델 다운로드
FROM python:3.12-slim AS builder

WORKDIR /app

# 시스템 패키지 업데이트 및 필요한 라이브러리 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 필요 패키지 설치
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Hugging Face 캐시 디렉토리 생성
RUN mkdir -p /app/cache
ENV HF_HOME=/app/cache

RUN --mount=type=secret,id=HUGGINGFACE_API_TOKEN \
    python -c "import os; \
    from transformers import AutoModelForCausalLM, AutoTokenizer; \
    model_name = 'LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct'; \
    f = open('/run/secrets/HUGGINGFACE_API_TOKEN', 'r'); \
    token = f.read().strip(); \
    f.close(); \
    AutoModelForCausalLM.from_pretrained(model_name, cache_dir='/app/cache', token=token, trust_remote_code=True); \
    AutoTokenizer.from_pretrained(model_name, cache_dir='/app/cache', token=token, trust_remote_code=True)"

# 최종 이미지: 필요한 파일만 복사
FROM python:3.12-slim

WORKDIR /app

# 시스템 패키지 업데이트 및 필요한 라이브러리 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 필요 패키지 설치
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Hugging Face 캐시 디렉토리 생성
RUN mkdir -p /app/cache
ENV HF_HOME=/app/cache

# 빌드 단계에서 다운로드한 모델 복사
COPY --from=builder /app/cache /app/cache

# 앱 소스 코드 복사
COPY main.py .

# Uvicorn 서버 시작
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Docker 실행 과정

# set HUGGINGFACE_API_TOKEN=your_huggingface_api_token_here

# (echo|set /p="%HUGGINGFACE_API_TOKEN%")>huggingface_token.txt

# set DOCKER_BUILDKIT=1

# docker build --secret id=HUGGINGFACE_API_TOKEN,src=./huggingface_token.txt -t yaggugi-module-llm .

# del huggingface_token.txt

# docker run --env-file .env --gpus all -d -p 8000:8000 --name yaggugi-module-llm yaggugi-module-llm
