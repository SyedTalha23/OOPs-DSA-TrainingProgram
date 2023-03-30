''' Mary is a kindergarten teacher . She has given a task to the children after teaching them a list of words. The task is to
find the unknown words (other than the words they already know) from the given text. Write a python function which accepts
the text and the known list of words and returns the set of unknown words found.

Return -1 if there are no unknown words.
Estimated Time - 20 minutes

Sample Input
Text: "the sun rises in the east"
Vocabulary:["sun","in","east","doctor","day"]
Expected Output
{'rises','the'}
'''
def find_unknown_words(text, vocabulary):
    unknown_words=[]
    words = text.split()
    for i in words:
        if i not in vocabulary:
            unknown_words.append(i)
    if len(unknown_words)==0:
        return -1

    return set(unknown_words)
text = "the sun rises in the east"
vocabulary = ["sun", "in", "east", "doctor", "day"]
print(find_unknown_words(text, vocabulary))