import random

zakres = range(0, 99999999999 + 1)

def czy_miesiac_z_dniami_jest_poprawny(pesel):
    rok = int(pesel[0:2])
    miesiac = int(pesel[2:4])
    dzien = int(pesel[4:6])
    if miesiac < 1 or miesiac > 12:
        return False
    if miesiac not in [1, 3, 5, 7, 8, 10, 12] and dzien >= 31:
        return False
        # print("miesiac jest poprawny")
    elif miesiac not in [4, 6, 9, 11] and dzien >= 30:
        return False
        # print("miesiac jest poprawny")
    elif miesiac not in [2] and dzien >= 29:
        return False
        # print("miesiac jest poprawny")

    else:
        return True
        # print("miesiac jest niepoprawny")


# pesel = range(0, 99999999999 + 1)
# miesiac = int(pesel[2:4])
# dzien = int(pesel[4:6])


def los_pesel(pesel_gen):
    return f'{str(random.choice(zakres)).rjust(11,"0")}'
warunek = False
numer = 0

while not warunek:
    nowy_pesel = los_pesel(zakres)
    numer += 1
    print(f'PESEL nr {numer } wylosowano: {nowy_pesel}')
    warunek = czy_miesiac_z_dniami_jest_poprawny(nowy_pesel)
# for numer in range(10):
#     print(f'PESEL nr {numer + 1} wylosowano: {los_pesel(pesel)}')