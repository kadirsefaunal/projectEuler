def main():
    dosya = open("Problem 18.txt")
    satirlar = dosya.readlines()
    sayilar = []
    toplam = 0
    indis = 0
    for value in satirlar:
        satir = value.split()
        satirSayisi = len(satir) + 1

        for sayi in satir:
            sayilar.append(int(sayi))

        grupMax = sayilar[indis]
        if len(sayilar) > 1:
            if sayilar[indis + 1] > grupMax:
                grupMax = sayilar[indis + 1]
                indis = indis + 1

        toplam += grupMax
        sayilar = []

    print(toplam)


if __name__ == '__main__':
    main()
