import sys
import heapq
m,n = map(int,sys.stdin.readline().rstrip().split())
arr =[0]*n
for _ in range(n):
    s = list(map(int,list(sys.stdin.readline().rstrip().split())))
    arr[_] = s

q = []

day = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            visited[i][j] == True
            heapq.heappush(q,(0,i,j))
while q:
    day,i,j = heapq.heappop(q)
    for dir in range(4):
        nx = i+ dx[dir]
        ny = j+ dy[dir]
        if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 0 and not visited[nx][ny]:
            heapq.heappush(q,(day+1,nx,ny))
            arr[nx][ny] = 1
            visited[nx][ny] = True
check = True
for i in arr:
    if 0 in i:
        check = False
if check:
    print(day)
else:
    print(-1)