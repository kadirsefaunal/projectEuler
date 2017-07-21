def main():
    durum = False
    for b in range(1, 1000):
        for a in range(1, b):
            if ((1000 * a) + (1000 * b) - (a * b)) == 500000:
                durum = True
                break

        if durum:
            break

    c = 1000 - a - b
    sonuc = a * b * c

    print(a, b, c)
    print(sonuc)


if __name__ == "__main__":
    main()
