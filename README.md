# 약국이 | Yaggugi - LLM

![Python](https://img.shields.io/badge/Python-v3.12.7-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-v2.5.1-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-v0.115.4-009688?style=for-the-badge&logo=fastapi&logoColor=white)

> 약국이는 내 몸에 맞는 영양제를 추천하고, 섭취 일정을 손쉽게 관리하는 맞춤형 건강 앱 입니다.

## 🩺 **Introduction**

- LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct 모델을 활용한 영양제 추천 서비스 제공

```bash

<!-- 실행방법 -->
git clone https://github.com/AI-X-4-A1/Yaggugi-module-LLM.git

cd Yaggugi-module-LLM

docker build -t yaggugi-module-llm .

docker run --env-file .env -d -p 8010:8000 --name yaggugi-module-llm yaggugi-module-llm

<!-- 테스트방법 -->

curl -X POST "http://127.0.0.1:8010/chat" -H "Content-Type: application/x-www-form-urlencoded" -d "text=성인 남성에게 좋은 영양제는 뭐가 있니"

```

## 🩺 **Feature**

- 영양제 조합 및 추천
  - 추론형모델(LLM)

## 🩺 **Folder Structure**

```bash
my_fastapi_app/
├── main.py               # FastAPI 애플리케이션 코드
├── requirements.txt      # 필요한 패키지 목록
└── Dockerfile            # Docker 설정 파일
```

## 🩺 **Contributor**

- stjoo0925 | 주순태 | [깃허브](https://github.com/Stjoo0925)

## 🩺 **Stack**

![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD300?style=for-the-badge&logo=huggingface&logoColor=black)
![Transformers](https://img.shields.io/badge/Transformers-FFD300?style=for-the-badge&logo=huggingface&logoColor=black)
