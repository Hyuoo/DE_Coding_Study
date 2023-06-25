"""
1차 시도 (실패): stack 
    - 블럭 수가 적어지면 고이기 시작하고 끝은 고인 시작점보다 높은 부분이다. == "고인물" 
    - 고인물의 최대 높이는, 양쪽 사이드의 최소 높이 
2차 시도 (성공/다른 풀이 참고) : 48ms
    - 특정 블럭을 기준으로 좌우에 더 높은 블럭이 있을 경우 고인다.
        - 이때 고이는 높이는 좌/우 블럭 높이의 최대값 중 작은 값이 됨  
"""
# 2차 시도
import sys
input = sys.stdin.readline
h, w = map(int, input().split())
wall = list(map(int, input().split()))
answer = 0

for i in range(1, w-1) :
    left_max = max(wall[:i]) 
    right_max = max(wall[i+1:])
    top = min(left_max, right_max)
    if wall[i] < top:
        answer +=  top - wall[i]
print(answer)


"""
# 1차 시도 (실패)
# 원인 : 모든 경우를 생각해서 작성한 코드가 아님. (반례가 많았음)
input = sys.stdin.readline
h, w = map(int, input().split())
wall = list(map(int, input().split()))
answer = 0

stack = deque() # 물 웅덩이의 왼쪽부터 오른쪽 벽 저장

if h < 3:
    print(0)
else:
    for i in range(0, len(wall)-1):
        now= wall[i]
        if stack and wall[i] >= stack[0] : # 이전 벽이 현재보다 더 높음 (=감소하는 경우)
            min_wall = min(stack.popleft(), wall[i])
            while stack:
                answer += min_wall - stack.pop()
        if i+1 < len(wall) and wall[i] > wall[i+1] : # 감소하는 경우
            stack.append(wall[i])
        else :
            if stack : stack.append(wall[i])

    if stack : 
        min_wall = min(stack.popleft(), wall[-1])
        while stack:
            answer += min_wall - stack.pop()
        print(answer)
"""
