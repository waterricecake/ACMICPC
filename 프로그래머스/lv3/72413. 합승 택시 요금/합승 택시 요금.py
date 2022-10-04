import heapq
def dis(n,start,target,fare_graph):
    inf = 100000*n
    visited = [inf for _ in range(n+1)]
    q  = []
    heapq.heappush(q,(0,start))
    visited[start] = 0
    while q:
        total,now = heapq.heappop(q)
        for nxt,fare in fare_graph[now]:
            if visited[nxt]>total+fare:
                visited[nxt] = total+fare
                heapq.heappush(q,(total+fare,nxt))
    return visited[target]

def solution(n, s, a, b, fares):
    fare_graph = [[] for _ in range(n+1)]
    for x,y,z in fares:
        fare_graph[x].append((y,z))
        fare_graph[y].append((x,z))
    answer = 100000*n
    for i in range(1,n+1):
        answer = min(answer,dis(n,s,i,fare_graph)+dis(n,i,a,fare_graph)+dis(n,i,b,fare_graph))
    return answer