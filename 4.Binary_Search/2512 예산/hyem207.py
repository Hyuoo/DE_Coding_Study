import sys
input = sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
total = int(input())
n_list.sort()

left = total//n # 평균부터 최소 상한가
right = n_list[-1]

while left <= right:
    mid = (left+right)//2
    money = 0 
    for i in n_list:
        if i > mid : 
            money += mid 
        else : 
            money += i
    if money > total:
        right = mid -1
    else:
        left = mid + 1

print(right)
    

