import time
import gradio
import datetime
# importing google generative AI model into the code.
import google.generativeai as genai
# For pulling date and time of the user interaction.
current_date = datetime.date.today()
current_time = datetime.datetime.now().time()
#google gemini api_key to access the gemini model.
genai.configure(api_key="AIzaSyDs4Vsj-UeCkzgzGESotCULGOIB3aDjeZQ")
model = genai.GenerativeModel("gemini-1.5-flash")
messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}]
def slow_echo(message, history):
    # reading message for the temp.
    inn=message
    # text sends to the gemini model.
    response = model.generate_content(inn)
    # from respose only text data will be pulled.
    nnew=response.text
    # to save users input and response to a local server to pull history.
    with open('history.txt', 'a') as file:
        user_input = inn
        bot_res = nnew
        file.write(str(current_date)+"  "+str(current_time)+'\n'+'user input : '+user_input + '\n' +'gemini : '+ str(bot_res) + '\n')
    # helps in knowing input and output at command line.
    print(inn)
    print(nnew)
    messages.append({"role": "assistant", "content": nnew})
    # for text like feel(animation), also act as a loading screen
    for i in range(len(nnew)):
        time.sleep(0.01)
        yield  nnew[: i + 1]
    #yield nnew
# for chat interface.
demo = gradio.ChatInterface(slow_echo, type="messages")

if __name__ == "__main__":
    demo.launch(share=True)
