from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPEN_API_KEY')

def summarize_txt(file_path: str):
    client = OpenAI(api_key=api_key)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        txt = f.read()
        
    system_prompt = f'''
    너는 다음 글을 요약하는 봇이다. 아래 글을읽고, 저자의 문제 인식과 주장을 파악하고, 주요내용을 요약하라.
    
    작성해야하는 포맷은 다음과 같다.
    
    # 제목
    
    ## 저자의 문제 인식 및 주장 (15문장 이내)
    
    ## 저자 소개
    
    =================== 이하 텍스트 ===================
    {txt}
    '''
    
    print(system_prompt)
    print('--------------------------------')
    
    
    response = client.chat.completions.create(
        model='gpt-5-nano',
        messages=[
            {"role": "system", "content": system_prompt},
        ]
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    file_path = "chap04/output/과정기반 작물모형을 이용한 웹 기반 밀 재배관리 의사결정 지원시스템 설계 및 구축_with_preprocessing.txt"
    summary = summarize_txt(file_path)
    print(summary)
    
    with open(f"chap04/output/summary_{file_path.split('/')[-1].split('.')[0]}.txt", 'w', encoding='utf-8') as f:
        f.write(summary)
        
    print(f"Summary saved to {f.name}")