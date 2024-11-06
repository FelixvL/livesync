import os
import openai
import geheim


from openai import OpenAI
client = OpenAI(api_key=geheim.key())
invoer = input("Stel hier uw vraag? ")
response = client.chat.completions.create(
  model="gpt-4",
  messages=[{
      "role": "system",
      "content": ""+invoer
    }],
    temperature=0.5,
    max_tokens=2024,
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end="", flush=True)