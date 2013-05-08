# Import my collection of functions for use with nltk.
import nltkjj
import sys
from nltkjj import *

from nltk.corpus import brown
from random import choice, randint

# text = ''
# for line in sys.stdin:
#     text += line
# brown categories: ['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']

if len(sys.argv) > 1:
	cats = list(str(sys.argv[1]))
	iterate = int(sys.argv[2])
else:
	cats = ['adventure', 'fiction', 'humor', 'mystery', 'romance', 'science_fiction']
	iterate = 3

words = brown.words(categories=cats)
sents = brown.sents(categories=cats)
words_tagged = brown.tagged_words(categories=cats)
sents_tagged = brown.tagged_sents(categories=cats)

# Create our collection of phrases to be mucked together
# ques = preps = verbph = nounph = []

# Question beginnings
ques = phrasebytag(sents_tagged,'W','BE')
# Prepositional phrases
preps = phrasebytag(sents_tagged,'IN','AT')
# Verb phrases
verbph = phrasebytag(sents_tagged,'R','V')
# Noun phrases
nounph = phrasebytag(sents_tagged,'N','V')
# Special pronoun phrase for mocking
mock = bgram_by_tag(words_tagged,'PPS','MD')

#start fresh.
what = ''

# We'll do this a few times. Just 3 for now.
for x in range(0, iterate):
	# print str(x)+'::'
	# Start with a random question

	what += str(ran(ques)[0])+' '
	what += chain_phrase(words_tagged,what.split()[-1],5)
	last = what.split()[-1]
	what += '?\n'

	# what += last+', '+choice(bgram_by_tag(words_tagged,'PPS','MD'))+', '
	what += last+', '+str(ran(mock))+', '
	what += str(ran(verbph)[0])+' '
	what += choice(bgram_phrase(words_tagged,what.split()[-1]))+' '
	what += str(ran(preps)[0])
	what += '\n\n'

#print our dialogue!
print what