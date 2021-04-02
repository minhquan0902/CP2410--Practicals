# Practical 1- Nguyen Quoc Minh Quan


def harmonic_gen(n):
    # enter your generator code here

    h = 0
    for i in range(1, n + 1):
        h += 1 / i
    yield h


def main():
    num = int(input("Enter a number: "))

    genObj1 = harmonic_gen(num)

    # complete the printing from generator object here
    for items in genObj1:
        print(items)


if __name__ == "__main__":
    main()


