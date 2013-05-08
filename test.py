import nltkjj
import sys
from nltkjj import *

from nltk.corpus import brown
from random import choice, randint

if len(sys.argv) > 1:
	cat = str(sys.argv[1])
	stanzas = int(sys.argv[2])
else:
	cat = 'fiction'
	stanzas = 5

words = brown.words(categories=cat)
sents = brown.sents(categories=cat)
words_tagged = brown.tagged_words(categories=cat)
sents_tagged = brown.tagged_sents() #categories=cat)

def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                  if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].keys()[:5]) for tag in cfd.conditions())
 	
# tagdict = findtags('W', nltk.corpus.brown.tagged_words(categories='news'))
# for tag in sorted(tagdict):
# 	print tag, tagdict[tag]

brown_learned_text = brown.words(categories='learned')
sorted(set(b for (a, b) in nltk.ibigrams(brown_learned_text) if a == 'what'))


# def process(sentence):
#     for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence): 
#         if (t1.startswith('WD') or t1.startswith('WR')) and t2.startswith('BE'): 
#             print w1, w2, w3

pos = nltk.defaultdict(lambda: nltk.defaultdict(int))
brown_news_tagged = brown.tagged_words(categories='fiction', simplify_tags=True)
for ((w1, t1), (w2, t2)) in nltk.ibigrams(brown_news_tagged): 
	pos[w1][t2] += 1 

print pos['and']
