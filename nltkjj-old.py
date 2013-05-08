import nltk
import re
import sys
import random
import string

from random import choice, randint

# Used for processing an outside corpus.  (Not utilized for midterm, currently.)
def process_text(srctxt):
	# returns list of properly tokenized large piece of text
	sents = nltk.sent_tokenize(srctxt)
	sents = [nltk.pos_tag(sent) for sent in sents]
	sents = [nltk.word_tokenize(sent) for sent in sents]
	return sents

# Function for returning a unique list of words from a certain part of speech (tag) from a tagged corpus of words
def get_words(words_tagged,tag_prefix):
	words = []
	for (word, tag) in words_tagged:
		if tag.startswith(tag_prefix):
			words.append(word.lower())
	return list(set(words))

# Function for returning a unique list of parts of speech (tags) from a tagged corpus of words
def get_tags(words_tagged,tag_prefix):
	tags = []
	for (word, tag) in words_tagged:
		if len(tag_prefix) > 0:
			if tag.startswith(tag_prefix):
				tags.append(tag)
		else:
			tags.append(tag)
	return list(set(tags))

# Function for returning a trigram based on parts of speech tagged words from a tagged corpus of sentences
def tgram_by_tag(sents_tagged,tag_pre1,sep):
	tgrams = []
	for (word1,tag1), (word2,tag2), (word3,tag3) in nltk.trigrams(sents_tagged):
		if tag1.startswith(tag_pre1) and tag2.startswith(sep):
			tgrams.append(word1.lower() +' '+ word2.lower() +' '+ word3.lower())
	return list(set(tgrams))

# Function for returning a trigram based on a key word separated by a tagged word, and linked to any other word.
def tgram_by_word(sents_tagged,inword1,sep):
	tgrams = []
	for (word1,tag1), (word2,tag2), (word3,tag3) in nltk.trigrams(sents_tagged):
		if (word1 == inword1 and tag2 == sep) or (word3 == inword1 and tag2 == sep):
			tgrams.append(word1.lower() +' '+ word2.lower() +' '+ word3.lower())
	return list(set(tgrams))

# Function for returning a bigram for a particular word from a tagged corpus of words
def ibgram_tag_word(sents_tagged,tag_pre1,rel_word2):
	bgrams = []
	for (word1,tag1), (word2,tag2) in nltk.ibigrams(sents_tagged):
		if tag1.startswith(tag_pre1) and word2 == rel_word2:
			bgrams.append(word2.lower())
	return list(set(bgrams))

# Function for returning a bigram for a particular word from a tagged corpus of words
def ibgram_word_tag(sents_tagged,rel_word1,tag_pre2):
	bgrams = []
	for (word1,tag1), (word2,tag2) in nltk.ibigrams(sents_tagged):
		if word1 == rel_word1 and tag2.startswith(tag_pre2):
			bgrams.append(word2.lower())
	return list(set(bgrams))

# Function for returning a bigram for a particular word from a tagged corpus of words
def ibgram_by_word(words,rel_word):
	return list(set(word2.lower() for (word1, word2) in nltk.ibigrams(words) if word1 == rel_word))

# Function for returning and removing a random element from a list
def ran(listy):
	if len(listy) > 0:
		return listy.pop(random.randrange(len(listy)))

# Function for de-punctuating a list. (used mostly for cleaning bigrams)
def depunc(listy):
	listy = [''.join(c for c in s if c not in string.punctuation) for s in listy]
	listy = [s for s in listy if s]
	return listy