def main():
    a = 1
    b = 1
    x = 2
    while len(str(b)) < 1000:
        gecici = b
        b += a
        a = gecici

        x += 1
        print(x)





if __name__ == '__main__':
    main()
