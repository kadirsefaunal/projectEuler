import math

def main():
    enBuyuk = 0
    for i in range(999, 99, -1):
        durum = False
        for j in range(999, 99, -1):
            carpim = i * j
            if kontrol(carpim):
                if carpim > enBuyuk:
                    enBuyuk = carpim

    print(enBuyuk)

def kontrol(sayi):
    deger = str(sayi)
    k = 0
    l = len(deger) - 1
    while k < round(len(deger) / 2):
        durum = True
        if deger[k] != deger[l]:
            durum = False
            break
        k += 1
        l -= 1

    return durum;

if __name__ == "__main__":
    main()
