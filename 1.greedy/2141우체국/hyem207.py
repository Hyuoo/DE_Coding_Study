"""
앞에서부터 카운트 했을 때 인구 수 총합의 절반인 지역
"""
n = int(input())
x = []
total = 0
for _ in range(n):
    a, b = map(int,input().split())
    total += b
    x.append([a, b])

x.sort(key=lambda x: x[0])
middle = total/2

cnt = 0
for a, b in x:
    cnt += b
    if cnt >= middle:
        print(a)
        break
