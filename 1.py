from pprint import pprint

myString = "This is the string whose words we would like to count. " \
           "This string contains some repeated words, as well as some " \
           "unique words."
for i in ".?!,":
    myString = myString.replace(i, "")
myString = myString.split()
word = {}
for w in myString:
    word[w] = word.get(w, 0)+1
pprint(word)