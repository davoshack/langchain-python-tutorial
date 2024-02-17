import os

from dotenv import load_dotenv
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from pydantic.v1 import BaseModel, Field


class Country(BaseModel):
    capital: str = Field(description="The capital of the country")
    name: str = Field(description="The name of the country")


load_dotenv()

OPENAI_MODEL = "gpt-4"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

PROMPT_COUNTRY_INFO = """
    Provide information about the country of {country}.
    {format_instructions}
"""


def main():
    parser = PydanticOutputParser(pydantic_object=Country)

    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL)
    # get user input
    country = input("Enter a country: ")

    message = HumanMessagePromptTemplate.from_template(template=PROMPT_COUNTRY_INFO)
    chat_prompt = ChatPromptTemplate.from_messages(messages=[message])
    chat_prompt_with_values = chat_prompt.format_prompt(
        country=country, format_instructions=parser.get_format_instructions()
    )
    response = llm(chat_prompt_with_values.to_messages())
    data = parser.parse(response.content)

    print(data)


if __name__ == "__main__":
    main()
