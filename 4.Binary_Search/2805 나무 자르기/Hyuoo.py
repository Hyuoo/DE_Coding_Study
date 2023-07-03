def cutting(n,h):
    global trees
    ret = 0
    i=0
    while i<n and trees[i]>h:
        ret += trees[i]
        i+=1
    return ret-i*h

n,m = map(int,input().split())
trees = sorted(map(int,input().split()),reverse=True)

l = 0
r = trees[0]

while l<=r:
    h = (l+r)//2
    get = cutting(n,h)
    if get<m:
        r = h-1
    else:
        l = h+1
print(r)
'''
고려할톱날 높이 l~r (=0,max())
매 가능한 높이 중간값으로 가져가는 길이 계산해서
같거나 크면 높이 올려보기 (가져가는 값 줄임)
작으면 높이 낮추기 (가져가는 값 늘림)
'''
