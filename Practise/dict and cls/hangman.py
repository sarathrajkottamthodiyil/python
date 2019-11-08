from random import randint
from random import shuffle
class Hangman:
    animal = []
    word = ""
    shuffled_index = []
    f = open("animals.txt", "r")
    for ani in f:
        d = ani.strip()
        animal.append(d)
    random_index = randint(0, len(animal))
    word = animal[random_index]
    print(word)
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

            guess = input("spell your second guess:")
        if guess != word:
            print("**not correct try one more**")

            guess = input("spell your third guess:")
        if guess != word:
            print("!!!you are lose!!!")
            break
        else:
            print("!!!you are win!!!")
            break
    print("the correct word is:", word)
a = Hangman()
a.foo()
