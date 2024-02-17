import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate


load_dotenv()

OPENAI_MODEL = "gpt-4"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

PROMPT_COUNTRY_INFO = """
    Provide information about the country of {country}.
"""


def main():
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL)

    # get user input
    country = input("Enter a country: ")

    message = HumanMessagePromptTemplate.from_template(template=PROMPT_COUNTRY_INFO)
    chat_prompt = ChatPromptTemplate.from_messages(messages=[message])
    chat_prompt_with_values = chat_prompt.format_prompt(country=country)
    response = llm(chat_prompt_with_values.to_messages())

    print(response)


if __name__ == "__main__":
    main()
