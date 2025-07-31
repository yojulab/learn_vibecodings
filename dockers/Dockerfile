FROM mcr.microsoft.com/playwright:v1.54.0-noble

# Install necessary tools
RUN apt-get update && apt-get install -y \
    git net-tools \
    curl \
    nano \
    python3 python3-pip python3-pymongo \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python

# Install task-master-ai globally
RUN npm install -g task-master-ai
# Install any CLI
RUN npm install -g @google/gemini-cli
RUN npm install -g @anthropic-ai/claude-code
RUN npx playwright install chromium

# Set working directory
WORKDIR /apps

# Arguments private repository for GitHub credentials
ARG GITHUB_PAT
ENV GITHUB_PAT=${GITHUB_PAT}

# Clone the public repository using PAT
RUN git clone https://github.com/yojulab/learn_vibecodings.git learn_vibecodings

WORKDIR /apps/learn_vibecodings
