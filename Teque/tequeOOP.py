import collections

class TripleEndedQueue:
    def __init__(self):
        self.front = collections.deque()
        self.middle = []
        self.back = collections.deque()
    
    def push_front(self, item):
        self.front.append(item)
    
    def push_back(self, item):
        self.back.append(item)
    
    def push_middle(self, item):
        # If middle is empty, decide where to put the item
        if not self.middle:
            if len(self.front) <= len(self.back):
                self.front.append(item)
            else:
                self.back.appendleft(item)
        else:
            # Insert into the middle list
            self.middle.append(item)
    
    def get(self, index):
        # Determine whether to look from front, middle, or back
        total_length = len(self.front) + len(self.middle) + len(self.back)
        if index < len(self.front):
            return self.front[index]
        elif index < len(self.front) + len(self.middle):
            return self.middle[index - len(self.front)]
        else:
            return self.back[index - len(self.front) - len(self.middle)]

def main():  
    teque= TripleEndedQueue()
    
    for _ in range(int(input())):
        command, number = input().split()
        number= int(number)

        if command== "push_back":
            teque.push_back(number)
                    
        elif command== "push_front":
            teque.push_front(number)
               
        elif command== "push_middle":
            teque.push_middle(number)
                    
        elif command== "get":
            print(teque.get(number))

if __name__ == "__main__":
    main()
