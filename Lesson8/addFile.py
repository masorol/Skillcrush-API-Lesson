from openai import OpenAI
import time
import logging
import datetime
import random

log = logging.getLogger("assistant")

logging.basicConfig(filename = "assitant.log", level = logging.INFO)

client = OpenAI()

curriculum_knowledge = client.files.create(
    file = open("Lesson8/knowledge/OpenAIChatCompletionsAPICheatsheet.pdf", "rb"),
    purpose = "assistants"
)

print(curriculum_knowledge)

# def process_run(thread_id, assistant_id):
#     #create a run
#     run = client.beta.threads.runs.create(
#         thread_id = thread.id,
#         assistant_id = assistant.id
#     )

#     phrases = ["Thinking", "Pondering", "Dotting the i's", "Achieving world peace"]

#     #extract the most recent message content when the run is completed
#     while True:
#         time.sleep(1)
#         print(random.choice(phrases) + "...")
#         run_check = client.beta.threads.runs.retrieve(
#             thread_id = thread.id,
#             run_id = run.id
#         )
#         if run_check.status in ["cancelled", "failed", "completed", "expired"]:
#             return run_check


# def log_run(run_status):
#     if run_status in ["cancelled", "failed", "completed", "expired"]:
#         log.error(str(datetime.datetime.now()) + " Run " + run_status + "\n")

# def get_message(run_status):
#     if run_status == "completed":
#         thread_messages = client.beta.threads.messages.list(
#             thread_id = thread.id
#         )
#         message = thread_messages.data[0].content[0].text.value
    
#     if run_status in ["cancelled", "failed", "expired"]:
#         print("\nAssistant: An error has occurred, please try again.\n")
    
#     return message

# #create the assistant
# assistant = client.beta.assistants.create(
#     name = "Study Buddy",
#     model = "gpt-3.5-turbo",
#     instructions = "You are a study partner for students who are newer to technology. When you answer prompts, do so with simple language suitable for someone learning fundamental concepts.",
#     tools=[]
# )


# user_input = ""

# #create a thread
# thread = client.beta.threads.create()

# while True:
#     if user_input == "":
#         user_input = input("Chatbot: Hello! What's your name? ")
#         user_name = f"User's name: {user_input}"
#     else:
#         #prmpt the user to input a message
#         user_input = input("You: ")

#     if user_input.lower() == "exit":
#         print(f"Chatbot: Goodbye {user_name}")
#         exit()

#     #use the prompt to create a message within the thread
#     message = client.beta.threads.messages.create(
#         thread_id = thread.id,
#         role = "user",
#         content = user_input
#     )

#     run = process_run(thread.id, assistant.id)

#     log_run(run.status)

#     message = get_message(run.status)

#     print("Assistant: " + message)
