from count_words import count_words
from read_book import read_book


def word_statistics(word_counts):
    words_num = len(word_counts.keys())
    return (words_num, word_counts.values())


if __name__ == "__main__":
    text = read_book("./Books_EngFr/English/shakespeare/Romeo and Juliet.txt")
    word_counts = count_words(text)
    (num_unique, counts) = word_statistics(word_counts)
    print(num_unique, sum(counts))
