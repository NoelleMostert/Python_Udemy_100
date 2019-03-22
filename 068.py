d = dict(weather = "clima", earth = "terra", rain = "chuva")

def vocab(word):
    return d[word]

word = input("Enter word: ").casefold()

try:
    vocab(word)
    print(vocab(word))
except:
    print("%s is not in the dictionary" % word)