FROM python:3.12-slim

# 환경 기본 설정
ENV DEBIAN_FRONTEND=noninteractive

# 필수 패키지 설치
RUN apt-get update && apt-get install -y \
    curl \
    git \
    nano \
    net-tools \
    wget \
    gnupg \
    ca-certificates \
    libnss3 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libxss1 \
    libasound2 \
    libxshmfence1 \
    libgbm1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libu2f-udev \
    fonts-liberation \
    libappindicator3-1 \
    libatk1.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Node.js LTS (v18 기준) 설치
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get update && \
    apt-get install -y nodejs && \
    npm install -g npm && \
    rm -rf /var/lib/apt/lists/*

# Python pip 최신화
RUN pip install --upgrade pip

# 글로벌 CLI 설치
RUN npm install -g task-master-ai @google/gemini-cli @anthropic-ai/claude-code

# Playwright 설치 (전체 브라우저 포함: Chromium, Firefox, WebKit)
RUN npm install -D playwright && \
    npx playwright install --with-deps

# 작업 디렉토리 설정
WORKDIR /apps

# GitHub Personal Access Token 전달
ARG GITHUB_PAT
ENV GITHUB_PAT=${GITHUB_PAT}

# GitHub 저장소 클론
RUN git clone https://github.com/yojulab/learn_vibecodings.git learn_vibecodings

# 작업 디렉토리 이동
WORKDIR /apps/learn_vibecodings

# 필요 시 Git 정보 제거
# RUN rm -rf .git
