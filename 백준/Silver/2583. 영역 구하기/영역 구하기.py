import sys
m,n,k =map(int,sys.stdin.readline().rstrip().split())

arr = [[0] * n for _ in range(m)]
cmd = [
    [0,2,4,4],
    [1,1,2,5],
    [4,0,6,2]
]
for c in range(k):
    m1,n1,m2,n2 =map(int,sys.stdin.readline().rstrip().split())
    for i in range(m1,m2):
        for j in range(n1,n2):
            arr[j][i] = 1
dx = [1,0,-1,0]
dy = [0,1,0,-1]
total = 0
result = []
visited = [[False] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if not visited[i][j] and arr[i][j] ==0:
            cnt = 1
            total +=1
            visited[i][j] = True
            q = [(i,j)]
            while q:
                mnow,nnow = q.pop()
                for dir in range(4):
                    mnxt = mnow +dx[dir]
                    nnxt = nnow +dy[dir]
                    if 0<=mnxt<m and 0<=nnxt<n and not visited[mnxt][nnxt] and arr[mnxt][nnxt] == 0:
                        q.append((mnxt,nnxt))
                        visited[mnxt][nnxt] =True
                        cnt+=1
            result.append(cnt)
print(total)
for i in sorted(result):
    print(i, end =' ')