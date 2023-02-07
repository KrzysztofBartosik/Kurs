from generator_pesel import generator_pesel
import pytest

# pesel = "99021623564"

@pytest.fixture()
def pesel_testowy():
    return generator_pesel()

# pesel = generator_pesel()
# print(pesel)


def test_dlugosc(pesel_testowy):
    assert len(pesel_testowy) == 11, "niepoprawna dlugosc"


def test_miesiac(pesel_testowy):
    miesiac = int(pesel_testowy[2:4])
    assert 12 >= miesiac > 0, "nie ma takiego miesiaca"
 

def test_dzien(pesel_testowy):
    dzien = int(pesel_testowy[4:6])
    assert 0 < dzien <= 31, "nie ma takiego dnia"
