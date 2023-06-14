f=lambda:[*map(int, input().split())]
n,t=f()
c=sorted([f() for _ in range(n)],key=lambda x:-x[1])
a=0
for q,w in c:
    t-=1
    a+=t*w+q
print(a)
