

def read_book(title_path):
    with open(title_path, "r", encoding="utf-8") as f:
        content = f.read()
    return content.replace("\n", "").replace("\r", "")


if __name__ == "__main__":
    text = read_book("./Books_EngFr/English/shakespeare/Romeo and Juliet.txt")
    print(len(text))
    ind = text.find("What's in a name?")
    print(ind)
    sample_text = "".join(list(text)[ind:ind+1000])
    print(sample_text)
