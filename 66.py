d = dict(weather = "clima", earth = "terra", rain = "chuva")

def vocab(word):
    return d[word]

word = input("Enter word: ")
print(vocab(word))