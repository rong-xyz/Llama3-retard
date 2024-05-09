import subprocess
import os
alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}
### Input:
{}
### Response:
{}"""


def run_llama_inference(input_text, instruction="请用中文回答", Model="model-unsloth.F16.gguf"):

    print(os.getcwd())

    # Define the paths and inputs
    MODEL_PATH = Model
    INPUT = alpaca_prompt.format(
        instruction,
        input_text,
        "",
    )
    
    # Construct the command to run the bash script
    command = [
        "./llama.cpp/main",
        "-m", MODEL_PATH,
        "-p", INPUT,
        "-n", "256"
    ]
    
    # Execute the command and capture its output
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            response = stdout.decode()
            response_start = response.find("### Response:") + len("### Response:")
            response_end = response.find("<|endoftext|>", response_start) - len(" <|endoftext|> ")
            return response[response_start:response_end].strip()  # Strip leading/trailing whitespaces
        else:
            return stderr.decode()
    except Exception as e:
        return "Error occurred: " + str(e)