import sys
import heapq
f,s,g,u,d = map(int,sys.stdin.readline().rstrip().split())
visited = [False for _ in range(f+1)]
visited[0] = True
visited[s] = True
q = []
heapq.heappush(q,(0,s))
ud = [u,-d]
check = False
while q:
    cnt,now = heapq.heappop(q)
    if now == g:
        check = True
        break
    for button in ud:
        nxt = now + button
        if 0<nxt<=f and not visited[nxt]:
            visited[nxt] = True
            heapq.heappush(q,(cnt+1,nxt))
if check:
    print(cnt)
else:
    print('use the stairs')