import sys
input = sys.stdin.readline
n = int(input())
ar = []
s = 0
for _ in range(n):
    a,b=map(int,input().split())
    ar.append([a,b])
    s+=b
ar.sort()
acc = 0
for a,b in ar:
    acc+=b
    if acc>=s/2:
        print(a)
        break
