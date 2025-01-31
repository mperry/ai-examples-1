
import requests
import json
import gradio as gr
import time

url = "http://localhost:11434/api/generate"
headers = {
    'Content-Type': 'application/json',
}
response_history = []
prompt_history = []
tiny_model = "tinyllama"
llama3_model = "llama3.2"
llama2_model = "llama2"
deepseek_model = "deepseek-r1:8b"
deepseek_coder_model = "deepseek-coder-v2"
default_model = tiny_model
supported_models = [tiny_model, llama3_model, deepseek_model, deepseek_coder_model]
print(f"The default model is {default_model}")
time_decimal_places = 1
log_response = True
stream_response = False

def generate_response(model, question, progress=gr.Progress()):
    prompt_history.append([question, model])
    p = format_prompt(question, model)
    print(f"The model is: {model}\n")
    print(f"The question is:\n{p}")
    data = {
        "model": model,
        "stream": stream_response,
        "prompt": p,
    }

    start_time = time.perf_counter()
    response = requests.post(url, headers=headers, data=json.dumps(data))
    end_time = time.perf_counter()
    elapsed_time = round(end_time - start_time, time_decimal_places)
    print(f"Elapsed time {elapsed_time}s")

    if response.status_code == 200:
        response_text = response.text
        if log_response:
            print(f"The response is:\n{response_text}")

        data = json.loads(response_text)
        actual_response = data["response"]
        response_history.append([actual_response, elapsed_time])
        return actual_response, model, elapsed_time, prompt_history, response_history
    else:
        print("Error:", response.status_code, response.text)
        return None

def run_ui():
    iface = gr.Interface(
        fn=generate_response,
        inputs=[
            gr.Dropdown(supported_models, label="Model", value=default_model),
            gr.Textbox(lines=4, placeholder="Enter your prompt here...", label="Prompt")
        ],
        outputs=[
            gr.Textbox(label="Response"), gr.Textbox(label="Model"), gr.Number(label="Runtime (s)"),
            gr.Textbox(label="Prompts", lines=10, interactive=False),
            gr.Textbox(label="Responses", lines=10, interactive=False)
        ]
    )
    iface.launch(debug=True)

def format_prompt(question, model):
    if (model == tiny_model):
        return tiny_prompt(question)
    elif (model == llama3_model):
        return llama3(question)
    else:
        return question

def tiny_prompt(question):
    # https://ollama.com/library/tinyllama:latest/blobs/af0ddbdaaa26
    # https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0
    p2 = f"""
<|system|>
You are a friendly chatbot.
<|user|>
{question}
<|assistant|>
"""
    return p2

def llama3(question):
    # https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_1/#prompt-template
    # https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/text_prompt_format.md
    return f"""
<|begin_of_text|>
<|start_header_id|>user<|end_header_id|>
{question}
<|end_of_text|>
"""

run_ui()