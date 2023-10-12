

def count_words(text):
    text = text.replace(".", "").replace("!", "")\
        .replace(",", "").replace("?", "")
    text = text.split()
    words = {}
    for i in text:
        try:
            words[i] = words.get(i) + 1
        except:
            words[i] = 1

    return words


if __name__ == "__main__":
    text = "This is my test text. " \
           "We're keeping this text short to keep things manageable."
    print(count_words(text))
