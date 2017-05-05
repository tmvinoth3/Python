#code
from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt') as story:
    words = []
    for line in story:
        line_words = line.decode("utf-8").split()
        for word in line_words:
            words.append(word)
for word in words:
    print(word)