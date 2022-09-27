import sys
n =  int(sys.stdin.readline().rstrip())
arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int,sys.stdin.readline().rstrip()))
dx = [1,0,-1,0]
dy = [0,1,0,-1]
visited = [[False] * n for _ in range(n)]
total = 0
result = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == 1:
            q = [(i,j)]
            visited[i][j] = True
            total +=1
            cnt =1
            while q:
                x,y = q.pop()
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and arr[nx][ny] == 1:
                        visited[nx][ny] = True
                        q.append((nx,ny))
                        cnt+=1
            result.append(cnt)
print(total)
for i in sorted(result):
    print(i)