import sys

sys.setrecursionlimit(3000000)

n, m = map(int,sys.stdin.readline().rstrip().split())
arr =[0]*n
for _ in range(n):
    s = list(map(int,sys.stdin.readline().rstrip().split()))
    arr[_] = s
check = [[False] * m for _ in range(n)]
q = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]
maxs = 0
count = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and check[i][j] == False:
            count +=1
            cnt = 1
            check[i][j] = True
            q.append((i,j))
            while q:
                nx, ny = q.pop()
                for dir in range(4):
                    nx_ = nx + dx[dir]
                    ny_ = ny + dy[dir]
                    if nx_<0 or ny_<0 or nx_>=n or ny_>=m:
                        continue
                    if arr[nx_][ny_] == 1 and check[nx_][ny_] == False:
                        q.append((nx_,ny_))
                        check[nx_][ny_] = True
                        cnt += 1
            maxs = max(maxs,cnt)
print(count)
print(maxs)
