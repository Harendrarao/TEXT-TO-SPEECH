from gtts import gTTS
import os
import time
tts = gTTS(input("Enter the SCRIPT you want to convert: "), lang="en")
tts.save("intro.mp3")
os.system("start intro.mp3")
time.sleep(5)
