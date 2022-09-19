import sys
import heapq
n = int(sys.stdin.readline().rstrip())
dx = [2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,-1,1,2,-2,2,-2]
for _ in range(n):
    l =int(sys.stdin.readline().rstrip())
    x,y = map(int,sys.stdin.readline().rstrip().split())
    tx,ty = map(int,sys.stdin.readline().rstrip().split())
    move = 0
    q =[]
    visited = [[False] * l for __ in range(l)]
    heapq.heappush(q,(move,x,y))
    while q:
        
        move,x,y = heapq.heappop(q)
        if x == tx and y == ty:
            break
        for dir in range(8):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0<=nx<l and 0<=ny<l and not visited[nx][ny]:
                visited[nx][ny] = True
                heapq.heappush(q,(move+1,nx,ny))
    print(move)