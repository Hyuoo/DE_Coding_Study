"""
첫 시작은 무조건 충전
가장 저렴하면 많이 채운다 => 가장 낮은 가격을 기억해두기
"""
n = int(input())
dist = list(map(int, input().split()))
oil = list(map(int, input().split()))
answer = oil[0]*dist[0]
min_oil = oil[0]

for i in range(1, n-1):
    if oil[i] < min_oil:
        min_oil = oil[i]
    answer += min_oil*dist[i]

print(answer)
