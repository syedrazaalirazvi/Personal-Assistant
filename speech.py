#Importing python package to convert text to speech
import pyttsx3

#creating pyttsx3 object
engine = pyttsx3.init('sapi5')

#setting properties for pyttsx3 object
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
engine.setProperty('rate',128)

#Function to say "input text"
def speak(text):
    engine.say(text)
    engine.runAndWait()


