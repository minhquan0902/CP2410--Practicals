# Practical 1- Nguyen Quoc Minh Quan

def main():
    # enter your algorithm here
    # the logic can be included in another method
    list1 = []
    # get number of elements inside a list
    n = int(input("Input the number of elements inside a list: "))
    for i in range(n):
        elements = int(input(">> "))
        list1.append(elements)

    print("Your current list: {}".format(list1))

    # Check for duplicates by using Set and comparing len of the Set and the List
    # in Python, all elements inside a Set must be unique
    if len(list1) == len(set(list1)):
        return print("All the numbers are different from each other")
    else:
        return print("All the numbers are NOT different from each other")



if __name__ == "__main__":
    main()
