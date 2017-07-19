import math

def main():
    asallar = []
    print(len(asallar))
    k = 2
    while len(asallar) < 10001:
        if asalMi(k):
            asallar += [k]
        k += 1

    print(asallar[10000])
    print(len(asallar))

def asalMi(sayi):
    if sayi == 2:
        return True
    hedef = sayi ** 0.5
    for j in range(2, round(hedef)):

        if sayi % j == 0:
            return False

    return True

if __name__ == "__main__":
    main()
