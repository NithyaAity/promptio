import gradio as gr

def greet(name, intensity):
    return "Howdy!!!!, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()
