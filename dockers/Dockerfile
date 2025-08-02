FROM python:3.12-slim

# Install necessary tools and Node.js (for npm-based CLIs)
RUN apt-get update && apt-get install -y \
    curl \
    git \
    nano \
    net-tools \
    gnupg \
    wget \
    procps \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js (v22 LTS) and npm
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get update && \
    apt-get install -y nodejs && \
    npm install -g npm && \
    rm -rf /var/lib/apt/lists/*

# Python dependencies (already in base image, just pip upgrade)
RUN pip install --upgrade pip

# Install task-master-ai and other global CLIs
RUN npm install -g task-master-ai @google/gemini-cli @anthropic-ai/claude-code

# Set working directory
WORKDIR /apps

# GitHub access token as build-time argument
ARG GITHUB_PAT
ENV GITHUB_PAT=${GITHUB_PAT}

# Clone the target repository
RUN git clone https://github.com/yojulab/learn_vibecodings.git learn_vibecodings

WORKDIR /apps/learn_vibecodings

# (Optional) Remove .git directory for a cleaner image
# RUN rm -rf .git
