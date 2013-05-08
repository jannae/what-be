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

# seps = ['IN','RB','MD','HV','DO','TO']

adjs = get_words(words_tagged,'J')
# verbs = get_words(words_tagged,'V')
nouns = get_words(words_tagged,'NN') # only common nouns
# whs = get_words(words_tagged,'W')
# bes = get_words(words_tagged,'B')
# advs = get_words(words_tagged,'R')
# qual = get_words(words_tagged,'Q')
conj = get_words(words_tagged,'CC')
pron = get_exact_words(words_tagged,'PPS')
moda = get_words(words_tagged,'MD')

# Create our collection of question beginnings
ques = []
ques = phrasebytag(sents_tagged,'W','BE')

preps = []
preps = phrasebytag(sents_tagged,'IN','AT')

verbph = []
verbph = phrasebytag(sents_tagged,'R','V')

nounph = []
nounph = phrasebytag(sents_tagged,'N','V')

#start fresh.
what = ''

# Begin with 'what'
# start = 'what'

# We'll do this a few times. Just 3 for now.
for x in range(0, iterate):
	print str(x)+'::'
	# Start with a random question
	qu = ran(ques)
	print qu
	what += str(qu[0])+' '

	pr = ran(preps)
	print pr

	vp = ran(verbph)
	print vp

	np = ran(nounph)
	print np

	what += chain_phrase(words_tagged,what.split()[-1],5)
	last = what.split()[-1]
	what += '?\n'
	what += last+', '+choice(tgram_by_tag(words_tagged,'PPS','MD'))+', '
	what += str(pr[0])
	what += '\n\n'

#print our dialogue!
print what