print("Enter your input - k value to generate sets: ")
k = int(input())
def calcN(k):
    n = k*(k-1) + 1
    return n

import itertools
def generate(n):
    total_numbers = set(range(1, n+1))
    subsets = list(itertools.combinations(total_numbers, k))
    common = []
    common.append(subsets[0])

    def common_member(a, b):
        a_set = set(a)
        b_set = set(b)

        if(len(a_set.intersection(b_set)) == 1):
            return True
        else:
            return False


    for i in subsets:
        count = 0
        for j in common:

            if common_member(i, j):
                    count+=1
            if count == len(common):
                common.append(i)
            else:
                continue
    print("Number of Nodes:", n)
    print(common)

generate(calcN(k))
