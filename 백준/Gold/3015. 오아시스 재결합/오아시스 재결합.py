import sys

n = int(sys.stdin.readline().rstrip())
result = 0
s = []
while n:
    h = int(sys.stdin.readline().rstrip()) 
    cnt = 1
    if s:
        while s[-1][0] <=h:
            result += s[-1][1]
            if (s[-1][0] == h):
                cnt +=s[-1][1]
            s.pop()
            if not s:
                break
        else:
            result +=1
    
    s.append([h,cnt])
    n -=1   
    
print(result)