import numpy as np
import re

class Word:

    @classmethod
    def find(cls, file):
        a = np.array([["elo", 1]])
        new_word = True
        f = open(file, 'r')
        word1 = ""

        for line in f.readlines():
            for word in line.split():
                word = word.lower()
                new_word=True
                word1 = "".join(re.findall("[a-zA-Z]+", word))
                word=word1
                for i in range(1, a.shape[0]):
                    if word == a [i, 0]:
                        x = int(a[i, 1])
                        x += 1
                        a[i, 1] = str(x)
                        new_word=False
                if new_word:
                    a = np.append(a, [[word, '1']], axis=0)
        f.close()
        return a

    @classmethod
    def find_most_used_word(cls, file, amount_of_words=1):
        a = cls.find(file)
        max = []
        max_index = []
        tab = []
        for i in range(0, amount_of_words):
            max.append(0)
            max_index.append(0)
            tab.append(0)
        for i in range(1, a.shape[0]):
            for j in range(0, amount_of_words):
                x = int(a[i, 1])
                if x>max[j]:
                    max_index[j]=i
                    max[j] = x
                    tab[j]=a[i, 0]
                    break
        return tab
if __name__ == '__main__':
    W = Word()
    t = W.find('file.txt')
    print(t)