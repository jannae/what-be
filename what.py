# Import my collection of functions for use with nltk.
import nltkjj
import sys
from nltkjj import *

from nltk.corpus import brown
from random import choice, randint

# brown categories: ['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']

cats = ['adventure', 'fiction', 'humor', 'mystery', 'romance', 'science_fiction']

if len(sys.argv) > 1:
	iterate = int(sys.argv[1])
else:
	iterate = 3

words_tagged = brown.tagged_words(categories=cats)
sents_tagged = brown.tagged_sents(categories=cats)

# Create our collection of phrases to be mucked together
# Question beginnings
ques = phrase_by_tag(sents_tagged,'W','BE')
# Prepositional phrases
preps = phrase_by_tag(sents_tagged,'IN','AT')
# Prepositional phrases
verbph = phrase_by_tag(sents_tagged,'R','V')
# Special pronoun phrase for mocking
mock = bgram_by_tag(words_tagged,'PPS','MD')

#start fresh.
what = []

# We'll do this a few times. Just 3 for now.
for x in range(0, iterate):
	# print str(x)+'::'
	what.append(x)

	# Start with a random question fragment
	what[x] = str(ran(ques)[0])+' '

	# Let's hang on to the generated chain
	chain = chain_phrase(words_tagged,what[x].split()[-1],5)

	what[x] += chain

	# Hang on to the last subject word.
	last = what[x].split()[-1]

	what[x] += '?\n'

	# Repeat the last subject of the question. Mock it. Repeat the question annoyingly.
	what[x] += last+', '+str(ran(mock))
	last = what[x].split()[-1]
	what[x] += '. '+what[x].split()[0]+'?\n'

	# Repeat original question's predicate
	what[x] += what[x].split()[1]+' '+what[x].split()[2]+'. '

	# Seemingly eager verb phrase
	what[x] += str(ran(verbph)[0])+' '
	# Chain based on verb phrase
	what[x] += chain_phrase(words_tagged,what[x].split()[-1])+', '
	# Repeat the final bit of the original question
	what[x] += chain.split()[-2]+' '+chain.split()[-1]+' '
	# Prepositional phrase to end the sentence
	what[x] += str(ran(preps)[0])+'...'

#print our dialogue!
print '\n\n'.join(what)