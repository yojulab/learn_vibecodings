# 프로젝트 Gemini 가이드

이 문서는 `learn_vibecodings` 프로젝트의 원활한 개발을 돕기 위한 기술 가이드입니다. 프로젝트의 구조, 기술 스택, 주요 실행 명령어 등을 포함하고 있습니다.

## 1. 프로젝트 개요

이 프로젝트는 **React/Vite** 기반의 프론트엔드와 **Python/FastAPI** 기반의 백엔드로 구성된 풀스택 웹 애플리케이션입니다. 또한, `.taskmaster` 디렉토리를 통해 **Task Master AI**를 활용한 프로젝트 관리 및 자동화가 설정되어 있습니다.

## 2. 기술 스택

### 프론트엔드 (`frontend/`)

-   **Framework**: [React](https://react.dev/) (^19.1.0)
-   **Build Tool**: [Vite](https://vitejs.dev/) (^7.0.4)
-   **Styling**: [Tailwind CSS](https://tailwindcss.com/) (^4.1.11)
-   **Linting**: [ESLint](https://eslint.org/) (^9.32.0)
-   **Package Manager**: npm

### 백엔드 (`backend/`)

-   **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
-   **Server**: [Uvicorn](https://www.uvicorn.org/)
-   **Language**: Python 3.12
-   **Environment**: venv

## 3. 프로젝트 구조

```
/
├── backend/            # FastAPI 백엔드 소스 코드
│   ├── app/            # FastAPI 애플리케이션
│   │   ├── main.py     # FastAPI 앱 진입점
│   │   ├── models/     # 데이터 모델
│   │   └── routes/     # API 라우트
│   └── venv/           # Python 가상 환경
├── frontend/           # React 프론트엔드 소스 코드
│   ├── src/            # React 소스 코드
│   │   └── main.jsx    # React 앱 진입점
│   ├── package.json    # Node.js 의존성 및 스크립트
│   └── vite.config.js  # Vite 설정
├── .taskmaster/        # Task Master AI 설정 및 데이터
└── restart-server.sh   # 서버 재시작 스크립트
```

## 4. 시작하기

### 백엔드 설정 및 실행

1.  **가상 환경 활성화**:
    ```bash
    source backend/venv/bin/activate
    ```

2.  **의존성 설치** (필요시):
    `requirements.txt` 파일이 없으므로, 필요시 현재 가상환경에 설치된 패키지를 기반으로 생성할 수 있습니다.
    ```bash
    pip freeze > backend/requirements.txt
    ```
    이후 다른 환경에서는 아래 명령어로 설치합니다.
    ```bash
    pip install -r backend/requirements.txt
    ```

3.  **백엔드 서버 실행**:
    루트 디렉토리에서 `restart-server.sh` 스크립트를 사용하거나 직접 Uvicorn을 실행합니다.
    ```bash
    # 스크립트 사용 (추천)
    ./restart-server.sh start

    # 직접 실행
    uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
    ```
    -   API는 `http://localhost:8000` 에서 실행됩니다.

### 프론트엔드 설정 및 실행

1.  **디렉토리 이동**:
    ```bash
    cd frontend
    ```

2.  **의존성 설치**:
    ```bash
    npm install
    ```

3.  **프론트엔드 개발 서버 실행**:
    ```bash
    npm run dev
    ```
    -   애플리케이션은 `http://localhost:5173` (또는 Vite가 지정하는 다른 포트)에서 실행됩니다.

## 5. 주요 명령어

### 전체 서버 관리 (`restart-server.sh`)

-   **서버 시작/재시작**: `./restart-server.sh` 또는 `./restart-server.sh restart`
-   **서버 중지**: `./restart-server.sh stop`
-   **서버 상태 테스트**: `./restart-server.sh test`

### 프론트엔드 (`frontend/` 디렉토리에서 실행)

-   **개발 서버 시작**: `npm run dev`
-   **프로덕션 빌드**: `npm run build`
-   **코드 린팅**: `npm run lint`

### Task Master AI

-   **전체 태스크 목록 보기**: `task-master list`
-   **다음 작업 추천 받기**: `task-master next`
-   **특정 태스크 상세 보기**: `task-master show <id>`