import os
import json
import azure.cognitiveservices.speech as speechsdk


class AzureTextToSpeech:
    def __init__(self):
        # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        self.speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'),
                                                    region=os.environ.get('SPEECH_REGION'))
        self.audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        self.voices_config = json.load(open(r"configs/voices.json"))

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

    def convert_to_speech(self, language, gender, text):
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config,
                                                         audio_config=self.audio_config)

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
    atts = AzureTextToSpeech()
    atts.convert_to_speech("czech", "male", "Ahoj světe! Toto je příklad textu pro převod na hlas pomocí Azure Speech.")
