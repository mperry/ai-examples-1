
import requests
import json
import gradio as gr
import time

url = "http://localhost:11434/api/generate"
headers = {
    'Content-Type': 'application/json',
}
conversation_history = []
prompt_history = []
tiny_model = "tinyllama"
llama3_model = "llama3.2"
llama2_model = "llama2"
default_model = tiny_model
supported_models = [tiny_model, llama3_model]
print(f"The default model is {default_model}")
time_decimal_places = 1
log_response = True
stream_response = False

def generate_response(model, question, progress=gr.Progress()):
    conversation_history.append(question)
    full_prompt = "\n".join(conversation_history)
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
        conversation_history.append(actual_response)
        prompt_history.append(question)
        history_text = "\n".join(prompt_history)
        return actual_response, model, elapsed_time, history_text
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
            gr.Textbox(label="History", lines=10, interactive=False)
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
    p1 = f"""
<|system|>
You are a friendly chatbot.</s>
<|user|>
{question}</s>
<|assistant|>
"""
    p2 = f"""
<|system|>
You are a friendly chatbot.
<|user|>
{question}
<|assistant|>
"""
    return p2

def llama3(question):
    return f"""
<|begin_of_text|><|start_header_id|>user<|end_header_id|>
{question}
<|eot_id|><|start_header_id|>assistant<|end_header_id|>
"""

run_ui()