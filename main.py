import mysql.connector
import os

clear = lambda: os.system('cls')

try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="")
except:
    print("Can't connect with database. Please check if the db is running.")
    print(mydb)

query = mydb.cursor()

query.execute("SHOW tables FROM slowka")
wybor_kategorii = []
wybor_kategorii_z_numerem = []
licznik = 0
for x in query:
    licznik += 1
    for y in x:
        wybor_kategorii.append(y)
        wybor_kategorii_z_numerem.append(str(licznik) + "." + y)


for i in wybor_kategorii_z_numerem:
    print(i)

wybrana_kategoria = input("Wybierz numer kategorii:\n")

query2 = mydb.cursor()
query2.execute("USE slowka")
query3 = mydb.cursor()
query3.execute("SELECT * FROM " + str(wybor_kategorii[int(wybrana_kategoria) - 1]))

licznik_bledow = 0
lista_slowek = []
for i in query3:
    linijki = list(i)
    lista_slowek.append(linijki)

slowka_do_przetlumaczenia = len(lista_slowek)

slowka_do_poprawy = []
odpowiedzi_do_slowek_do_poprawy = []
for i in lista_slowek:
    clear()
    print("Pozostało " + str(slowka_do_przetlumaczenia) + " do przetłumaczenia")
    odpowiedz = input("Przetłumacz: " + i[2] + "\n")
    if odpowiedz == i[1]:
        print("Dobrze")
        slowka_do_przetlumaczenia -= 1

    else:
        licznik_bledow += 1
        input("Poprawna odpowiedz to: " + i[1])
        slowka_do_poprawy.append(i[2])
        odpowiedzi_do_slowek_do_poprawy.append(i[1])


wdol = 0
while True:
    licznik_bledow -= wdol
    q = 0
    blad = 0
    wdol = 0
    print(licznik_bledow)

    if licznik_bledow == 0:
        print("Koniec")
        break
    while (q < licznik_bledow):
        clear()
        print("Pozostało " + str(slowka_do_przetlumaczenia) + " do przetłumaczenia")
        odpowiedz = input("Przetłumacz: " + slowka_do_poprawy[q] + "\n")

        if odpowiedz == odpowiedzi_do_slowek_do_poprawy[q]:
            print("Dobrze ")
            wdol += 1
            slowka_do_przetlumaczenia -= 1

        else:
            odpowiedzi_do_slowek_do_poprawy[blad] = odpowiedzi_do_slowek_do_poprawy[q]
            input("Poprawna odpowiedz to: " + odpowiedzi_do_slowek_do_poprawy[q])
            slowka_do_poprawy[blad] = slowka_do_poprawy[q]
            blad += 1
        q += 1
