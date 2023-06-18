n=int(input())
dist = list(map(int,input().split()))
cost = list(map(int,input().split()))[:-1]
m = 1e9
ans = 0
for i in range(n-1):
    m = min(m,cost[i])
    ans += m*dist[i]
print(ans)
