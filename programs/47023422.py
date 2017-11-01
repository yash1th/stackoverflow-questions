import random
import time
import requests

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(word_site)
WORDS = response.content.decode('utf-8').splitlines()
a = random.choice(WORDS)

words = 0
points = 0
Counter = -1

class App(object):
    def welcome(self):
        print("""
        ===========================
        The Typing Test
        ===========================

        -words are chosen random from a dictionary
        -a wrong word is 0 points, a right word is 100 points
        -Depending on how many correct words you get in 60 secs, you get an amount of points
        -Depending on the percentage of right answers you will also get a bonus
        """)
        print()
        answer = input("Press enter to proceed - ").lower()
        if answer == "":
            self.words()
        else:
            self.words()

    def words(self):
        print (str(a) + str(words) + str(points))
        self.userinput()

    def userinput(self):
        answer = input("").lower()
        if answer == str(a).lower():
            points = points + 1
            self.words()
        else:
            self.words()


cl = App()
cl.welcome()