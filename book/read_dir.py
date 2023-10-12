import os
from read_book import read_book
from word_statistics import word_statistics, count_words

book_dir = "./Books_EngFr"

for i in os.listdir("./Books_EngFr"):
    for j in os.listdir("./Books_EngFr/"+i):
        for k in os.listdir("./Books_EngFr/"+i+"/"+j):
            text = read_book("./Books_EngFr/"+i+"/"+j+"/"+k)
            print(word_statistics(count_words(text)))