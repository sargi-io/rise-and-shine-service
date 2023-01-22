from app import app
from flask import jsonify, Response
from rise_and_shine.text_generator import TextGenerator
from rise_and_shine.text_to_speech import TextToSpeech

tg = TextGenerator()
tts = TextToSpeech()


@app.route("/")
def hello():
    return jsonify(message="Hello, World!")


# TODO Adjust this route so it would be able to accept POST request with json payload,
#      with parameters bio and voice (male, female)
@app.route("/api/v1/generate")
def generate_text():
    return Response(tts.text_to_speech(
        motivation=tg.send_generate_motivation())['AudioStream'].read(), mimetype='audio/mp3')

