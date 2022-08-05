from gtts import gTTS


class TextReader:
    def __init__(self, text="", lang="ru", slow="False"):
        self.text = text
        self.lang = lang
        self.slow = slow

    def convert_to_audio_and_save(self, name="default"):
        file = gTTS(text=self.text, lang=self.lang, slow=self.slow)
        file.save(name + ".mp3")
