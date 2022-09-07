import sys

while True:
    data = list(map(int,sys.stdin.readline().rstrip().split()))
    if data[0] == 0:
        break
    s = []
    m = 0
    for i in range(data[0]):
        h = data[i+1]
        pos = i+1
        if s:
            while s[-1][0] > h:
                height, pos = s[-1]
    
                s.pop()
                m = max(m,height*(i+1-pos))
                if not s:
                    break
        s.append([h,pos])
    while s:
        height, pos = s.pop()
        m = max(m, height*(data[0]-pos+1))
    print(m)