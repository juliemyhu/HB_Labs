import sys

def count_words():

	count_file = open(sys.argv[1])
	word_counts = {}

	for line in count_file:
		line = line.rstrip()
		words = line.split()

		for word in words:
			word_counts[word]=word_counts.get(word,0) +1 

	for word,value in word_counts.items():
		print (word, value)

count_words()
