import sys

class Node():
    def __init__(self,val:int,prev=None,nxt =None):
        self.val = val
        self.prev = prev
        self.nxt = nxt


data = sys.stdin.readline().rstrip()
head = Node("")
node = head
for s in data:
    node.nxt = Node(s)
    node.nxt.prev = node
    node = node.nxt

for _ in range(int(sys.stdin.readline().rstrip())):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == "L":
        if node.prev:
            node = node.prev
    elif cmd[0] == "D":
        if node.nxt:
            node = node.nxt
    elif cmd[0] =="B":
        if node.prev:
            if node.nxt:
                node.prev.nxt = node.nxt
                node.nxt.prev = node.prev
                node =node.prev
            else:
                node.prev.nxt = None
                node = node.prev
    elif cmd[0] == "P":
        new = Node(cmd[1])
        new.nxt = node.nxt
        new.prev = node
        if node.nxt:
            node.nxt.prev = new
        node.nxt = new
        node = new

p = head
while p:
    print(p.val, end = "")
    p = p.nxt