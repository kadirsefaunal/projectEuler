def main():
    dosya = open("Problem 13.txt")
    toplam = 0
    for value in dosya.readlines():
        sayi = int(value[:13])
        toplam += sayi

    sonuc = str(toplam)[:10]
    print(sonuc)


if __name__ == "__main__":
    main()
