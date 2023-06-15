import pyttsx3
import time

engine = pyttsx3.init()
engine.setProperty("voice", engine.getProperty("voices")[44].id)
engine.setProperty("rate", 170)
string = '''
Hello Everyone. Today I shall talk on the
topic Computer Vision.
'''
engine.say(string)
# engine.save_to_file(string, '1.mp3')
engine.runAndWait()

'''
voices = engine.getProperty("voices")
count = 1
lst = [3, 4, 11, 12, 13, 15, 30, 34, 37, 38, 44, 45, 52, 68]
for voice in voices:
	if count in lst:
		engine.setProperty("voice", voice.id)
		print(count, voice, voice.id)
		engine.say("Hello World")
		engine.runAndWait()
	count += 1
'''

