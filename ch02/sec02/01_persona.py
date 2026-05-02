from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()

client = genai.Client()

system_instruction = "너는 백설공주 이야기 속의 거울이야. 그 이야기 속의 마법 거울의 캐릭터에 부합하게 답변해줘."

prompt = "세상에서 누가 제일 아름답니?"

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=prompt,
    config=types.GenerateContentConfig(
      system_instruction=system_instruction
    ),
)

print(response.text)