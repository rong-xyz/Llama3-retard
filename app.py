import gradio as gr
from util import run_llama_inference


def run_inference(input_text, model):
    # Map UI model selection to file paths
    model_paths = {
        "4位模型（更快）": "llama3.Q4_K_M.gguf",
        "16位模型（更强大）": "llama3.F16.gguf"
    }
    model_path = model_paths.get(model, "llama3.Q4_K_M.gguf")  # Default to "4位模型（更快）"

    # Call the inference function
    response = run_llama_inference(
        input_text=input_text,
        Model=model_path
    )
    return response


with gr.Blocks() as demo:
    demo.title = "Llama3 弱智吧微调版"
    demo.queue(max_size=1)
    with gr.Row():
        with gr.Column():
            input_txt = gr.Textbox(label="输入文本")
            model_select = gr.Dropdown(
                ["4位模型（更快）", "16位模型（更强大）"],
                label="选择模型",
                value="4位模型（更快）"  # Set default value
            )
            input_btn = gr.Button(value="提交")
        with gr.Column():
            output = gr.Textbox(label="回答")
    
    input_btn.click(
        fn=run_inference,
        inputs=[input_txt, model_select],
        outputs=output
    )
    
    examples = gr.Examples(
        examples=[
            ["鸡柳是鸡身上哪个部位啊？"],
            ["爸爸再婚，我是不是就有了个新娘？"],
            ["为什么抄袭永远都是今人抄袭古人，而没有古人抄袭今人的案例？"]
        ],
        inputs=[input_txt]
    )


demo.launch(share=True)
'''
with gr.Blocks() as demo:
    
    with gr.Row():
        with gr.Column():
            input_txt = gr.Textbox(lines=5, label="输入文本")
            input_btn = gr.Button(value="提交")
        with gr.Column():
            output = gr.Textbox(lines=5, label="回答")
    
    input_btn.click(run_llama_inference, inputs=input_txt, outputs=output)
    examples = gr.Examples(examples=["只剩一个心脏了还能活吗？",
                                     "马上要上游泳课了，昨天洗的泳裤还没干，怎么办"],
                           inputs=[input_txt])
    
demo.launch(share=False)
'''