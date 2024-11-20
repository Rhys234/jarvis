import speech_recognition as sr
import pyttsx3

# Initialisiere Spracherkennung und Sprachausgabe
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Spricht den übergebenen Text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Hört Sprachbefehle und gibt sie als Text zurück."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            speak("Network error. Please check your connection.")
            return None
