from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()

client = genai.Client()

system_instruction = "너는 유치원 학생이야. 유치원생처럼 답변해줘. 특수문자, 이모지 사용금지!"
prompt = """
선생님: 참새
유치원생: 짹짹
선생님: 말
유치원생: 히이잉
선생님 개구리
유치원생: 개굴개굴
선생님: 오리
유치원생: 
"""

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=prompt,
    config=types.GenerateContentConfig(
      system_instruction=system_instruction
    ),
)

print(response.text)