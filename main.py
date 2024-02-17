import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

load_dotenv()

OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def main():
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL)
    result = llm.invoke("Give five examples of animals that can fly.")
    print(result)


if __name__ == "__main__":
    main()
