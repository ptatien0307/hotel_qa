#!/bin/bash

# Start Frontend
cd rag_fe
echo "Starting Frontend..."
npm run dev &

# Store the process ID of the frontend
FRONTEND_PID=$!

# Start Backend
cd ../rag_be
echo "Starting Backend..."
source activate base
conda activate rag_app
python main.py &

# Store the process ID of the backend
BACKEND_PID=$!

# Wait for both processes to finish
wait $FRONTEND_PID
wait $BACKEND_PID
