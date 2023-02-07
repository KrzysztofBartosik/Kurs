import string

import pytest
from generator_hasla import generator_hasla

silne_haslo = range(8)
@pytest.fixture()
def haslo_testowe():
    return "abcdefg1"
    return generator_hasla(silne_haslo)


def test_dlugosci_hasla(haslo_testowe):
    assert len(haslo_testowe) == 8, "niepoprawna dlugosc"


def test_haslo_zawiera_tylko_litery(haslo_testowe):
    nonletter = False
    for litera in haslo_testowe:
        if litera not in string.ascii_letters:
            nonletter = True
    assert nonletter, "zawiera tylko litery"



def test_haslo_zawiera_tylko_cyfry(haslo_testowe):
    if haslo_testowe not in string.punctuation or string.ascii_letters:
        assert haslo_testowe == "zawiera tylko cyfry"


def test_haslo_zawiera_tylko_znaki_specjalne(haslo_testowe):
    if haslo_testowe not in string.ascii_letters or string.digits:
        assert haslo_testowe == "zawiera tylko znaki specjalne"
