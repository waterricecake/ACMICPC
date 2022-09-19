import sys
sys.setrecursionlimit(1000000)
def dfs(i,j):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for dir in range(4):
        nx = i + dx[dir]
        ny = j + dy[dir]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and farm[nx][ny] == 1:
            visited[nx][ny] = True
            dfs(nx,ny)
t = int(sys.stdin.readline().rstrip())
result = []
for _ in range(t):
    n,m,k = map(int,sys.stdin.readline().rstrip().split())
    farm = [[0]*m for __ in range(n)]
    for i in range(k):
        x,y = map(int,sys.stdin.readline().rstrip().split())
        farm[x][y] = 1
    visited = [[False]*m for _ in range(n)]
    q = []
    worm = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and farm[i][j] == 1:
                worm +=1
                dfs(i,j)
    result.append(worm)
for w in result:
    print(w)