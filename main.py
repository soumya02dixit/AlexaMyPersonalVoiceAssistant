import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
     try:
         with sr.Microphone() as source:
             print('listening...')
             voice = listener.listen(source)
             command = listener.recognize_google(voice)
             command = command.lower()
             if 'alexa' in command:
                 command = command.replace('alexa', '')
                 print(command)
     except:
         pass
     return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)

    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'how are you' in command:
        talk('I am good , what about you?')
    elif 'morning' in command:
        talk('Very good morning')
    elif 'master' in command:
        talk('I m assistant of soumya dixit')
    elif 'help' in command:
        talk('how can i help you dear')
    elif 'introduce' in  command:
        talk('Hello this is blabby, a personal assistant working on your instructions')
    elif 'evening' in command:
        talk('good evening')

    elif "night" in command:
        talk('good night and sleep well')
    elif 'developer' in command:
        talk('soumya dixit , is a student at vit computer science and engineering branch.She is passionate about web development and currently my developer and master ')
    elif'joke' in command:
        talk(pyjokes.get_joke())
    elif 'thank' in command:
        talk('your welcome')

    else:
        talk('please say it again')


while True:
    run_alexa()













