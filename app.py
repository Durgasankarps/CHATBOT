import openai
import gradio

openai.api_key = "" #the api key is attached with the form

messages = [{"role": "system", "content": "Personal Assitant"}]  #type of assistant

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", #openai gpt version used 3.5-turbo
        messages=messages
    )
    assistant_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": assistant_reply})  #messages and replies 
    return assistant_reply

flagging_directory = r"c:\Users\durga\Desktop\task\gradio"  #logs stored in local, when flagged

demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Mr. Monkey the Assistant", flagging_dir=flagging_directory) #tile input and outputs

demo.launch(share=True)  #making it sharable produces a second URL which is valid for 72 hours
