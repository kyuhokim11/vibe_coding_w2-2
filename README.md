# Vibe Coding Week 2 - Project 2

이 프로젝트는 Vibe Coding Week 2의 두 번째 프로젝트입니다. 백엔드와 프론트엔드로 구성된 챗봇 애플리케이션을 개발하며, GitHub Actions를 활용한 자동화된 CI/CD 파이프라인을 구축합니다.

## 주요 기능
- 백엔드: FastAPI 기반의 AI 챗봇 Agent
- 프론트엔드: Streamlit 기반의 챗봇 UI
- GitHub Actions: 자동 테스트, PR/이슈 관리 자동화

## 설치 및 실행 방법

### 백엔드
```bash
cd backend
pip install -r requirements.txt
python run.py
```

### 프론트엔드
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

## GitHub Actions
이 프로젝트에는 다음 GitHub Actions가 설정되어 있습니다:
- PR 및 Push 시 자동 테스트 실행
- PR 및 이슈에 대한 자동 댓글, 할당, 라벨링, 코드 리뷰 할당 