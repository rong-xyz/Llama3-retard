# Llama3-retard

This project focuses on fine-tuning the Llama3-8b model using the Unsloth framework with data from a specific online community(弱智吧). 

The goal is to adapt the Llama3-8b model to understand and generate content that is closely aligned with the unique linguistic characteristics of the chosen dataset. This README provides an overview of the project setup, including how to run the model and visualize results using Gradio.

## Project Overview

The Llama3-8b model is part of the Llama series known for its effectiveness in natural language understanding and generation. In this project, we employ the Unsloth framework for efficient fine-tuning and optimization of the model on specific textual data. Gradio is used to provide an interactive interface to visualize the model outputs.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

We are going to use unsloth as the fine-tuning framework, which currently only supports `Linux`, for `Windows` users, you can use `WSL`, for `Mac` users I have no clue.


## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rong-xyz/Llama3-retard.git
    ```

## Python env setup using Conda

```bash
conda create --name unsloth_env python=3.10
conda activate unsloth_env

conda install pytorch-cuda=<12.1/11.8> pytorch cudatoolkit xformers -c pytorch -c nvidia -c xformers

pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"

pip install --no-deps trl peft accelerate bitsandbytes
```
**If you prefer other methods check  [Official Unsloth Repo](https://github.com/unslothai/unsloth)**

## Training specs
```bash
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.171.04             Driver Version: 535.171.04   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce RTX 4080 ...    Off | 00000000:01:00.0  On |                  N/A |
| N/A   70C    P0             146W / 150W |   6717MiB / 12282MiB |    100%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    0   N/A  N/A      1351      G   /usr/lib/xorg/Xorg                           69MiB |
|    0   N/A  N/A     87122      C   .../rong/miniconda3/envs/us/bin/python     6638MiB |
+---------------------------------------------------------------------------------------+
```