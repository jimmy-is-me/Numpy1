import openai

openai.api_key = "您的 OpenAI API 金鑰"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "您是一位有幫助的助手。"},
        {"role": "user", "content": "您好！"}
    ]
)

print(response.choices[0].message['content'])
