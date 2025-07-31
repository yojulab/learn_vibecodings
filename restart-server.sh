#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "--- Stopping any running servers... ---"
# Use pkill to stop processes matching a pattern. The '|| true' prevents the script from exiting if no process is found.
pkill -f "node dist/main.js" || true
pkill -f "vite" || true
echo "All running server processes stopped."
echo "-----------------------------------"
sleep 2 # Give ports time to be released

echo "--- Starting backend server... ---"
cd backend
npm run start &
cd ..
echo "Backend server started in the background."
echo "-----------------------------------"

echo "--- Starting frontend server... ---"
cd frontend
# --host makes it accessible over the network
npm run dev -- --host &
cd ..
echo "Frontend server started in the background."
echo "-----------------------------------"

echo "Servers have been restarted."
echo "Wait a few moments for them to initialize."
echo "You can check their status with: ps -ef | grep -E 'node|vite'"
