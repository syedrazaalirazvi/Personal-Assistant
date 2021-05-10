# Personal-Assistant

Developed using Python 3.9.5

Python packages used:
    pyttsx3

## speech.py

Initialises a pyttsx3 object by the name engine and makes it use the sapi5 
engine which is default in Windows machine. 
pyttsx3 uses nsss (NSSpechSynthesizer) in Mac OS X and eSpeak in other
platforms.

### The reason I have used pyttsx3 instead of gTTS is:

gTTS which works perfectly in python3 but it needs internet connection to 
work since it relies on google to get the audio data. But Pyttsx is completely 
offline and works seemlesly and has multiple tts-engine support.

Also has a function speech.speak(text):
Which converts the given string as argument to speech output.

## Start.py

has strings which stores messages to be read out as output at the start of
AI and accomplishes it using speech.py module created by us.

#### Example:
    
    text = 'Hi! My Name is VIS. I have been developed by Syed Raza Ali Razvi'
    speech.speak(text)
    
The above code results in a speech output:

Hi! My name is VIS. I have been developed by Syed Raza Ali Razvi.
