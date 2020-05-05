import sys

def count_words():

	count_file = open(sys.argv[1])
	word_counts = {}

	for line in count_file:

		line = line.strip()
		
		words = line.split()

		for word in words:
			word = word.strip(",.!?$%")
			word = word.lower()
			word_counts[word]=word_counts.get(word,0) +1 


	for word,value in word_counts.items():
		print (word, value)

count_words()
