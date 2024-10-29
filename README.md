# 약국이 | Yaggugi
![Python](https://img.shields.io/badge/Python-v3.10.8-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-v2.1.0-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)

> 약국이는 내 몸에 맞는 영양제를 추천하고, 섭취 일정을 손쉽게 관리하는 맞춤형 건강 앱 입니다.

## 🩺 **Introduction**

```약국이```는 인공지능을 활용하여 사용자 맞춤형 영양제 정보를 제공하고 섭취 일정을 체계적으로 관리할 수 있는 건강 관리 앱입니다.<br />
```Python```과 ```PyTorch``` 기반으로 구축된 AI 모델을 통해 영양제의 성분과 효능을 분석하고,<br />
사용자의 건강 상태와 필요에 맞는 최적의 영양제 조합을 추천합니다.<br />
```React```와 ```Bootstrap```을 사용하여 직관적이고 반응형인 UI를 설계해, 누구나 손쉽게 접근할 수 있는 사용자 경험을 제공합니다.<br />

## 🩺 **Architecture**

![Architecture](https://github.com/user-attachments/assets/3d833756-c761-4cbd-9500-84ad59113859)

## 🩺 **Feature**
+ 영양제 조합 및 추천
  + 추론형모델, 음성인식모델, TTS모델

+ 영양제 사진찍어서 성분검색
  + OCR모델

+ 영양제 섭취 스캐쥴
  + 음성인식모델

## 🩺 **Branch Strategy**

### 버전 관리 규칙
> 프로젝트 버전 관리는 **Github Actions**으로 Pipeline이 구축되어 있습니다.<br />
> 변경 내역을 프로젝트 **package.json**에서 `version`, `releaseNotes` 에 내용을 추가하여<br />
> 적용할수 있습니다.

- "version"
  - `주 버전` . `부 버전` . `수정 버전` EX) 1.0.0
    
  - 주 버전
    - 주 버전은 하위 호환성이 깨지는 큰 변경 사항이 있을 때 업데이트됩니다.
      
  - 부 버전
    - 부 버전은 하위 호환성을 유지하는 새로운 기능이 추가되었을 때 업데이트됩니다.
      
  - 수정 버전
    - 수정 버전은 버그 수정과 같은 사소한 변경 사항이 있을 때 업데이트됩니다.

- "releaseNotes"
  - 릴리즈 변경내역을 기술합니다. 

### 브랜치 네이밍 규칙

- `main` : 안정적인 릴리스 브랜치
- `develop` : 기능들이 병합되는 개발 브랜치
- `feature/{feature-name}` : 새로운 기능을 위한 브랜치
- `fix/{issue-name}` : 버그 수정을 위한 브랜치

### 커밋 메시지 규칙

- **형식**: `[태그]: (변경 사항)`
- **태그 종류**:
  - `feat` : 새로운 기능 추가
  - `fix` : 버그 수정
  - `refactor` : 코드 리팩토링
  - `style` : 코드 스타일 수정 (공백, 세미콜론 등)
  - `docs` : 문서 관련 변경

## 🩺 **Folder Structure**

## 🩺 **Contributor**

- stjoo0925 | 주순태 | [깃허브](https://github.com/Stjoo0925)

- ppudding3861 | 강형석 | [깃허브](https://github.com/ppudding3861)

- shaneee123 | 이세인 | [깃허브](https://github.com/shaneee123)

- Yesssung | 박예성 | [깃허브](https://github.com/Yesssung)

- Bigdata92 | 송지섭 | [깃허브](https://github.com/Bigdata92)

- kimkunook | 김건욱 | [깃허브](https://github.com/kimkunook)

## 🩺 **Stack**
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD300?style=for-the-badge&logo=huggingface&logoColor=black)
![Transformers](https://img.shields.io/badge/Transformers-FFD300?style=for-the-badge&logo=huggingface&logoColor=black)
