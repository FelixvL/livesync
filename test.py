import os
import openai
import geheim


from openai import OpenAI
client = OpenAI(api_key=geheim.key())

# Laad het bestand in als tekst (bijvoorbeeld JSON of tekst)
with open("films.csv", "r") as file:
    file_content = file.read()

# Stel de vraag met de inhoud van het bestand als context
vraag = input("stel een vraag over het bestand: ")
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Dit is de inhoud van het bestand: " + file_content},
        {"role": "user", "content": vraag}
    ],
    temperature=0.7,
    max_tokens=3200
)

# Print het antwoord van de API
print(response)
print(response.choices[0].message.content)