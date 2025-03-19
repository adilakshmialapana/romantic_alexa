import speech_recognition as sr  # Import speech recognition module
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize recognizer
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    """Function to make Alexa speak"""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Function to take voice input and convert it to text"""
    command = ""  # ✅ Initialize command to avoid UnboundLocalError

    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)  # Listen to audio input
            command = listener.recognize_google(voice)  # Convert speech to text
            command = command.lower()

            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
                print(f"Command received: {command}")  # Debugging output


    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")  # If speech is not clear
    except sr.RequestError:
        print("Could not request results, check your internet connection.")  # If API request fails
    except Exception as e:
        print(f"Error: {e}")  # Print any other errors

    return command  # ✅ Ensures a value is always returned

def run_alexa():
    """Function to process the command and respond"""
    command = take_command()

    if 'play' in command:
        song=command.replace('play','')
        talk('Playing'+song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        print(time)
        talk('current time is ' + time)
    elif 'who the heck is ' in command:
        person=command.replace('who the heck is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, i have a headache')
    elif 'are you single' in command:
        talk(' im a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('pls say the command again')


while True:
   run_alexa()  # Start the Alexa function

