#!/bin/bash

echo "Installing backend dependencies..."
cd /apps/learn_vibecodings/backend
npm install

echo "Installing frontend dependencies..."
cd /apps/learn_vibecodings/frontend
npm install

cd ../
echo "All dependencies installed."
