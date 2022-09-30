#/usr/bin/env python3


def main():
    while True:
        n = int(input())
        if n !=0:
            l1 = list()
            l2 = list()
            l3 = list()
            l4 = [None] * n

            # create two lists for all the numbers we will be receiving
            for i in range(n):
                l1.append(int(input()))
            
            for i in range(n):
                l3.append(int(input()))
            
            # make list2 a copy of list 1
            for i in l1:
                l2.append(i)
            

            #sorted list2  (the copy of list1) and list3. 
            l2 = sorted(l2)
            l3 = sorted(l3)

            # Remember that list 2 and list 3 are sorted
                # access the copy of list1 (list2) at i (remembering that it is sorted),
                #  get the index of the value using the original list (l1), and use this index in order to put it into l4
                # l3[i] will represent each value in the second half of our sorted list
            for i in range(len(l2)):
                l4[l1.index(l2[i])] = l3[i]

            for i in l4:
                print(i)
        else:
            break
if __name__ == "__main__":
    main()