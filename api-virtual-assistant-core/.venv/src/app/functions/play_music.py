from app.model.Repositories import AssistantRepository
from app.functions.text_to_speech import config
from googleapiclient.discovery import build
import speech_recognition as sr
import webbrowser


voice_say = config()
recognizer = sr.Recognizer()
youtube_api_key = "AIzaSyAZziCEkXYO_2hxHvLcNox2Kz7fNrq87ME"
youtube = build("youtube", "v3", developerKey=youtube_api_key)
def listen_commands():
    with sr.Microphone() as source:
        print("Listening...")
        while True:
            try:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio).lower()
                voice_say.engine.say(f"Command: {command}")
                voice_say.engine.runAndWait()


                if "music play" in command or "another song" in command:
                    play_music()

                elif "thank you" in command or "you are a genius" in command:
                    voice_say.engine.say("enjoy the music")
                    voice_say.engine.runAndWait()

                elif "exit" in command or "stop" in command:
                    voice_say.engine.say("fuck off")
                    voice_say.engine.runAndWait()
                    break

            except sr.UnknownValueError:
                voice_say.engine.say("I didn't understand the order.")
                voice_say.engine.runAndWait()
            except sr.RequestError as re:
                voice_say.engine.say(f"Error connecting to the service: {re}")
                voice_say.engine.runAndWait()

def play_music():
    with sr.Microphone() as source:
        voice_say.engine.say("Tell me what song you want to hear")
        voice_say.engine.runAndWait()
        try:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            song = recognizer.recognize_google(audio).lower()
            voice_say.engine.say(f"reproducing {song}")
            voice_say.engine.runAndWait()

            search_response = youtube.search().list(
                q=song,
                part="id,snippet",
                maxResults=1,
                type="video"

            ).execute()

            video_id = search_response["items"][0]["id"]["videoId"]

            webbrowser.open(f"https://www.youtube.com/watch?v={video_id}")
        except sr.UnknownValueError:
            voice_say.engine.say("I didn't understand the order.")
            voice_say.engine.runAndWait()
        except sr.RequestError as re:
            voice_say.engine.say(f"Error connecting to the service: {re}")
            voice_say.engine.runAndWait()




listen_commands()