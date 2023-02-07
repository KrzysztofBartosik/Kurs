'''def czy_poprawny_pesel(pesel):
    rok = pesel[0:2]
    miesiac = pesel [2:4]
    dzien = pesel [4:6]
    print(rok, miesiac, dzien)

czy_poprawny_pesel("89050654659")
czy_poprawny_pesel("89054254659")
czy_poprawny_pesel("Batman")

pesel_uzytkownika = input("Podaj numer pesel: ")
czy_poprawny_pesel(pesel_uzytkownika)'''


def czy_poprawny_pesel(pesel):
    if len(pesel) > 11:
        print(f"pesel {pesel} jest za dlugi ({len(pesel)})")
    elif len(pesel) < 11:
        print("pesel jest za krotki")
    else:
        print("pesel jest ok")


testowy_pesel = "321"
czy_poprawny_pesel(testowy_pesel)
testowy_pesel = "12345678911"
czy_poprawny_pesel(testowy_pesel)
testowy_pesel = "4444432324523525235"
czy_poprawny_pesel(testowy_pesel)


def czy_pesel_jest_poprawny(pesel):
    if len(pesel) > 11:
        print("pesel jest za dlugi")
    elif len(pesel) < 11:
        print("pesel jest za krotki")
    else:
        print("pesel jest ok")


test_dlugosc_peselu = "9205167898"
czy_pesel_jest_poprawny(test_dlugosc_peselu)
test_dlugosc_peselu = "89072416574"
czy_pesel_jest_poprawny(test_dlugosc_peselu)
test_dlugosc_peselu = "890919876543210"
czy_pesel_jest_poprawny(test_dlugosc_peselu)
test_dlugosc_peselu = "89251367890"
czy_pesel_jest_poprawny(test_dlugosc_peselu)
test_dlugosc_peselu = "89077666992"
czy_pesel_jest_poprawny(test_dlugosc_peselu)


# Tu sprawdzamy poprawność roku

def czy_rok_jest_poprawny(pesel):
    rok = int(pesel[0:2])
    if (rok) <= 99:
        print("rok jest poprawny")
    else:
        print("rok jest niepoprawny")


test_roku_pesel = "9205167898"
czy_rok_jest_poprawny(test_roku_pesel)
test_roku_pesel = "1005157656"
czy_rok_jest_poprawny(test_roku_pesel)
test_roku_pesel = "7805167898"
czy_rok_jest_poprawny(test_roku_pesel)
test_roku_pesel = "1305157656"
czy_rok_jest_poprawny(test_roku_pesel)


# Tu sprawdzamy poprawność miesiąca
def czy_miesiac_jest_poprawny(pesel):
    miesiac = int(pesel[2:4])
    if (miesiac) <= 12:
        print("miesiac jest poprawny")

    else:
        print("miesiac jest niepoprawny")


test_miesiaca_pesel = "9205167898"
czy_miesiac_jest_poprawny(test_miesiaca_pesel)
test_miesiaca_pesel = "1005157656"
czy_miesiac_jest_poprawny(test_miesiaca_pesel)
test_miesiaca_pesel = "9213167898"
czy_miesiac_jest_poprawny(test_miesiaca_pesel)
test_miesiaca_pesel = "2512157656"
czy_miesiac_jest_poprawny(test_miesiaca_pesel)
test_miesiaca_pesel = "9225167898"
czy_miesiac_jest_poprawny(test_miesiaca_pesel)
test_miesiaca_pesel = "9889157656"
czy_miesiac_jest_poprawny(test_miesiaca_pesel)


# Tu sprawdzamy poprawność dnia

def czy_dzien_jest_poprawny(pesel):
    dzien = int(pesel[4:6])
    if (dzien) <= 31:
        print("dzien jest poprawny")
    else:
        print("dzien jest niepoprawny")


test_dnia_pesel = "92041898765"
czy_dzien_jest_poprawny(test_dnia_pesel)
test_dnia_pesel = "02073398765"
czy_dzien_jest_poprawny(test_dnia_pesel)
test_dnia_pesel = "39043198765"
czy_dzien_jest_poprawny(test_dnia_pesel)
test_dnia_pesel = "87043098765"
czy_dzien_jest_poprawny(test_dnia_pesel)
test_dnia_pesel = "78043198765"
czy_dzien_jest_poprawny(test_dnia_pesel)
test_dnia_pesel = "78049998765"
czy_dzien_jest_poprawny(test_dnia_pesel)


def czy_pesel_zmian_jest_poprawny(pesel):
    czy_rok_jest_poprawny(pesel)
    czy_miesiac_jest_poprawny(pesel)
    czy_dzien_jest_poprawny(pesel)


print("===")
czy_pesel_zmian_jest_poprawny(test_dnia_pesel)


### Tutaj dodatkowo chciałem sprawdzić miesiące z dniami w miesiącu 29, 30, 31
def czy_miesiac_z_dniami_jest_poprawny(pesel):
    rok = int(pesel[0:2])
    miesiac = int(pesel[2:4])
    dzien = int(pesel [4:6])
    if(miesiac)in [1,3,5,7,8,10,12] and int(dzien)<=31:
        print("miesiac jest poprawny")
    elif(miesiac) in [4,6,9,11] and int(dzien)<=30:
        print("miesiac jest poprawny")
    elif(miesiac) in[2] and int(dzien)<=29:
        print("miesiac jest poprawny")

    else:
        print("miesiac jest niepoprawny")

test_miesiaca_z_dniem ="97033209876" # Sprawdzamy 32 marzec
czy_miesiac_z_dniami_jest_poprawny(test_miesiaca_z_dniem)
test_miesiaca_z_dniem ="97043109876" # Sprawdzamy 31 kwiecien
czy_miesiac_z_dniami_jest_poprawny(test_miesiaca_z_dniem)
test_miesiaca_z_dniem ="97023009876" # Sprawdzamy 30 luty
czy_miesiac_z_dniami_jest_poprawny(test_miesiaca_z_dniem)
test_miesiaca_z_dniem ="97022909876" # Sprawdzamy 29 luty
czy_miesiac_z_dniami_jest_poprawny(test_miesiaca_z_dniem)
test_miesiaca_z_dniem ="97033109876" # Sprawdzamy 31 marzec
czy_miesiac_z_dniami_jest_poprawny(test_miesiaca_z_dniem)
test_miesiaca_z_dniem ="97043009876" # Sprawdzamy 30 kwietnia
czy_miesiac_z_dniami_jest_poprawny(test_miesiaca_z_dniem)
