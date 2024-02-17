import os

import openai
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser

OPENAI_MODEL = "gpt-4"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


def main(url, file_path):
    loader = GenericLoader(
        YoutubeAudioLoader([url], os.path.dirname(file_path)), OpenAIWhisperParser()
    )
    docs = loader.load()
    with open(file_path, "w", encoding="utf-8") as f:
        for doc in docs:
            f.write(doc.page_content)

    return docs


if __name__ == "__main__":
    youtube_url = "https://youtu.be/CYTwGx43SzY"
    file_path = "/Users/davoscode/Documents/Documents - Juan’s MacBook Air/Coding/data_science_playground/langchain-python-tutorial/3_things_never_do_in_the_morning.txt"

    main(youtube_url, file_path)
