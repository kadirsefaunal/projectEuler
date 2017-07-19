def main():
    n = 100
    toplamlarininKaresi = ((n * (n + 1)) / 2) ** 2
    karelerininToplami = (n * (n + 1) * (2 * n + 1)) / 6
    fark = toplamlarininKaresi - karelerininToplami

    print(fark)


if __name__ == "__main__":
    main()
