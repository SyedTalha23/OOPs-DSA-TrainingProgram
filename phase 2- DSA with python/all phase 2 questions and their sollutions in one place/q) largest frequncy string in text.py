"""
Write a python program that accepts a text and displays a 
string which contains the word with the largest frequency
 in the text and the 
frequency itself separated by a space.
Rules:
The word should have the largest frequency.
In case multiple words have the same frequency, then choose 
the word that has the maximum length.
Assumptions:
The text has no special characters other than space.
The text would begin with a word and there will be only a 
single space between the words.
Perform case insensitive string comparisons wherever 
necessary.
"""
def largest_frequency(text):
    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    max_frequency = 0
    max_word = ""
    for word in word_count:
        if word_count[word] > max_frequency:
            max_frequency = word_count[word]
            max_word = word
        elif word_count[word] == max_frequency and len(word) > len(max_word):
            max_word = word
    return([max_word, max_frequency])



txt="The quick brown fox jumped over the lazy dog. The dog was not happy with this and started barking loudly. The fox continued to run, ignoring the dog's barks. Finally, the fox reached its den and disappeared inside"
print(largest_frequency(txt))