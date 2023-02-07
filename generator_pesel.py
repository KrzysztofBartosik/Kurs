import random


def generator_pesel():
    tablica = []
    zakres = range(0, 9 + 1)
    for i in range(11):
        tablica.append(str(random.choice(zakres)))
    return "".join(tablica)