import math
from itertools import permutations

def gcd_gt_one(a, b):
    return math.gcd(a, b) > 1

def reorder_list(nums):
    for perm in permutations(nums):
        if all(gcd_gt_one(perm[i], perm[i + 1]) for i in range(len(perm) - 1)):
            return list(perm)
    return None


def main():
    _ = int(input())
    numbers = list(map(int, input().split()))

    result = reorder_list(numbers)
    if result:
        for i in result:
            print(i, sep=" ", end=" ")
    else:
        print("Neibb")

if __name__ == "__main__":
    main()
