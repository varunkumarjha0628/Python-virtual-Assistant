import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLiburary


#create a virtual assistant
def virtual_assistant():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Function to speak text
    def speak(text):
        engine.say(text)
        engine.runAndWait()

    # Function to listen for audio and recognize speech
    def listen():
        with sr.Microphone() as source:
            print("Listening...")           
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                print(f"You said: {command}")
                return command.lower().strip()
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
                return ""
            except sr.RequestError:
                print("Could not request results; check your network connection.")
                return ""

    # Main loop
    while True:
        command = listen()
        if not command:  # Skip empty commands
            speak("Sorry, I didn't catch that. Please try again.")
            continue

        # Exit command
        if "exit" in command or "stop" in command:
            speak("Goodbye")
            break

        # Greeting and conversation
        if "hello" in command or "hi" in command:
            speak("Hello! How can I assist you today?")
        elif "how are you" in command:
            speak("I am fine, and you?")
            if "good" in command or "fine" in command:
                speak("Great to hear that!")
            elif "bad" in command:
                speak("I am sorry to hear that.")
        elif "what a busy day" in command:
            speak("Why sir?")
            if "i am busy" in command:
                speak("I understand, take your time.")
            elif "i am tired" in command:
                speak("Rest is important, take care of yourself.")
            elif "i am bored" in command:
                speak("Let's find something fun to do!")
        elif "what's your name" in command:
            speak("I am your virtual assistant.")                
        elif "open" in command:
            try:
                if "google" in command:
                    webbrowser.open("https://www.google.com")
                    speak("Opening Google")
                elif "youtube" in command:
                    webbrowser.open("https://www.youtube.com")
                    speak("Opening YouTube")
                elif "twitter" in command:
                    webbrowser.open("https://www.twitter.com")
                    speak("Opening Twitter")
                elif "instagram" in command:    
                    webbrowser.open("https://www.instagram.com")
                    speak("Opening Instagram")
                elif "facebook" in command:
                    webbrowser.open("https://www.facebook.com")
                    speak("Opening Facebook")
                elif "github" in command:
                    webbrowser.open("https://www.github.com")
                    speak("Opening GitHub")
                elif "music" in command:
                    music_name = command.split("music")[-1].strip()
                    if music_name in musicLiburary.music:
                        webbrowser.open(musicLiburary.music[music_name])
                        speak(f"Playing {music_name} music")
                    else:
                        speak("Sorry, I don't have that music.")

                elif "exit" in command or "stop" in command:
                 speak("Goodbye")
                 break
            except Exception as e:
                speak("Sorry, I couldn't open the website.")
                print(f"Error opening website: {e}")
        else:
            speak("close the program")
            break
# Run the virtual assistant
if __name__ == "__main__":
    virtual_assistant()