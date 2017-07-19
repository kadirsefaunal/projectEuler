import math

def main():
    asallar = []
    k = 2
    while len(asallar) < 10001:
        if asalMi(k):
            asallar += [k]
        k += 1

    print(asallar[10000])

def asalMi(sayi):
    hedef = sayi ** 0.5

    for value in range(2, round(hedef) + 1):
        if sayi % value == 0:
            return False

    return True

if __name__ == "__main__":
    main()
