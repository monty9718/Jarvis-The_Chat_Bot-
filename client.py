from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)