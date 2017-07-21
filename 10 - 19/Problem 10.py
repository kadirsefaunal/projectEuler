def main():
    toplam = 0

    for value in range(2, 2000000):
        if asalMi(value):
            toplam += value

    print(toplam)


def asalMi(sayi):
    hedef = sayi ** 0.5

    for value in range(2, round(hedef) + 1):
        if sayi % value == 0:
            return False

    return True


if __name__ == "__main__":
    main()
