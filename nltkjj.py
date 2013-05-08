import nltk
import re
import sys
import random
import string

from random import choice, randint

# Function for returning a unique list of words from a certain part of speech (tag) from a tagged corpus of words
def get_words(words_tagged,tag_prefix):
	words = []
	for (word, tag) in words_tagged:
		if tag.startswith(tag_prefix):
			words.append(word.lower())
	return list(set(words))

# Function for returning a unique list of words from a certain part of speech (tag) from a tagged corpus of words
def get_exact_words(words_tagged,exact_tag):
	words = []
	for (word, tag) in words_tagged:
		if tag == exact_tag:
			words.append(word.lower())
	return list(set(words))

# Function for returning a trigram based on parts of speech tagged words from a tagged corpus of sentences
def tgram_by_tag(tagged,tag_pre1,sep):
	tgrams = []
	for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(tagged):
		if t1.startswith(tag_pre1) and t2.startswith(sep):
			tgrams.append(w1.lower() +' '+ w2.lower() +' '+ w3.lower())
	return list(set(tgrams))

# Function for returning a trigram based on parts of speech tagged words from a tagged corpus of sentences
def bgram_by_tag(tagged,tag_pre1,tag_pre2):
	bgrams = []
	for (w1,t1), (w2,t2) in nltk.bigrams(tagged):
		if t1.startswith(tag_pre1) and t2.startswith(tag_pre2):
			bgrams.append(w1.lower() +' '+ w2.lower())
	return list(set(bgrams))

# Function for returning a bigram for a particular word from a tagged corpus of words
def bgram_by_word(words,rel_word):
	return list(set(w2.lower() for (w1, w2) in nltk.ibigrams(words) if w1 == rel_word))

# Function for returning a bigram for a particular word based on the most likely following tag
def bgram_word_tag(tagged,rel_word,tag):
	bgrams = []
	for ((w1, t1), (w2, t2)) in nltk.bigrams(tagged):
		if w1 == rel_word and t2.startswith(tag[0]):
			bgrams.append(w2.lower())
	if len(bgrams) == 0:
		bgrams.append(ran(get_words(tagged,tag[0])))
	return list(set(bgrams))

# Function for returning a bigram for a particular word to follow a phrase based on the most likely following tag of the last word in the phrase
def chain_phrase(tagged,rel_word,size=3):
	bgrams = []
	for i in xrange(size):
		tag = ran(depunc(nextags(tagged,rel_word)))
		if tag is not None:
			for ((w1, t1), (w2, t2)) in nltk.bigrams(tagged):
				if w1 == rel_word and t2.startswith(tag[0]):
					rel_word = w2.lower()
			if len(rel_word) == 0:
				rel_word = ran(get_words(tagged,tag[0]))
		else:
			rel_word = ran(get_words(tagged,'N'))
		bgrams.append(rel_word)
	return ' '.join(bgrams)

# Function for returning a list of trigram phrases based on a set of tags.
def phrase_by_tag(tagged,tag_pre1,tag_pre2):
	phrases = []
	for s in tagged:
		phrase = tgram_by_tag(s,tag_pre1,tag_pre2)
		if len(phrase) > 0:
			phrases.append(depunc(phrase))
	return phrases

# Function for returning and removing a random element from a list
def ran(listy):
	if len(listy) > 0:
		return listy.pop(random.randrange(len(listy)))

# Function for de-punctuating a list. (used mostly for cleaning bigrams)
def depunc(listy):
	listy = [''.join(c for c in s if c not in string.punctuation) for s in listy]
	listy = [s for s in listy if s]
	return listy

def nextags(tagged,word):
	tags = []
	for ((w1, t1), (w2, t2)) in nltk.ibigrams(tagged):
		if w1 == word:
			tags.append(t2)
	return list(set(tags))





