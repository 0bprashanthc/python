if __name__ == "__main__":
    s = "I live in a house"
    i = 0
    words = []
    while i <= len(s)-1:
        word = ""
        while s[i] != " ":
            word = word + s[i]
            if i != len(s)-1: i = i + 1
        words.append(word)
        print word
        if i != len(s)-1:i = i + 1
    print " ".join(words)
