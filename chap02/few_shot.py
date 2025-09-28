from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPEN_API_KEY')

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model='gpt-5-nano',
    messages=[
        {"role": "system", "content":"너는 유치원생이야."},

        {"role": "user", "content":"참새"},
        {"role": "assistant", "content":"짹짹"},

        {"role": "user", "content":"말"},
        {"role": "assistant", "content":"히이잉"},

        {"role": "user", "content":"개구리"},
        {"role": "assistant", "content":"개굴개굴"},
        
        {"role": "user", "content":"뱀"},
    ]
)

# print(response)

# print('----')
print(response.choices[0].message.content) 
