import speech_recognition as sr   #recognising the speech by the user
import pyttsx3         #text to speech conversion
import os              #interacting with os of the system.
import datetime        #current date and time acc to the system
import webbrowser      #convenient web browser controller. 

engine = pyttsx3.init()
COMMANDS = {
    "open youtube": lambda: webbrowser.open("https://youtube.com"),
    "open google": lambda: webbrowser.open("https://google.com"),
    "open wikipedia": lambda: webbrowser.open("https://wikipedia.com"),
    "open amazon": lambda: webbrowser.open("https://amazon.in"),
    "time":lambda:datetime.datetime.now().strftime("%H:%M"),
}

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening...")
        audio = recognizer.listen(source)
    try: 
        command = recognizer.recognize_google(audio)
        print("You said: ",command)
        return command.lower()
    
    except sr.UnknownValueError:
        speak("Sorry, I didn't get that")
        return  ""
    except sr.RequestError:
        speak("Speech service is down")
        return ""

def main():
    speak("Hello!. I am Wall-E. Amogh's very own personalised action bot. How can I help you today?")
    for key, action in COMMANDS.items():
        if key in command:
            result = action()
            if result: 
                speak(f"the time is {result}")
            break
        else:
            speak("I don't understand that command yet.")
main()