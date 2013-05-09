from  AppKit import NSSpeechSynthesizer
import time
import sys

from datetime import datetime

startTime = datetime.now()

# http://stackoverflow.com/questions/12758591/python-text-to-speech-in-macintosh

nssp = NSSpeechSynthesizer
speak = nssp.alloc().init()

# voices = ["com.apple.speech.synthesis.voice.Alex",
# "com.apple.speech.synthesis.voice.Vicki",
# "com.apple.speech.synthesis.voice.Victoria" ]

alex = "com.apple.speech.synthesis.voice.Alex"
vicki = "com.apple.speech.synthesis.voice.Vicki"
victoria = "com.apple.speech.synthesis.voice.Victoria"

# for voice in nssp.availableVoices():
# for voice in voices:

def talky(voice,txt):
	speak.setVoice_(voice)
	spk = str(voice).split('.')[-1].title()
	print spk+': '+txt
	speak.startSpeakingString_(txt)
	while speak.isSpeaking():
		time.sleep(1)

l = 1

for line in open('read'):
	line = line.strip()
	if l%2 is not 0:
		talky(victoria,line)
	else:
		if line is not "":
			talky(alex,line)
		else:
			time.sleep(2)
			print '\n'
	l += 1


print(datetime.now()-startTime)