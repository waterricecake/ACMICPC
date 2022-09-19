import sys
sys.setrecursionlimit(10000)
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def dfs_b(i,j,color,t=True):
    for dir in range(4):
        nx = i + dx[dir]
        ny = j + dy[dir]
        if not t:
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if color == "B":
                    if arr[nx][ny] == color:
                        visited[nx][ny] = True
                        dfs_b(nx,ny,color,False)
                else:
                    if arr[nx][ny] == "R" or arr[nx][ny] == "G":
                        visited[nx][ny] = True
                        dfs_b(nx,ny,color,False)
        else:
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and arr[nx][ny] == color:
                visited[nx][ny] = True
                dfs_b(nx,ny,color)
n = int(sys.stdin.readline().rstrip())
arr = [[] for _ in range(n)]
for _ in range(n):
    arr[_] = list(str(sys.stdin.readline().rstrip()))

result = []
color =0
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            color+=1
            dfs_b(i,j,arr[i][j])
result.append(color)
color =0
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            color+=1
            dfs_b(i,j,arr[i][j],False)
result.append(color)
for s in result:
    print(s,end=" ")