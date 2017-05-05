#code
import sys
from urllib.request import urlopen

def fetch_words(url):
    """
    Returns :
        A list of strings containig words from the
        document
    """
    with urlopen(url) as story:
     words = []
     for line in story:
        line_words = line.decode("utf-8").split()
        for word in line_words:
            words.append(word)
    return words

def print_items(items):
    for item in items:
        print(item)

def main():
    #url = sys.argv[1]
    words = fetch_words('http://sixty-north.com/c/t.txt')
    print_items(words)
    
if __name__ == '__main__':
    main()