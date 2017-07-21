import math

def main():
    sayi = 600851475143
    asalMi(sayi)

def asalMi(deger):
    hedef = (deger ** 0.5) / 2
    print(round(hedef))
    for value in range(2, round(hedef)):
        durum = True
        for i in range(2, value):
            if (value % i == 0):
                durum = False

        if durum and (deger % value == 0):
            deger /= value
            print(value, round(deger), sep = "\t")

        if round(deger) == 1:
            break


if __name__ == "__main__":
    main()
