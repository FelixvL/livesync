import os
import openai
import geheim


from openai import OpenAI
client = OpenAI(api_key=geheim.key())
invoer = input("noem een stad? ")
completion = client.chat.completions.create(
  model="gpt-4",
  messages=[{
      "role": "system",
      "content": '''Ik heet Felix en spreek mij formeel aan. Noem de 5 beroemdste inwoners van : '''+invoer+''', en vertel er in het kort iets over.Ik wil de tekst in het Italiaans'''
    }],
    temperature=0.8,
    max_completion_tokens=600
)

# print(completion)
print(completion.choices[0].message.content)