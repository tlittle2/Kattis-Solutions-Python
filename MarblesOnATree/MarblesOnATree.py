#/usr/bin/env python3
#Trevor Little

class Node:
    def __init__(self, val, marbles, numOfChildren, children):
        self.children= children
        self.val= val
        self.numOfChildren= numOfChildren
        self.marbles= marbles
        self.childrenNodes = []
        self.parent= None
        self.need=0

    def add(self, child):
    #Checking for conditions present on tree
        self.childrenNodes.append(child)
        child.parent= self


    def postOrder(self):
        numOfMoves= 0
        for child in self.childrenNodes:
            numOfMoves+=child.postOrder()
        numOfMoves+=self.onePerNode()
        return numOfMoves
            
    def postPrint(self):
        for child in self.childrenNodes:
            child.postPrint()
        print(self.val,self.marbles)

    def howManyMarbles(self):
        need = 1-self.marbles
        for child in self.childrenNodes:
            need+= child.howManyMarbles()
        self.need= need
        return need
            
        

    
    def Sort(self):
        numOfMoves= 0
        for child in self.childrenNodes:
            numOfMoves+= child.Sort()
        if self.parent != None:
            self.parent.marbles-=self.need
            self.marbles+= self.need
            numOfMoves+= abs(self.need)
            self.need -= self.need

        return numOfMoves
       
            

while True:
    numOfNodes= int(input())
    if(numOfNodes ==0):
        break
    nodeArray= []
    globalNumOMoves=0
    for i in range(numOfNodes):
        theInput= list(map(int, (input().split())))
        n1= theInput[0]
        marbles= theInput[1]
        numOfChildren= theInput[2]
        children= theInput[3:]
        newNode= Node(n1, marbles, numOfChildren, children)
        nodeArray.append(newNode)

    for i in range(numOfNodes):
        for j in nodeArray[i].children:
            nodeArray[i].add(nodeArray[j-1])
    for k in nodeArray:
        if k.parent == None:
            root= k
            break
    root.howManyMarbles()
    #root.postPrint()
    globalNumOMoves+= root.Sort()
    print(globalNumOMoves)