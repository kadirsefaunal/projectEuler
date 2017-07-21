def main():
    us = 2 ** 1000
    sonuc = str(us)
    toplam = 0
    for value in sonuc:
        toplam += int(value)

    print(toplam)

if __name__ == "__main__":
    main()
