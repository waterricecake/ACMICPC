import sys
import heapq
n,m,h = map(int,sys.stdin.readline().rstrip().split())
arr = [[[0] *n for __ in range(m)] for _ in range(h)] #arr[h][m][n]
day = 0
q = []
visited =[[[False] *n for __ in range(m)] for _ in range(h)]
for k in range(h):
    for i in range(m):
        li = list(map(int,sys.stdin.readline().rstrip().split()))
        for j in range(n):
            arr[k][i][j] = li[j]
            if li[j] ==1:
                heapq.heappush(q,(day,i,j,k))
                visited[k][i][j] = True
dx = [1,0,-1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]          
while q:
    day, x,y,z = heapq.heappop(q)
    ch = False
    for dir in range(6):
        nx = x + dx[dir]
        ny = y + dy[dir]
        nz = z + dz[dir]
        if 0<=nx<m and 0<=ny<n and 0<=nz<h and not visited[nz][nx][ny] and arr[nz][nx][ny] == 0:
            arr[nz][nx][ny] = 1
            visited[nz][nx][ny] = True
            heapq.heappush(q,(day+1,nx,ny,nz))
            ch =True    
check = True
for k in range(h):
    for i in range(m):
        for j in range(n):
            if arr[k][i][j] == 0:
                check = False
if check:
    print(day)
else:
    print(-1)