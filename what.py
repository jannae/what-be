"""
    What? Be.

    Dependencies:
        [Natural Language Toolkit 2.0](http://nltk.org/)
        (using the [Brown Corpus](http://icame.uib.no/brown/bcm.html))

        sudo pip install -U numpy pyyaml nltk
        sudo python -m nltk.downloader -d /usr/share/nltk_data all

    Usage (arguments can be empty):
        python what.py <number of iterations (def=3)>
"""

import sys
from nltkjj import chain_phrase, ran, phrase_by_tag, bgram_by_tag

from nltk.corpus import brown

# brown categories:
#   ['adventure', 'belles_lettres', 'editorial', 'fiction', 'government',
#    'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion',
#    'reviews', 'romance', 'science_fiction']

CATS = ['adventure', 'fiction', 'humor', 'mystery', 'romance', 'science_fiction']

if len(sys.argv) > 1:
    ITERATE = int(sys.argv[1])
else:
    ITERATE = 3

WORDS_TAGGED = brown.tagged_words(categories=CATS)
SENTS_TAGGED = brown.tagged_sents(categories=CATS)

# Create our collection of phrases to be mucked together
# Question beginnings
QUES = phrase_by_tag(SENTS_TAGGED, 'W', 'BE')
# Prepositional phrases
PREPS = phrase_by_tag(SENTS_TAGGED, 'IN', 'AT')
# Prepositional phrases
VERBPH = phrase_by_tag(SENTS_TAGGED, 'R', 'V')
# Special pronoun phrase for mocking
MOCK = bgram_by_tag(WORDS_TAGGED, 'PPS', 'MD')

#start fresh.
WHAT = []

# We'll do this a few times. Just 3 for now.
for x in range(0, ITERATE):
    # print str(x)+'::'
    WHAT.append(x)

    # Start with a random QUEStion fragment
    WHAT[x] = str(ran(QUES)[0])+' '

    # Let's hang on to the generated chain
    chain = chain_phrase(WORDS_TAGGED, WHAT[x].split()[-1], 5)

    WHAT[x] += chain

    # Hang on to the last subject word.
    last = WHAT[x].split()[-1]

    WHAT[x] += '?\n'

    # Repeat the last subject of the QUEStion. Mock it. Repeat the QUEStion annoyingly.
    WHAT[x] += last+', '+str(ran(MOCK))
    last = WHAT[x].split()[-1]
    WHAT[x] += '. '+WHAT[x].split()[0]+'?\n'

    # Repeat original QUEStion's predicate
    WHAT[x] += WHAT[x].split()[1]+' '+WHAT[x].split()[2]+'. '

    # Seemingly eager verb phrase
    WHAT[x] += str(ran(VERBPH)[0])+' '
    # Chain based on verb phrase
    WHAT[x] += chain_phrase(WORDS_TAGGED, WHAT[x].split()[-1])+', '
    # Repeat the final bit of the original QUEStion
    WHAT[x] += chain.split()[-2]+' '+chain.split()[-1]+' '
    # Prepositional phrase to end the sentence
    WHAT[x] += str(ran(PREPS)[0])+'...'

#print our dialogue!
print '\n\n'.join(WHAT)
