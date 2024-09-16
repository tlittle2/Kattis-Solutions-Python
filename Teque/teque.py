import collections
"""
Correct answers, but time limited exceeded
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
            deq1.insert(median,number)
        
        elif command== "get":
            print(deq1[number])

if __name__ == "__main__":
    main()
