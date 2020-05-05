import sys

def word_count(file_name):

	count_file = open(file_name)
	word_counts = {}

	for line in count_file:

		line = line.strip()

		words = line.split()

		for word in words:
			word = word.strip(",.!?$%")
			word = word.lower()
			word_counts[word]=word_counts.get(word,0) +1 

	# print(word_dict.keys(), type(word_dict.keys()))

	for word,value in word_counts.items():
		print (word, value)

word_count(sys.argv[1])




