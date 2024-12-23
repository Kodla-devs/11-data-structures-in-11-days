harf = "a"
print(harf)

tek_tirnak = 'a'
cift_tirnak = "a"

coklu_satir = """birden fazla satirdan 
olusan bir string"""
print(coklu_satir)

erisim = "bu bir stringdir"
print(erisim[0])
print(erisim[-2])
print(erisim[3:6])

s = "bu ikinci string"

s1 = 'B' + s[1:]
print(s1)

# del s
# print(s)

s2 = "ucuncu"

s3 = s1.replace("ikinci", s2)
print(s3)

print(len(s3))

print(s3.upper())
print(s3.lower())

bosluk = "     bosluk      "

print(bosluk)
print(bosluk.strip())

m1 = "merhaba"
m2 = "dünya"
m3 = m1 + m2
print(m3)

print(m3 * 4)

isim = "alice"
print(f"isim: {isim}")

kodla = "kodla"

print("k" in kodla)
print("s" in kodla)