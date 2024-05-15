#!/bin/bash

MODEL_PATH="/home/rong/Documents/_Projects/Llama3-retard/llama3.Q4_K_M.gguf"
INPUT="I believe the meaning of life is "
# Run llama.cpp with the specified model path and redirect stderr to a file
./llama.cpp/main \
  -m "$MODEL_PATH" \
  -p "$INPUT" -n 128 \
  2> llama_error.log
