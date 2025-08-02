#!/bin/bash

# Ensure the script is run from its directory
cd "$(dirname "$0")"

# Function definitions
stop_servers() {
    echo "Stopping existing servers..."
    # Kill backend server (uvicorn)
    pkill -f "uvicorn app.main:app" && echo "Backend server stopped." || echo "No backend server process found."
    # Kill frontend server (vite)
    pkill -f "npm run dev" && echo "Frontend server stopped." || echo "No frontend server process found."
}

test_servers() {
    echo "Testing backend server..."
    curl -s http://localhost:8000/ && echo "Backend root endpoint OK."
    curl -s http://localhost:8000/health && echo "Backend health endpoint OK."
    curl -s http://localhost:8000/posts/ && echo "Backend posts endpoint OK."


    echo "Testing frontend server..."
    # We will rely on the logs to check if the frontend server is running.
    if grep -q "ready in" frontend.log; then
        echo "Frontend server (vite) is running."
    else
        echo "Frontend server (vite) is NOT running."
    fi
}

start_servers() {
    echo "Starting servers in background..."

    # Start backend server
    echo "Starting backend server..."
    cd backend
    nohup python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 > ../backend.log 2>&1 &
    echo "Backend server started. PID: $!. Log: backend.log"
    cd ../

    # Start frontend server
    echo "Starting frontend server..."
    cd frontend
    nohup npm run dev -- --host &> ../frontend.log &
    echo "Frontend server started. PID: $!. Log: frontend.log"

    cd /apps/learn_vibecodings
}

# Main logic
ACTION=${1:-restart} # Default to 'restart' if no argument is given

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