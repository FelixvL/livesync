import geheim
import os
import openai


from openai import OpenAI
client = OpenAI(api_key=geheim.key())
invoer = input("stel een vraag? ")
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[{
      "role": "system",
      "content": '''vertel in spaans over: '''+invoer+''''''
    }],
    temperature=0.8,
    max_completion_tokens=1024
)

print(completion)
# print(completion.choices[0].message.content)