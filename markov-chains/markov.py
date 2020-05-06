"""Generate Markov text from text files."""
from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text_file = open(file_path)

    text = text_file.read()

    text_file.close()

    return text #text is now a long file of words


# print(open_and_read_file(sys.argv[1]))


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {} # empty dictionary name

    words = text_string.split() # splits the giant text into list of strings called words


    # set a stopping point to our list 
    words.append(None)

    #list of words ['Would', 'you', 'could', 'you',... 'Sam', 'I', 'am?', None]
    # print (words)
    # print ("-" *10)

    # create a loop to iterate through words except last two
    for idx, word in enumerate(words[:-2]):

        key = (word, words[idx +1])
        value = words[idx +2]

        if key not in chains:
            chains[key] = []
            
        chains[key].append(value)
    # print (f'chains in dict form : {chains}')

    return chains



# make_chains(open_and_read_file(sys.argv))

def make_text(chains):
    """Return text from chains."""
    
    key= choice(list(chains.keys())) 
    words = [key[0],key[1]] 
    word = choice(chains[key])

    while word is not None:
        key = (key[1],word)
        words.append(word)
        word = choice(chains[key])

    print(type(words)) #list
    print(words)
    

    joined_words = " ".join(words)
    print(type(joined_words)) #str
    print(joined_words)
    # return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
