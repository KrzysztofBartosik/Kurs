import random
import string


def generator_hasla(silne_haslo):
    znaki = list(string.ascii_letters + string.digits + string.punctuation)
    haslo = ""
    for i in range(len(silne_haslo)):
        haslo += random.choice(znaki)
    return haslo



