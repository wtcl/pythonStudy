import pandas as pd
from read_dir import *

stats = pd.DataFrame(columns=("language", "author", "title", "length", "unique"))
title_num = 1
book_dir = "./"
for i in os.listdir("./Books_EngFr"):
    for j in os.listdir("./Books_EngFr/"+i):
        for k in os.listdir("./Books_EngFr/"+i+"/"+j):
            text = read_book("./Books_EngFr/"+i+"/"+j+"/"+k)
            (num_unique, counts) = word_statistics(count_words(text))
            stats.loc[title_num] = i, j, k, sum(counts), num_unique
            title_num += 1
print(stats)
stats.to_csv("stats1.csv", index=False)

stats = pd.DataFrame(columns=("language", "author", "title", "length", "unique"))
title_num = 1
book_dir = "./"
for i in os.listdir("./Books_EngFr"):
    for j in os.listdir("./Books_EngFr/"+i):
        for k in os.listdir("./Books_EngFr/"+i+"/"+j):
            text = read_book("./Books_EngFr/"+i+"/"+j+"/"+k)
            (num_unique, counts) = word_statistics(count_words(text))
            stats.loc[title_num] = i, j.capitalize(), k.replace(".txt", ""), sum(counts), num_unique
            title_num += 1
print(stats)
stats.to_csv("stats2.csv", index=False)

print(stats.head())
print(stats.tail())
print(stats["length"])
print(stats.length)
