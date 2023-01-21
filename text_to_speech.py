import os
import boto3


class TextToSpeech:
    def __init__(self):
        self.polly_client = boto3.Session(
                        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID_POLLY"),
                        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY_POLLY"),
                        region_name='eu-central-1').client('polly')
        self.aws_access_key_id = None
        self.aws_secret_access_key = None

    # TODO Implement check on the voice ID. Throw error if incorrect voice.
    def text_to_speech(self, motivation="Another Test", voice="Matthew"):
        return self.polly_client.synthesize_speech(VoiceId=voice,
                                                   OutputFormat='mp3',
                                                   Text=motivation,
                                                   Engine='neural')


if __name__ == "__main__":
    ttp = TextToSpeech()
    file = open('speech.mp3', 'wb')
    file.write(ttp.text_to_speech()['AudioStream'].read())
    file.close()


