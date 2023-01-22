from app import app
from flask import jsonify, Response
from rise_and_shine.text_generator import TextGenerator
from rise_and_shine.azure_text_to_speech import AzureTextToSpeech

tg = TextGenerator()
tts = AzureTextToSpeech()


@app.route("/")
def hello():
    return jsonify(message="Hello, World!")


# TODO Adjust this route so it would be able to accept POST request with json payload,
#      with parameters bio and voice (male, female)
@app.route("/api/v1/generate")
def generate_text():
    return Response(tts.convert_to_speech(gender="female", language="english",
                                          text=tg.send_generate_motivation(language="english",
                                                                           gender="female")),
                    mimetype="audio/mp3")

