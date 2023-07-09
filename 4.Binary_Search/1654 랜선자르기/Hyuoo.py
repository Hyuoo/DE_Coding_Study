k,n = map(int,input().split())
ar = sorted([int(input()) for _ in range(k)])

l = 1
r = ar[-1]

while l<=r:
    m = (l+r)//2
    ret = sum(map(lambda x:x//m,ar))
    if ret<n:
        r = m-1
    else:
        l = m+1

print(r)
