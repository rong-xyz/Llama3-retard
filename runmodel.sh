#!/bin/bash

MODEL_PATH="/home/rong/Documents/_Projects/Llama3-retard/model-unsloth.F16.gguf"
INPUT="I believe the meaning of life is "
# Run llama.cpp with the specified model path and redirect stderr to a file
./llama.cpp/main \
  -m "$MODEL_PATH" \
  -p "$INPUT" -n 128 \
  2> llama_error.log
