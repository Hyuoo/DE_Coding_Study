"""
우선순위 : 빨리 끝나면 good 
"""
answer = 0
n = int(input())
time_table = [] 

for _ in range(n):
    x, y = map(int, input().split())
    time_table.append([x, y])

time_table.sort(key=lambda x: (x[1], x[0]))

end_time = -1
for start_t, end_t in time_table:
    if end_time <= start_t:
        end_time = end_t
        answer += 1

print(answer)
