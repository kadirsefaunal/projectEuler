s1 = 1
s2 = 2
toplam = 2

while s2 < 4000000:
    gecici = s2
    s2 += s1
    s1 = gecici
    if s2 % 2 == 0:
        toplam += s2

print(toplam)
