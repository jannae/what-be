import random

class Question(object):

	def __init__(self, tagged_corpus):
		self.cache = {}
		self.tagged = tagged_corpus
		self.words = self.get_words
		self.word_size = len(self.words)
		self.database()


	def get_words(self):
		words = []
		for (word, tag) in words_tagged:
			words.append(word.lower())
		return list(set(words))


	def tgrams(self):
		if len(self.words) < 3:
			return
		for i in range(len(self.words) - 2):
			yield (self.words[i], self.words[i+1], self.words[i+2])

	def database(self):
		for w1, w2, w3 in self.tgrams():
			key = (w1, w2)
			if key in self.cache:
				self.cache[key].append(w3)
			else:
				self.cache[key] = [w3]

	def ask(self):
		begin = 


		bgrams = []
		tag = ran(depunc(nextags(tagged,rel_word)))
		if tag is not None:
			print 'tagpre: '+tag[0]
			for ((w1, t1), (w2, t2)) in nltk.bigrams(tagged):
				if w1 == rel_word and t2.startswith(tag[0]):
					bgrams.append(w2.lower())
			if len(bgrams) == 0:
				bgrams.append(ran(get_words(tagged,tag[0])))
			print len(bgrams)
		else:
			bgrams.append(ran(get_words(tagged,'N')))
		return list(set(bgrams))


	def generate_markov_text(self, size=25):
		seed = random.randint(0, self.word_size-3)
		seed_word, next_word = self.words[seed], self.words[seed+1]
		w1, w2 = seed_word, next_word
		gen_words = []
		for i in xrange(size):
			gen_words.append(w1)
			w1, w2 = w2, random.choice(self.cache[(w1, w2)])
		gen_words.append(w2)
		return ' '.join(gen_words)