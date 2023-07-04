import sys
input = sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_list.sort()
answer = []

def search(target, left, right):
    if left <= right :
        mid = (left+right) // 2
        if n_list[mid] == target:
            return 1
        elif n_list[mid] < target :
            return search(target, mid+1, right)
        elif n_list[mid] > target :
            return search(target, left, mid-1)
    else:
        return 0

for target in m_list:
    answer.append(search(target,0,n-1))


print(*answer)
