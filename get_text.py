from bs4 import BeautifulSoup
import requests


class Textowo:

    def __init__(self, link):
        self.page = requests.get(link)
        self.soup = BeautifulSoup(self.page.content, 'lxml')

    def save_to_file(self, file):
        text_box = self.soup.find("div", {"class": "song-text"})
        f = open(file, "w")
        f.write(text_box.text)
        f.close()

if __name__ == '__main__':
    T = Textowo('https://www.tekstowo.pl/piosenka,lil_pump,gucci_gang.html')
    T.save_to_file("file1.txt")