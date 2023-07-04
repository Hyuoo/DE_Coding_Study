n = int(input())
ar = sorted(map(int,input().split()))

mini = 2000000000
mini_set = []

l = 0
r = n-1

while l<r:
    tmp = ar[l]+ar[r]
    if mini>abs(tmp):
        mini = abs(tmp)
        mini_set = [ar[l],ar[r]]
    if tmp==0:
        mini_set = [ar[l], ar[r]]
        break
    if tmp<0:
        l += 1
    else:
        r -= 1

print(*mini_set)
