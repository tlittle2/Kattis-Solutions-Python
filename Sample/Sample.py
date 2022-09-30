#/usr/bin/env python3

import sys

def main():
	num = int(sys.stdin.readline())
	print(num)

numString = sys.stdin.readline()
nums= numString.split()
for i in range(len(nums)):
	print(nums[i])
	
numString= sys.stdin.readline()
nums= numString.split()
for i in range(len(nums)):
	print (nums[i], ' ', end = '')
	print()
	

if __name__ == "__main__":
    main()