import string
def janitor(word):
    alphabets = string.ascii_lowercase
    result = [0]*26
    for i in word:
        index = alphabets.find(i)
        if word.rfind(i) < 0:
            result[index] = 0
        else:
            result[index]=word.rfind(i) - word.find(i) + 1
    print(result)

if __name__ == '__main__':
    janitor('abacaba')