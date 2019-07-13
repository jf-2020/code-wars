def comp(array1, array2):
    # print("\nin comp()")
    remaining = list(array2)
    # print("remaining: " + str(remaining))
    squares = [num**2 for num in array1]
    # print("squares: " + str(squares))
    for num in squares:
        # print("\nlooking at: " + str(num))
        if (num in array2):
            # print(str(num) + " in " + str(array2))
            if (num in remaining):
                # print(str(num) + " in " + str(remaining))
                # print("\npopping...")
                remaining.pop(remaining.index(num))
    if len(remaining) == 0:
        return True
    else:
        return False

def test():
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    print("Calling comp(a1, a2)")
    print(comp(a1, a2))

def main():
    test()

if __name__ == "__main__":
    main()