h,w=map(int,input().split())
a=[*map(int,input().split())]
water = [h for _ in range(w)]
l,r = 0,0

for i in range(w):
    if a[i]>l:
        l = a[i]
    water[i]=min(water[i],l)

for i in reversed(range(w)):
    if a[i]>r:
        r = a[i]
    water[i]=min(water[i],r)

print(sum(water[i]-a[i] for i in range(w)))
