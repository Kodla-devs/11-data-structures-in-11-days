s = {"bu", "bir", "settir"}

list_to_set = set(["bu", "bir", "listeydi", "ama", "sete", "dönüştü"])

a = {"kodla", "kodla", "kodla", "kodla"}
print(a)

karisik = {"kodla", 1, 5.1, True}

fs = frozenset(["bu", "dondurulmuş", "bir", "settir"])
# fs.add("eklenemez")

veriler = {"a", "b", "c", "d"}

set1 = {"kodla", 1}

set1.add("suleyman")

sayilar = {1, 2, 3, 4}
harfler = {"a", "b", "c"}

sayilar_ve_harfler = sayilar.union(harfler)
print(sayilar_ve_harfler)

asal_rakamlar = {2, 3, 5, 7}
cift_rakamlar = {2, 4, 6, 8}
ortaklar = asal_rakamlar.intersection(cift_rakamlar)
print(ortaklar)

fark = cift_rakamlar.difference(asal_rakamlar)
print(fark)

fark.clear()
print(fark)

print(2 in asal_rakamlar)
print(4 not in asal_rakamlar)
print(asal_rakamlar == cift_rakamlar)
print(asal_rakamlar < cift_rakamlar)

for i in asal_rakamlar:
    print(i)
    