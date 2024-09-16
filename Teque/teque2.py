import collections
"""
Still not fast enough
"""
def main():  
    deq1= collections.deque()
    
    for _ in range(int(input())):
        command, number = input().split()
        number= int(number)

        if command== "push_back":
            deq1.append(number)
                    
        elif command== "push_front":
            deq1.appendleft(number)

        elif command== "push_middle":
            median = (len(deq1) + 1) // 2
            temp_list = list(deq1)
          #glue 2 lists together split at median - when median, append to list1 (below the median) and glue list1 and list2 together
            list1 = temp_list[:median]
            list2 = temp_list[median:]
            list1.append(number)
            deq1 = collections.deque(list1+list2)
        
        elif command== "get":
            print(deq1[number])

if __name__ == "__main__":
    main()
