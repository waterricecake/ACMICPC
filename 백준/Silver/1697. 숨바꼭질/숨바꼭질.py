import sys
import heapq
n, k = map(int,sys.stdin.readline().rstrip().split())

q = []
visited = [False for _ in range(1000000)]
heapq.heappush(q,(0,n))
x = -1
while x != k:
    time,x =heapq.heappop(q)
    if 0<=x+1<100001 and not visited[x+1]:
        visited[x+1] = True
        heapq.heappush(q,(time+1,x+1))
    if 0<=x-1 and not visited[x-1]:
        visited[x-1] = True
        heapq.heappush(q,(time+1,x-1))
    if 0<=x*2<100001 and not visited[x*2]:
        visited[x*2] = True
        heapq.heappush(q,(time+1,x*2))
print(time)