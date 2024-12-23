
tam_sayi = [0, 1, 2]
string_listesi = ["kodla", "suleyman"]
sayi_string = ["kodla", 1, 2]

veriler = (1, "kodla", 2)
veriler_listesi = list(veriler)
print(veriler_listesi)

sifir_tablosu = [0] * 5
print(sifir_tablosu)

liste = []

liste.append(10)
print(liste)

liste.insert(0, 5)
print(liste)

liste.extend([3, 10, 25])
print(liste)

liste[0] = 1
print(liste)

# liste.remove(1)
# print(liste)

# liste.pop(-1)
# print(liste)

# del liste[1]
# print(liste)

for item in liste:
    print(item)
