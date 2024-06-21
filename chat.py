import openai
import config

openai.api_key = config.OPENAI_API_KEY

#OPENAI_API_KEY = "sk-proj-vOChPP4UlaXwinZpsYgoT3BlbkFJ5wnF8lEr0UI1iWznOHys"

def chatbot(input):
    if input:
        
        messages = [
            {"role": "system","content":"You are an AI specialized in Data Analysis. Do not answer anything other than Data Analysis related queries"},
            {"role":"user", "content":input}
            ]
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
            )
        reply = chat.choices[0].messages.content
        
        return reply
        
