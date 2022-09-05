import sys
arr = [0] * 10
x = sys.stdin.readline()
y = sys.stdin.readline()
z = sys.stdin.readline()
result = str(int(x)*int(y)*int(z))
for i in result:
    arr[int(i)] +=1
for k in arr:
    print(k)
    