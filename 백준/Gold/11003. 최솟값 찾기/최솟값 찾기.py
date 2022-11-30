import sys
import heapq

#n, l = 12,3 
n,l = map(int,sys.stdin.readline().split())
#arr =  [1,5, 2, 3, 6, 2, 3, 7, 3, 5, 2, 6]
arr = list(map(int,sys.stdin.readline().rstrip().split()))
answer =[]
heap = []
if(l == 1):
    print(*arr)
else:
    for i,num in enumerate(arr):
        if(i<l):
            heapq.heappush(heap,(num,i))
            answer.append(heap[0][0])
        else:
            while(heap[0][1]<i-l+1):
                heapq.heappop(heap)
            heapq.heappush(heap,(num,i))
            answer.append(heap[0][0])

    print(*answer)