from dotenv import load_dotenv
from langgraph.func import entrypoint, task
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key=os.getenv("GEMINI_API_KEY"))

@task 
def task1():
    return model.invoke("What is up?")

@task
def task2():
    return model.invoke("Hello there, how are you?")

@entrypoint()
def main(input):
    task1_result = task1().result()
    task2_result = task2().result()
    print(f"Task 1: {task1_result.content}, Task 2: {task2_result.content}")
    return f"{task1_result.content} {task2_result.content}"

if __name__ == "__main__":
    main.invoke(input="HHH")