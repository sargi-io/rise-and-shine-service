import os
import openai
import json


class TextGenerator:
    def __init__(self):
        openai.api_key = os.getenv(key="OPENAI_API_KEY")

    # TODO - Improve this prompt to get better motivational speeches
    @staticmethod
    def __motivation_speech_prompt(bio, language, gender):
        return f"""Generate motivation speech based on following bio for me from perspective of 
        {gender} to get me out of bed. Use following information about me, to make it more personal: {bio}.
        Speech should start with Good morning or {language} equivalent based on the whole text.
        Add inspiration quote at the end which should start with "And here is quote for today"
        and it should not include quote author.
        There should be limitation 100 words
        Final text should be in {language}"""

    def send_generate_motivation(self, bio="", language="english", gender="female"):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.__motivation_speech_prompt(bio, language, gender),
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


