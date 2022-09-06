import sys
class Node():
    def __init__(self,val:int,prev=None,nxt=None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

n, k = map(int,sys.stdin.readline().rstrip().split())

startnode = Node(1)
node = startnode
for i in range(2,n+1):
    node.nxt = Node(i)
    node.nxt.prev = node
    node = node.nxt

node.nxt = startnode
startnode.prev = node
node = startnode
arr = [0] * n
for i in range(n):
    for _ in range(k-1):
        node = node.nxt
    arr[i] = node.val
    node.prev.nxt = node.nxt
    node.nxt.prev = node.prev
    node = node.nxt
    

print("<"+", ".join(map(str,arr))+">")