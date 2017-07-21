import math

def main():
    liste = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    taban = 2520

    print(taban)

    for value in liste:
        if taban % value != 0:
            if asalMi(value):
                taban *= value
            else:
                asalBolenleri = asalBul(value)
                for i in asalBolenleri:
                    taban *= i
                    if taban % value == 0:
                        break

    print(taban)


def asalBul(deger):
    asalBolenler = []
    h = (deger ** 0.5) / 2
    for value in range(2, round(deger)):
        if deger % value == 0:
            if asalMi(value):
                asalBolenler += [value]

    return asalBolenler

def asalMi(sayi):
    hedef = sayi / 2
    durum = True
    for j in range(2, round(hedef)):
        durum = True
        if sayi % j == 0:
            durum = False
            break

    return durum

if __name__ == "__main__":
    main()
