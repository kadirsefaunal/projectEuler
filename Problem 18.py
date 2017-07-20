def main():
    dosya = open("Problem 18.txt")
    satirlar = dosya.readlines()
    sayilar = []
    grup = []
    toplam = 0
    for value in satirlar:
        satir = value.split()
        satirSayisi = len(satir) + 1

        for sayi in satir:
            sayilar.append(int(sayi))

        indis = satir.index(str(max(sayilar)))
        grup.append(sayilar[indis])
        if (indis - 1 >= 0):
            grup.append(sayilar[indis - 1])
        if (indis + 1 < satirSayisi):
            grup.append(sayilar[indis + 1])

        toplam += max(grup)
        sayilar = []
        grup = []

        print(max(sayilar), satir.index(str(max(sayilar))), satirSayisi)

    print(toplam)




if __name__ == '__main__':
    main()
