l = 0
a = 0
for s,e in sorted([list(map(int,input().split())) for _ in range(int(input()))],key=lambda x:(x[1],x[0])):
    if l<=s:
        a += 1
        l = e
print(a)
