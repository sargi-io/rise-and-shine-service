from app import app
import uuid
import os
from flask import request, Response
from rise_and_shine.azure_text_to_speech import AzureTextToSpeech

tts = AzureTextToSpeech()


@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello world"


@app.route("/api/v1/generate", methods=["POST"])
def generate_text():
    file_id = uuid.uuid4()
    gender = request.get_json()["gender"]
    language = request.get_json()["language"]
    bio = request.get_json()["bio"]

    try:
        tts.convert_to_speech(file_id=file_id,
                              gender=gender,
                              language=language,
                              bio=bio)
        with open(f"{file_id}.wav", "rb") as f:
            file_data = f.read()
        response = Response(file_data, content_type="audio/wav",
                            headers={"Content-disposition": f"attachment;{file_id}.wav"})
        return response
    finally:
        os.remove(f"{file_id}.wav")




