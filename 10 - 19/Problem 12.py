import math

def main():
    bolenSayisi = 0
    i = 10000
    while bolenSayisi < 500:
        bolenSayisi = 0
        i += 1
        sayi = (i * (i + 1)) / 2
        print(sayi)
        for value in range(1, round(sayi / 2)):
            if i % value == 0:
                bolenSayisi += 1

    print(bolenSayisi)
    print(i)



if __name__ == "__main__":
    main()
