# 18234 당근 훈쳐먹기

# 오리 텃밭에 n종류의 당근 하나씩 심고, T일동안 재배
# 당근 i에 사용할 만큼 맛을 증가 시켜주는 영양제 T만큼 준비
# w : 처음의 맛 p : 맛을 증가시캬주는 영양제
# 토끼가 먹을 수 있는 당근의 맛의 합의 최댓값
"""
출력 예시
1일차 오전에 당근 1과 당근 2를 심음
1 맛 3
2 맛 4 - 토끼가 당근 뽑아 먹음 : 토끼 먹은 양

원래의 맛을 신경 안쓰고, 성장치만 신경을 써도 됌
성장치가 가장 큰걸 제일 많이 키워야  -> 늦게 먹어야
T일 기준으로 제일 성장 높이게 하는 것 (T 중 에서 토끼가 안먹을 수 있다는 거)
일수 * 성장치 + 기본값

마지막 삼일만 먹는 것
"""
import sys

input = sys.stdin.readline
n, t = map(int, input().split())

carrot = []
for _ in range(n):
    w, p = map(int, input().split())
    carrot.append((w, p))

carrot.sort(key=lambda x: x[1], reverse=True)

answer = 0
for w, p in carrot:
    answer += (w + p*(t-1))
    t -= 1

print(answer)
