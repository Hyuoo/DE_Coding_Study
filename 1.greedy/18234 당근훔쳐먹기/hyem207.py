"""
가장 맛있는 당근 먹어야됨
T일째 되는날 부터 거꾸로 큰 수를 먹어주면 됨  
"""
import sys
n, t = map(int, sys.stdin.readline().split())
carrot = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    carrot.append([a, b])

carrot.sort(key= lambda x: (-x[1], -x[0]))
# print(carrot)


answer = 0
t -= 1 
for a, b in carrot:
    answer+= b*t+a
    t -=1
print(answer)
