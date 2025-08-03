
---

### 브랜치별 목적 및 기술 스펙

| 브랜치명                | 주 목적                                                         | 주요 기술/스펙                                      |
|------------------------|----------------------------------------------------------------|-----------------------------------------------------|
| main                   | 전체 프로젝트 통합, 기본 환경 및 문서 관리                      | Docker, Python, Node.js, MongoDB, MCP, AI CLI       |
| gemini_clis_main       | Gemini API 및 Taskmaster 연동, AI CLI 실습 환경                 | Node.js, @google/gemini-cli, task-master-ai, Python |
| gemini_clis_taskmaster | Taskmaster 기반 AI 작업 관리 및 프론트엔드 예제                | React, Vite, Taskmaster, MongoDB, Python            |
| gemini_clis_blog       | 블로그 예제, TDD 기반 포스트 관리, 프론트엔드(Vue) 실습         | Vue 3, Vite, Playwright, MongoDB, Python            |
| copilot_main           | VS Code Copilot 및 확장 설정, 개발 환경 자동화                  | VS Code, Copilot, Node.js, Python                   |

- 각 브랜치는 실습 목적에 따라 AI CLI, MCP 서버, 프론트엔드(React/Vue), 자동화 등 다양한 기술을 포함합니다.
# learn_vibecodings
- docker 설치 확인
```bash
~$ python ./codes/mongo_test.py
```

## 프로젝트 목적

이 프로젝트는 다양한 AI CLI, MCP 서버, 그리고 Vibe Coding IDE 환경을 설치하고, 사용법을 정리하며, 실제 프로젝트 구현 예시를 제공하는 것을 목표로 합니다.

## 주요 목표
- AI 관련 커맨드라인 툴(CLI) 설치 및 활용법 정리
- Model Context Protocol(MCP) 서버 구축 및 실습
- Vibe Coding IDE 환경 설정 및 사용법 안내
- 실습 중심의 프로젝트 예제 구현

