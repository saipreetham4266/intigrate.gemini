import time
import gradio
import google.generativeai as genai
genai.configure(api_key="AIzaSyDs4Vsj-UeCkzgzGESotCULGOIB3aDjeZQ")
model = genai.GenerativeModel("gemini-1.5-flash")
messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}]
def slow_echo(message, history):
    inn=message
    response = model.generate_content(inn)
    nnew=response.text
    with open('history.txt', 'a') as file:
        user_input = inn
        bot_res = response
        file.write(user_input + '\n' + str(bot_res) + '\n')
    print(inn)
    print(nnew)
    messages.append({"role": "assistant", "content": nnew})
    for i in range(len(nnew)):
        time.sleep(0.01)
        yield  nnew[: i + 1]
    #yield nnew   
demo = gradio.ChatInterface(slow_echo, type="messages")

if __name__ == "__main__":
    demo.launch(share=True)
