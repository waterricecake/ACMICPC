import sys
import heapq
dx = [1,0,-1,0]
dy = [0,1,0,-1]
result = []
for _ in range(int(sys.stdin.readline().rstrip())):
    w,h = map(int,sys.stdin.readline().rstrip().split())
    arr = [['']*w for __ in range(h)]
    visited = [[False] * w for __ in range(h)]
    q = []
    time = 0
    for i in range(h):
        a = list(str(sys.stdin.readline().rstrip()))
        for j in range(w):
            arr[i][j] = a[j]
            if a[j] == "@":
                heapq.heappush(q,(time,1,i,j))
                visited[i][j] = True
            elif a[j] =='*':
                heapq.heappush(q,(time,0,i,j))
                visited[i][j] = True
    while q:
        time, p, x, y = heapq.heappop(q)
        if p == 1:
            if (x == 0 or y == 0 or x ==(h-1) or y ==(w-1)):
                print(time+1)
                break
        for dir in range(4):
            nx = x +dx[dir]
            ny = y + dy[dir]
            if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and arr[nx][ny] == '.':
                visited[nx][ny] = True 
                heapq.heappush(q,(time+1,p,nx,ny))
    else:
        print('IMPOSSIBLE')