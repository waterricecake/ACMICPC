import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = list(sys.stdin.readline().rstrip())
length = len(st1) + len(st2)
cnt = 0
for i in range(len(st1)):
    for j in range(len(st2)):
        if st1[i] == st2[-1-j]:
            st2[-1-j] = ' '
            cnt +=2
            break
print(length - cnt)
