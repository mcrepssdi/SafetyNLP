# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download()
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

# Open text
textFile = open("words.txt")

# Reads the text file
text = textFile.read()
print(text)

sentences = sent_tokenize(text)
print("Sentences Found:", str(len(sentences)))
print(sentences)

words = word_tokenize(text)
print("Words Found:", str(len(words)))
print("All Words: ", words)

# remove punctuation marks
words_no_punc = []
for w in words:
    if w.isalpha():
        words_no_punc.append(w.lower())

print("Words Found:", str(len(words)))
print("All Words: ", words)

# remove punctuation marks
words_no_punc = []
for w in words:
    if w.isalpha():
        words_no_punc.append(w.lower())

print("Words WO Punctuation: ", words_no_punc)
print("Len Words WO Punctuation: ", len(words_no_punc))

# english stopwords
stopwords = stopwords.words("english")
print("Stop Words: ", stopwords)
print("Len Stop Words: ", len(stopwords))

# Create a clean list
clean_words = []
for w in words_no_punc:
    if w not in stopwords:
        clean_words.append(w)

print("Cleaned Words: ", clean_words)
print("Len Cleaned Words: ", len(clean_words))

print("Stop Words: ", stopwords)
print("Len Stop Words: ", len(stopwords))

# Create a clean list
clean_words = []
for w in words_no_punc:
    if w not in stopwords:
        clean_words.append(w)

print("Cleaned Words: ", clean_words)
print("Len Cleaned Words: ", len(clean_words))

# Create distribution on words
fdist = FreqDist(clean_words)
fdist.most_common(15)

# display the plot
fdist.plot(15)