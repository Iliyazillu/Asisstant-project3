import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()



def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("I'm listening")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that.")
    except sr.RequestError:
        speak("Network error.")
    return ""

def open_website(command):
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open ajio" in command:
        speak("Opening ajio")
        webbrowser.open("https://www.ajio.com/")
    elif "hello" in command:
        speak("What the fuck do you want..anytime alexa alexa.. what uou want.")
    elif "intresting song" in command:
        webbrowser.open("https://www.youtube.com/watch?v=6OXfgu8uKnE")
    elif "item song" in command:
        speak("open youtube")
        webbrowser.open("https://www.youtube.com/watch?v=FZLadzn5i6Q&list=RDGMEM916WJxafRUGgOvd6dVJkeQ&index=3")
    elif "romantic song" in command:
        speak("open youtube")
        webbrowser.open("https://www.youtube.com/watch?v=hHuG7FIKgtc")
    elif "didi ke liye ek gaana" in command:
        speak("open youtube")
        webbrowser.open("https://www.youtube.com/watch?v=OkpIoEC44kk")
    elif "emaan" in command:
        speak("open youtube")
        webbrowser.open("https://www.youtube.com/watch?v=QXGuAwrfSz8")

    else:
        speak("Sorry, I don't know how to open that.")

# Main loop
if __name__ == "__main__":
    speak("Hello Iliyaz, I am your assistant. What would you like me to do?")
    while True:
        command = listen()
        if command:
            if "exit" in command or "quit" in command or "stop" in command:
                speak("Goodbye!")
                break
            open_website(command)
