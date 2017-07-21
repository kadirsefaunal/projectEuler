def main():
    faktoriyel = factorial(100)
    print(faktoriyel)
    toplam = 0
    for value in str(faktoriyel):
        toplam += int(value)

    print(toplam)

def factorial(n):
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        return res

if __name__ == '__main__':
    main()
