import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def main():
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
    result = llm.invoke("Give five examples of animals that can fly.")
    print(result)


if __name__ == "__main__":
    main()
