from random import randint
from PyDictionary import PyDictionary
from random import shuffle
class Hangman:
    word = "APPLE"
    shuffled_index = []
    f = open("animals.txt", "r")
    for i in f:
        animal = f[randint()]
        print(animal)
    # print(f.read())
    for i in range(len(word)):
        shuffled_index.append(i)
    shuffle(shuffled_index)
    print("<<<< UNSCRAMBLE THE LETTERS >>>>")
    for i in range(len(word)):
        index = shuffled_index[i]
        print(word[index], end=" ")

    def foo(self):
        global word
    for i in word:
        guess = input("\nspell your first guess:")
        if guess != word:
            print("**not correct try one more**")
            pass
            guess = input("spell your second guess:")
        if guess != word:
            print("**not correct try one more**")
            pass
            guess = input("spell your third guess:")
        if guess != word:
            print("!!!you are lose!!!")
            break
        else:
            print("!!!you are win!!!")
            break
a = Hangman()
a.foo()

#
#  from random_word import RandomWords
# >>> r = RandomWords
# >>> r = RandomWords()
# >>> r.get_random_word()
# 'morder'
# >>> r.get_random_word()
# from random import randint
# from random import shuffle
#
# txt = "apple"
# shuffled_index = []
# for i in range(len(txt)):
#     shuffled_index.append(i)
#
# shuffle(shuffled_index)
# print(shuffled_index)
#
# for i in range(len(txt)):
#     index = shuffled_index[i]
#     print(txt[index], end=" ")







# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p1 = person("john", 36)
# p2 = person("jack", 25)
# print(p1.name)
# print(p1.age)
# print(p2.name)
# print(p2.age)