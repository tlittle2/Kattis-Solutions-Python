#/usr/bin/env python3

import sys 


def makeMask(nums):
	gMx = max(nums)
	gMn = min(nums)

	eMn = min(nums[0], nums[-1])

	# Build island mask
	mask = [0 if (x <= gMn) else 1 for x in nums]
	return mask


def makeSplits(mask, nums):
	# build a list of tuples from the mask and numList
	ss = []
	ff = []
	i = False; # Are we on the island?
	for k in range(len(mask)):
		if ((i == False) and (mask[k] == 1)):
			i = True
			ss.append(k)
		if (mask[k] == 0 and i == True):
			i = False
			ff.append(k)
		if (i == True and k == (len(mask) - 1)):
			ff.append(k+1)

	#print('ss:',ss,'ff:',ff)
	splits = [nums[i:j] for i, j in zip(ss, ff)]
	return splits


island_count = 0;
def skipper(inputList):
	global island_count

	# Count each island
	splits = makeSplits(makeMask(inputList),inputList)
	island_count += len(splits)

	for s in splits:
		#print(s)
		skipper(s)

	return True


def surf(streamCase):
	global island_count

	caseLine = [int(x) for x in streamCase.strip().split(' ')]
	case = caseLine[0]
	## Crack the islands
	island_count = 0

	#print(caseLine[1:])
	skipper(caseLine[1:])
	print(case,island_count)


def main():
	## testList = [int(x) for x in [*"0 1 2 4 3 1 3 4 5 2 1 0".split(" ")]]

	cases = int(sys.stdin.readline().strip())

	for i in range(cases):
		ocean = sys.stdin.readline()
		surf(ocean)

	## print(testList)
	## skipper(testList)

if __name__ == "__main__":
    main()