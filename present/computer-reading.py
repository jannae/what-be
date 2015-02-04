"""
    What? Be. Performance script.
    Reads the piped output for playing various parts in the "play."
"""

from  AppKit import NSSpeechSynthesizer
import time

from datetime import datetime

STARTTIME = datetime.now()

# http://stackoverflow.com/questions/12758591/python-text-to-speech-in-macintosh

NSSP = NSSpeechSynthesizer
SPEAK = NSSP.alloc().init()

# voices = ["com.apple.speech.synthesis.voice.Alex",
# "com.apple.speech.synthesis.voice.Vicki",
# "com.apple.speech.synthesis.voice.Victoria" ]

ALEX = "com.apple.speech.synthesis.voice.Alex"
VICKI = "com.apple.speech.synthesis.voice.Vicki"
VICTORIA = "com.apple.speech.synthesis.voice.Victoria"

# for voice in NSSP.availableVoices():
# for voice in voices:

def talky(voice, txt):
    """
        Talky, "speaks" provided text using preferred voice.
    """
    SPEAK.setVoice_(voice)
    spk = str(voice).split('.')[-1].title()
    print spk+': '+txt
    SPEAK.startSpeakingString_(txt)
    while SPEAK.isSpeaking():
        time.sleep(1)

LINE = 1

for line in open('read'):
    line = line.strip()
    if LINE%2 is not 0:
        talky(VICTORIA, line)
    else:
        if line is not "":
            talky(ALEX, line)
        else:
            time.sleep(2)
            print '\n'
    LINE += 1

print datetime.now()-STARTTIME
