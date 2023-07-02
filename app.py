
import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "Personal Assitant"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    assistant_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": assistant_reply})
    return assistant_reply

flagging_directory = r"c:\Users\durga\Desktop\task\gradio"

demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Mr. Monkey the Assistant", flagging_dir=flagging_directory)

demo.launch(share=True)
