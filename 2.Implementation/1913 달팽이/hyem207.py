"""
위로 2칸 -> (방향전환) -> 오른쪽 2칸 -> (방향전환) -> 아래 3칸 -> (방향전환) -> 왼쪽 3칸  -> (방향 전환) -> 위로 4칸 -> (방향전환) ...
흐름 : 칸 채우고 방향전환함. 이때 이동하는 칸수는 2개 단위로 바뀜
- 방향 : 위 -> 오른쪽 -> 아래 -> 왼쪽  반복
==> 1060ms
"""
import sys

def print_n_list(n, n_list):
    for i in range(n):
        for j in range(n):
            print(n_list[i][j], end=' ')
        print()

input = sys.stdin.readline
n = int(input())
x = int(input())

n_list = [[0]*n for _ in range(n)]
answer_x = 0
answer_y = 0

# 위 -> 오 -> 아 -> 왼
dx = [0,1,0,-1]
dy = [-1,0,1,0]

fill = 1
fill_n = 1
d_idx = 0 

# n에 따른 중심좌표 x
i = n//2
j = n//2

while fill < n*n:
    # 왼쪽이나 아래쪽 방향이 돌아오면 채우는 수는 +1
    if d_idx == 0 or d_idx == 2:
        fill_n += 1
    # 칸 채우기
    for _ in range(fill_n):
        if fill > n*n :
            break
        n_list[i][j] = fill
        if fill == x :
            answer_x = i + 1
            answer_y = j + 1
        i += dy[d_idx]
        j += dx[d_idx]
        fill += 1
    # 방향 전환 전 이전 좌표로 이동
    fill -= 1
    i -= dy[d_idx]
    j -= dx[d_idx]
    # 방향 전환 
    d_idx = (d_idx+1)%4  

print_n_list(n,n_list)
print(answer_x, answer_y)
