from openai import OpenAI
import tiktoken
import logging
from datetime import datetime

log = logging.getLogger("chatbot_token_count")

logging.basicConfig(filename = "chatbot_token_count.log", level = logging.INFO)

client = OpenAI()

def get_api_chat_response_message(model, messages):
    api_response = client.chat.completions.create(
        model = model,
        messages = messages
    )

    response_content = api_response.choices[0].message.content

    return response_content

model = "gpt-3.5-turbo"

encoding = tiktoken.encoding_for_model(model)
token_input_limit = 12289

# print(encoding)

chat_history = []

user_input = ""

total_input_tokens = 0
total_output_tokens = 0

while True:
    if (user_input == ""):
        user_input = input("Chatbot: Hello there, I'm your helpful chatbot! Type exit to end our chat. What's your name? ")
        user_name = f"User name is {user_input}"
        chat_history.append({
          "role": "user",
          "content": user_name
        })
    else:
        user_input = input("You: ")
    if user_input.lower() == "exit":
	log.info({
		'total input tokens': total_input_tokens,
		'total output tokens': total_output_tokens,
		'total tokens': total_input_tokens + total_output_tokens,
		'date': datetime.now()
	})
        exit()
	
    token_input = len(encoding.encode(user_input))
	total_input_tokens += token_input
	# print(token_count)
	if (token_input > token_input_limit):
	        print("Your prompt is too long. Please try again.")
	        continue

    chat_history.append({
        "role": "user",
        "content": user_input
    })

    response = get_api_chat_response_message(model, chat_history)

	token_output = len(encoding.encode(response))
	total_output_tokens += token_output

    print("Chatbot: ", response)

    chat_history.append({
        "role": "assistant",
        "content": response
    })


