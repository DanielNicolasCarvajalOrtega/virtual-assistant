import speech_recognition as sr
from googletrans import Translator
import time
from app.functions.text_to_speech import config


translator = Translator()
recognizer = sr.Recognizer()
voice_say = config()

def recognize_speech():
    with sr.Microphone() as source:
        print("Listening for speech...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")
        recognized_text = recognizer.recognize_google(audio, language='es-ES')
        print(f"Recognized text: {recognized_text}")
        return recognized_text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
        voice_say.engine.runAndWait()
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None


def translate_text_to_english(text, target_language='en'):
    try:
        translation = translator.translate(text, dest=target_language) # Traducir el texto al inglés
        translated_text = translation.text
        print(f"Translated text: {translated_text}")
        return translated_text

    except Exception as err:
        print(f"Error translating text: {err}")
        voice_say.engine.say("There was an error during the translation.")
        voice_say.engine.runAndWait()
        return None


def speak_text(text):
    voice_say.engine.say(text)
    voice_say.engine.runAndWait()

def main_translated():
    # El asistente comienza saludando pero no escucha hasta que detecta la palabra clave
    speak_text("Hello, I'm ready. Say 'translation idiom' when you need me.")

    while True:
        print("Waiting for keyword 'translation idiom'...")
        recognized_text = recognize_speech() # Escuchar hasta que detecte la palabra clave
        if recognized_text and 'translation idiom' in recognized_text.lower():
            print("Keyword recognized!")
            speak_text("I'm listening, please tell me what you want me to translate.")


            time.sleep(1)
            print("Listening for text to translate...")
            text_to_translate = recognize_speech()  # Escuchar el texto a traducir después de la palabra clave

            if text_to_translate:
                translated_text = translate_text_to_english(text_to_translate, 'en') # Traducir el texto al inglés
                if translated_text:
                    speak_text(f"The translation is: {translated_text}")
            else:
                speak_text("I didn't hear any text to translate.")
            time.sleep(1)   # Pausa para un flujo más natural

            speak_text("If you need another translation, just say 'translation idiom' again.")
        elif recognized_text and 'salir' in recognized_text.lower():
            break


if __name__ == '__main__':
    main_translated()