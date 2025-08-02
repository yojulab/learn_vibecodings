#!/bin/bash

# 스크립트가 있는 디렉토리에서 실행되도록 보장합니다.
cd "$(dirname "$0")"

# 함수 정의
stop_servers() {
    echo "Stopping existing servers..."
    # 백엔드 서버 (uvicorn) 종료
    pkill -f "uvicorn main:app"
    echo "Backend server (uvicorn) stop signal sent."

    # 프론트엔드 서버 (vite) 종료
    # 'npm run dev'는 vite를 실행합니다.
    pkill -f "vite"
    echo "Frontend server (vite) stop signal sent."
    sleep 2
}

test_servers() {
    echo "Testing backend server..."
    curl -s http://localhost:8000/ && echo "Backend root endpoint OK."
    curl -s http://localhost:8000/health && echo "Backend health endpoint OK."

    echo "Testing frontend server..."
    if pgrep -f "vite" > /dev/null
    then
        echo "Frontend server (vite) is running."
    else
        echo "Frontend server (vite) is NOT running."
    fi
}

start_servers() {
    echo "Starting servers in background..."

    # 백엔드 서버 시작
    echo "Starting backend server..."
    cd backend
    nohup python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 > ../backend.log 2>&1 &
    echo "Backend server started. PID: $!. Log: backend.log"
    cd ../

    # 프론트엔드 서버 시작
    echo "Starting frontend server..."
    cd vibecodings-vue-frontend
    nohup npm run dev -- --host &> ../frontend.log &
    echo "Frontend server started. PID: $!. Log: frontend.log"

    cd /apps/learn_vibecodings
}

# 메인 로직
ACTION=${1:-restart} # 인자가 없으면 'restart'를 기본값으로 사용

case "$ACTION" in
    start)
        start_servers
        ;;
    stop)
        stop_servers
        echo "Servers stopped."
        ;;
    restart)
        stop_servers
        start_servers
        ;;
    test)
        test_servers
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|test}"
        exit 1
        ;;
esac

echo "Script finished."
