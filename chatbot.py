from openai import OpenAI

client = OpenAI()

def get_response(model, messages):
    response = client.chat.completions.create(
        model = model,
        messages = messages
    )
    return response.choices[0].message.content

user_input = input("\nAsk something...\n\n")

model = "gpt-3.5-turbo"

messages = [
    {"role": "system", "content": "You are an assistant that always answers in the form of a poem."},
    {"role": "user", "content": user_input}
]

response_for_user = get_response(model, messages)

print("\n" + response_for_user + "\n")

