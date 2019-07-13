def delete_nth(order,max_e):
    # build count dict
    d = dict()
    for item in order:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    print("count dict:", d)
    cp = list(order)
    print("list copy:", cp)
    for item in d:
        print("\n========================")
        print("looking at :: ", str(item) + ": " + str(d[item]))
        while d[item] > max_e:
            print(str(d[item])+": => need to remove", d[item]-max_e)
            for idx, num in enumerate(cp[::-1]):
                if num == item:
                    print("removing:", num, "at", len(cp)-1-idx)
                    cp.pop(len(cp)-1-idx)
                    break
            d[item] -= 1
    return cp

def test():
    tests = [([20,37,20,21], 1), ([1,1,3,3,7,2,2,2,2], 3)]
    for test in tests:
        print(">>> Initiating Test <<<")
        print("\n ------> answer:", delete_nth(test[0], test[1]))

def main():
    test()

if __name__ == "__main__":
    main()