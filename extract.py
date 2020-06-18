import collections
import pandas as pd
import matplotlib.pyplot as plt
file = open('commits_dataset.txt', encoding="utf-8-sig",errors='ignore')
a= file.read()

wordcount = {}
for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
fp = open('most_occuring_keywords.txt','a')
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    fp.write(word+"\n")
    print(word, ": ", count)
file.close()
fp.close()