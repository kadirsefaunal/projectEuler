import math

def main():
    sonuc = 0

    for value in range(1, 10001):
        deger1 = BolenlerinToplami(value)
        deger2 = BolenlerinToplami(deger1)
        if (value != deger1) and (value == deger2):
            sonuc += value

    print(sonuc)

def BolenlerinToplami(sayi):
    toplam = 0
    for value in range(1, round(sayi / 2) + 1):
        if sayi % value == 0:
            toplam += value

    return toplam

if __name__ == '__main__':
    main()
