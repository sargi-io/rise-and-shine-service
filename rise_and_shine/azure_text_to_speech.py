import os
import json
from rise_and_shine.text_generator import TextGenerator
import azure.cognitiveservices.speech as speechsdk


class AzureTextToSpeech:
    def __init__(self):
        self.speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'),
                                                    region=os.environ.get('SPEECH_REGION'))
        self.voices_config = json.load(open(r"configs/voices.json"))
        self.text_gen = TextGenerator()

    def __prepare_ssml(self, language, gender, text):
        speaker = self.voices_config[language][gender]
        print(speaker[:5])
        return f"""
                <speak version="1.0" xml:lang="{speaker[:5]}">
                    <voice name="{speaker}">
                        <prosody rate="-4">
                            <style name="hopeful">{text}</style>
                        </prosody>
                    </voice>
                </speak>
               """

    def convert_to_speech(self, file_id, language, gender, bio):
        self.audio_config = speechsdk.audio.AudioOutputConfig(filename=f"{file_id}.wav")
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config,
                                                         audio_config=self.audio_config)

        text = self.text_gen.send_generate_motivation(gender=gender, language=language, bio=bio)
        speech_synthesis_result = speech_synthesizer.speak_ssml_async(
            self.__prepare_ssml(language, gender, text)).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}]".format(text))
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")


if __name__ == "__main__":
    azure_text_speech = AzureTextToSpeech()
    azure_text_speech.convert_to_speech("english", "female", "This is text that needs to be said")