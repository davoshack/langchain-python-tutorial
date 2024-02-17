import os

from dotenv import load_dotenv
from langchain.chains import APIChain
from langchain.chains.api import open_meteo_docs
from langchain_openai import OpenAI

load_dotenv()

OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def main():
    llm = OpenAI(temperature=0)

    chain_new = APIChain.from_llm_and_api_docs(
        llm,
        open_meteo_docs.OPEN_METEO_DOCS,
        verbose=False,
        limit_to_domains=["https://api.open-meteo.com/"],
    )
    result = chain_new.run(
        "What is the weather like right now in Medellin, Colombia in degrees Celcius?"
    )
    print(result)


if __name__ == "__main__":
    main()
