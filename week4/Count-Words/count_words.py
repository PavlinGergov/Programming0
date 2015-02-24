def count_words(words):
    info = {}
    for word in words:
        if word in info:
            info[word] += 1
        else:
            info[word] = 1
    return info

print(count_words(["words", "are", "meaningful", "words", "words", "are"]))



            
