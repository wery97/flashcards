import mysql.connector
import os
import pyinputplus

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
query2 = mydb.cursor()
query2.execute("USE slowka")

number_of_words_in_category = []
for i in range(licznik):
    query2.execute("select count(*) from " + wybor_kategorii[i])
    for j in query2:
        number_of_words_in_category.append(j[0])

for i in range(licznik):
    print(wybor_kategorii_z_numerem[i] + " (words {})".format(number_of_words_in_category[i]))
wybrana_kategoria = pyinputplus.inputInt("Type in the number of category:\n")


query3 = mydb.cursor()

amount_choice = pyinputplus.inputInt("1. All words\n2. Last 40 words\n3. Specific amount of random words\nChoose one option:\n")
if amount_choice == 1:
    query3.execute("SELECT * FROM " + str(wybor_kategorii[int(wybrana_kategoria) - 1]))
elif amount_choice == 2:
    query3.execute("SELECT * FROM " + str(wybor_kategorii[int(wybrana_kategoria) - 1]) + " order by id desc limit 40")
else:
    amount_of_words_choice = pyinputplus.inputInt("Type in number of words to learn:\n")
    query3.execute("SELECT * FROM " + str(wybor_kategorii[int(wybrana_kategoria) - 1]) + " ORDER BY RAND() LIMIT " + str(amount_of_words_choice))

clear()

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
    print("Pozostało " + str(slowka_do_przetlumaczenia) + " do przetłumaczenia\n")
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
