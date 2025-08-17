import requests
import gradio as gr
import json


url = "http://localhost:11434/api/generate" 

headers = {
    'Content-Type': "application/json"
}


history = []
def gen_response(prompt):

    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model":"CodeJarvis",
        "prompt":final_prompt,
        "stream" : False
    }

    response = requests.post(
        url = url,
        headers=headers,
        data=json.dumps(data)
    )

    if response.status_code==200:
        response = response.text
        data = json.loads(response)
        actual_response = data['response']
        return actual_response
    else:
        print("error:", response.text)


interface = gr.Interface(
    title="CodeJarvis: Simple Code Assistant using Codellama",
    fn = gen_response,
    inputs = gr.Textbox(lines = 1, placeholder = "Enter your prompt"),
    outputs = "text"
)

interface.launch()