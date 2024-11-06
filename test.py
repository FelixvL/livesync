import os
import openai
import geheim


from openai import OpenAI
client = OpenAI(api_key=geheim.key())

invoer = input("kies een onderwerp? ")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[{
      "role": "system",
      "content": '''JE BENT ONDERDEEL VAN EEN SYSTEEM: maak een website met informatie over: 
        '''+invoer+''' 
        IK WIL UITSLUITEND HTML. GEEN INTRO. GEEN UITRO. maak het mooi met css in vrolijke kleuren.'''
    #   "content": ''''''+invoer+''''''
    }],
    temperature=0.8,
    max_completion_tokens=1024
)

print(completion)
# print(completion.choices[0].message.content)

tekst = completion.choices[0].message.content
bestandsnaam = "voorbeeld.html"
with open(bestandsnaam, "w") as bestand:
    bestand.write(tekst)