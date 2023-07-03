def bsearch(l,r,x):
    global s
    while l<=r:
        m = (l+r)//2
        if s[m]==x:
            return 1
        elif s[m]<x:
            l=m+1
        else:
            r=m-1
    return 0
n=int(input())
s = sorted(map(int,input().split()))
m=input()
ans = []
for i in map(int,input().split()):
    ans.append(bsearch(0,n-1,i))
print(*ans)
