

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


# Czy dzien i miesiac sa poprawne

def czy_pesel_jest_poprawny(pesel):
    if len (pesel) > 11:
        print("pesel jest za dlugi")
    elif len(pesel) < 11:
            print ("pesel jest za krotki")
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

def czy_rok_jest_poprawny(pesel) :
    rok = int(pesel[0:2])
    miesiac = int(pesel[2:4])
    dzien = int(pesel [4:6])
    if int(rok) <=99 :
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
def czy_miesiac_jest_poprawny(pesel) :
    rok = int(pesel[0:2])
    miesiac = int(pesel[2:4])
    dzien = int(pesel [4:6])
    if int(miesiac) <=12 :
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

 #Tu sprawdzamy poprawność dnia

def czy_dzien_jest_poprawny(pesel) :
    rok = int(pesel[0:2])
    miesiac = int(pesel[2:4])
    dzien = int(pesel [4:6])
    if int(dzien) <=31 :
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



