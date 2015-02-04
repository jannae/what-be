import nltk
import string

from random import randrange


def get_words(words_tagged, tag_prefix):
    """
    Function for returning a unique list of words from a certain part of
    speech (tag) from a tagged corpus of words
    """
    words = []
    for (word, tag) in words_tagged:
        if tag.startswith(tag_prefix):
            words.append(word.lower())
    return list(set(words))

def get_exact_words(words_tagged, exact_tag):
    """
    Function for returning a unique list of words from a certain part of
    speech (tag) from a tagged corpus of words
    """
    words = []
    for (word, tag) in words_tagged:
        if tag == exact_tag:
            words.append(word.lower())
    return list(set(words))

def tgram_by_tag(tagged, tag_pre1, sep):
    """
    Function for returning a trigram based on parts of speech tagged words
    from a tagged corpus of sentences
    """
    tgrams = []
    for (word1, tgram1), (word2, tgram2), (word3, tgram3) in nltk.trigrams(tagged):
        if tgram1.startswith(tag_pre1) and tgram2.startswith(sep):
            tgrams.append(word1.lower() +' '+ word2.lower() +' '+ word3.lower())
    return list(set(tgrams))


def bgram_by_tag(tagged, tag_pre1, tag_pre2):
    """
    Function for returning a trigram based on parts of speech tagged words
    from a tagged corpus of sentences
    """
    bgrams = []
    for (word1, tgram1), (word2, tgram2) in nltk.bigrams(tagged):
        if tgram1.startswith(tag_pre1) and tgram2.startswith(tag_pre2):
            bgrams.append(word1.lower() +' '+ word2.lower())
    return list(set(bgrams))


def bgram_by_word(words, rel_word):
    """
    Function for returning a bigram for a particular word from a tagged corpus
    of words
    """
    return list(set(word2.lower() for (word1, word2) in nltk.ibigrams(words) if word1 == rel_word))


def bgram_word_tag(tagged, rel_word, tag):
    """
    Function for returning a bigram for a particular word based on the most
    likely following tag
    """
    bgrams = []
    for ((word1, tgram1), (word2, tgram2)) in nltk.bigrams(tagged):
        if word1 == rel_word and tgram2.startswith(tag[0]):
            bgrams.append(word2.lower())
    if len(bgrams) == 0:
        bgrams.append(ran(get_words(tagged, tag[0])))
    return list(set(bgrams))


def chain_phrase(tagged, rel_word, size=3):
    """
    Function for returning a bigram for a particular word to follow a phrase
    based on the most likely following tag of the last word in the phrase
    """
    bgrams = []
    for i in xrange(size):
        tag = ran(depunc(nextags(tagged, rel_word)))
        if tag is not None:
            for ((word1, tgram1), (word2, tgram2)) in nltk.bigrams(tagged):
                if word1 == rel_word and tgram2.startswith(tag[0]):
                    rel_word = word2.lower()
            if len(rel_word) == 0:
                rel_word = ran(get_words(tagged, tag[0]))
        else:
            rel_word = ran(get_words(tagged, 'N'))
        bgrams.append(rel_word)
    return ' '.join(bgrams)

def phrase_by_tag(tagged, tag_pre1, tag_pre2):
    """
    Function for returning a list of trigram phrases based on a set of tags.
    """
    phrases = []
    for s in tagged:
        phrase = tgram_by_tag(s, tag_pre1, tag_pre2)
        if len(phrase) > 0:
            phrases.append(depunc(phrase))
    return phrases

def ran(listy):
    """
    Function for returning and removing a random element from a list
    """
    if len(listy) > 0:
        return listy.pop(randrange(len(listy)))

def depunc(listy):
    """
    Function for de-punctuating a list. (used mostly for cleaning bigrams)
    """
    listy = [''.join(c for c in s if c not in string.punctuation) for s in listy]
    listy = [s for s in listy if s]
    return listy

def nextags(tagged, word):
    """
    Add the tag of the next word to our list of tags.
    """
    tags = []
    for ((word1, tgram1), (word2, tgram2)) in nltk.ibigrams(tagged):
        if word1 == word:
            tags.append(tgram2)
    return list(set(tags))
