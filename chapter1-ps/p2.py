import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("Manish is a good boy and he is gonna start his personal brand named as manish_does, and it will definetly work")
engine.runAndWait()
