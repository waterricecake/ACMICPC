import sys
n = int(sys.stdin.readline().rstrip())

arr = [[] for _ in range(n)]
max_h = 0
for _ in range(n):
    info = list(map(int,sys.stdin.readline().rstrip().split()))
    for i in info:
        max_h = max(max_h,i)
    arr[_] = info

answer = n**2
dx = [1,0,-1,0]
dy = [0,1,0,-1]
safe = 0
for rain in range(max_h+1):
    visited = [[False] *n for _ in range(n)]
    total = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] =True
                if arr[i][j] >rain:
                    total+=1
                    q = [(i,j)]
                    while q:
                        x,y = q.pop()
                        for dir in range(4):
                            nx = x+dx[dir]
                            ny = y + dy[dir]
                            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                                visited[nx][ny] =True
                                if arr[nx][ny]>rain:
                                    q.append((nx,ny))
    safe = max(total,safe)
print(safe)