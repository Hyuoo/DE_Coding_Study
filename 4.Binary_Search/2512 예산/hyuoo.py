def get(h):
    global n, ar
    ret = 0
    i = 0
    while i<n and ar[i]<h:
        ret+=ar[i]
        i+=1
    return ret + (n-i)*h

n = int(input())
ar = sorted(map(int,input().split()))
money = int(input())

l=0
r=ar[-1]

while l<=r:
    h = (l+r)//2
    if get(h)>money:
        r = h-1
    else:
        l = h+1

print(r)
