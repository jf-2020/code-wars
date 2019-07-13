import random

def score(dice):
    #
    d = dict()
    for die in dice:
        if die in d:
            d[die] += 1
        else:
            d[die] = 1
            
    #
    ret, index = 0, 0
    remaining = list(die for die in dice)
    points = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}

    #
    for die, count in d.items():
        if count == 3:
            ret += points[die]
            for _ in range(3):
                del remaining[remaining.index(die)]

    #
    for die in remaining:
        if die == 1:
            ret += 100
        elif die == 5:
            ret += 50

    #
    return ret

def score1(dice):
    # sort the input
    dice = sorted(dice)
    d_copy = dice.copy()
    # init ret val, counter
    ret, index = 0, 0
    # loop over die
    for die in dice:
        # if pos = 0,1,2 (i.e. next 3 items exist & no IndexError)
        if index < 3 and die == dice[index+1] and die == dice[index+2]:
            # check if val == 1
            if die == 1:
                # then add 1000
                ret += 1000
                # remove the 1s
                for _ in range(3):
                    d_copy.remove(die)
                # bump up counter by 3
                index += 3
                # break outta loop
                break
            # otherwise, add 100 * val
            else:
                ret += die * 100
                # bump up counter by 3
                index += 3
                # break outta loop
                break
        # bump up the counter by 1
        index += 1
    # then just consider remaining vals == 1 or == 5
    for die in d_copy:
        if die == 1:
            ret += 100
        elif die == 5:
            ret += 50
    return ret
  

def main():
    # # answer1 = 0
    # test1 = [2, 3, 4, 6, 2]
    # # answer2 = 400
    # test2 =  [4, 4, 4, 3, 3]
    # # answer3 = 450
    # test3 = [2, 4, 4, 5, 4]

    # tests = [test1, test2, test3]

    # for test in tests:
    #     print(score(test))

    for _ in range(30):
        l = [random.randrange(1,6) for _ in range(5)]
        print(l, score(l), "\n")

if __name__ == "__main__":
    main()