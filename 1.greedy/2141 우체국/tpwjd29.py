# 2285 우체국

# 수직선과 같은 일직선상에 N개의 마을
# 각 사람들까지의 거리의 합이 최소가 되는 우체국 세우기
# 우체국 세울 위치를 구하는 프로그램
n = int(input())
village = []
total = 0
for _ in range(n):
	x, a = map(int, input().split())
	village.append((x, a))
	total += a 		# 전체 인구 수
village.sort() # village
tmp = 0
for x, a in village :
	tmp += a
	if tmp >= total / 2 : # 사람이 절반 이상의 마을
		print(x)
		break


