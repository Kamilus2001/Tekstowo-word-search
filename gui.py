from tkinter import *
from word_finder import Word
from get_text import Textowo
from threading import Thread


class Gui:
    def __init__(self, master):
        self.link = Label(text="LINK FROM TEKSTOWO: ")
        self.link_text = Entry()
        self.amount = Label(text="AMOUNT OF MOST USED WORDS: ")
        self.amount_text = Entry()
        self.file_name = Label(text="ENTER FILE NAME: ")
        self.file_name_text = Entry()
        self.most_used_words = Label()
        self.button = Button(text="FIND!")
        self.link.grid(row=0, column=0)
        self.link_text.grid(row=0, column=1)
        self.amount.grid(row=1, column=0)
        self.amount_text.grid(row=1, column=1)
        self.file_name.grid(row=2, column=0)
        self.file_name_text.grid(row=2, column=1)
        self.button.grid(row=3, columnspan=2)
        self.most_used_words.grid(row=0, column=2)
        self.button.bind("<Button-1>", self.find_top_words)

    def find_top_words(self, master):
        link = self.link_text.get()
        x = int(self.amount_text.get())
        file_name = self.file_name_text.get()
        Thread(target=self.find_top_words_2, args=(link, x, file_name)).start()
    def find_top_words_2(self, link, x, file_name):
        W = Word()
        T = Textowo(link)
        T.save_to_file(file_name)
        tab = W.find_most_used_word(file_name, x)
        text1 =" "
        for i in range(0, len(tab)):
            text1 += str(i+1)+"."+tab[i]
            text1 += ', '
        self.most_used_words.config(text=" "+text1)


if __name__ == '__main__':
    root = Tk()
    root.title("Text-owo")
    G = Gui(root)
    root.mainloop()
