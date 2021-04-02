# Practical 1- Nguyen Quoc Minh Quan


def is_multiple(n, m):
    # enter your algorithm here
    if n % m == 0:
        return True
    else:
        return False


def main():
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))

    if is_multiple(a, b):
        print(a, "is a multiple of", b)
    else:
        print(a, "is NOT a multiple of", b)


if __name__ == "__main__":
    main()
