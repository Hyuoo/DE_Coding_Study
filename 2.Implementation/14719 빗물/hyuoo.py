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

'''
빗물 다 채워놓고
좌우에서부터 물이차는 만큼 깎아먹는 식
'''
