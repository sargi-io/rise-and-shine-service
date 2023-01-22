import os
import openai
import json

from jinja2.lexer import TOKEN_DOT


class TextGenerator:
    def __init__(self):
        openai.api_key = os.getenv(key="OPENAI_API_KEY")

    # TODO - Improve this prompt to get better motivational speeches
    @staticmethod
    def __motivation_speech_prompt(bio):
        return f"""Generate motivation speech based on following bio for me to get me out of bed. Here is the bio: {bio}.
        Speech should start with Good morning.
        Add inspiration quote at the end"""

    def send_generate_motivation(self, bio=""):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.__motivation_speech_prompt(bio),
            temperature=1,
            max_tokens=300
        )
        json_response = json.loads(str(response))
        return json_response["choices"][0]["text"]


if __name__ == "__main__":
    bio_txt = open("../bio_example.txt", "r")
    print(str(bio_txt.read()).strip())
    tg = TextGenerator()
    print(tg.send_generate_motivation(bio=str(bio_txt.read()).strip()))


