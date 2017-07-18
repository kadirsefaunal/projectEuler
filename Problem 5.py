def main():
    asallar = [11, 13, 17, 19]
    asalOlmayanlar = [12, 14, 15, 16, 18, 20]
    taban = 2520

    #for value in asallar:
    #    taban *= value

    print(taban)

    for value in asallar:
        if (taban % value != 0):
            taban *= value

    for value in asalOlmayanlar:
        #kendisinden küçük asal çarpanlarla çarp

    print(taban)

if __name__ == "__main__":
    main()
