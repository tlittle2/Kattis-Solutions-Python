import sys, heapq
def main():
    minHeap= []
    maxHeap= []
    while(True):
        ip= sys.stdin.readline().strip()
        if ip== '':
            break            
        elif ip =='#':
            print((heapq.heappop(minHeap)))
        else:
            ip= int(ip)
            #add things
            if len(maxHeap) == 0 and len(minHeap) == 0:
                heapq.heappush(minHeap, ip)
            elif minHeap[0] > ip :
                heapq.heappush(maxHeap, -ip)
            elif  minHeap[0] < ip:
                heapq.heappush(minHeap, ip)
            elif minHeap [0] == ip:
                if len(minHeap) == len(maxHeap):
                    heapq.heappush(minHeap, ip)
                elif len(minHeap) > len(maxHeap):
                    heapq.heappush(maxHeap, -ip)
                elif len(minHeap) < len(maxHeap):
                    heapq.heappush(minHeap, ip)
            #print(minHeap, maxHeap)

        #fix things
        if len(maxHeap) == len(minHeap):
            continue

        elif len(minHeap) > len(maxHeap)+1:
            heapq.heappush(maxHeap, -(heapq.heappop(minHeap)))
        
        elif len(minHeap) < len(maxHeap):
            heapq.heappush(minHeap, -(heapq.heappop(maxHeap)))
        #print(minHeap, maxHeap)     
if __name__ == "__main__":
    main()
