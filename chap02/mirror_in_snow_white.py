from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model='gpt-5-nano',
    messages=[
        {"role": "system", "content":"너는 백설공주 이야기 속의 마법 거울이야. 캐릭터에 부합하게 답변해줘"},
        {"role": "user", "content":"세상에서 누가 제일 아름답니?"},
    ]
)

# print(response)

# print('----')
print(response.choices[0].message.content) 
