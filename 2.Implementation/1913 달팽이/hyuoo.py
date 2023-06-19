n=int(input())
f=int(input())
a=[[0 for _ in range(n)] for _ in range(n)]
d=[0,0,0,0]
m=1
i=j=n//2
while m<=n**2:  # while >> for 바꾸니 988 >> 812 실행시간 개선
    a[i][j]=m
    if m==f:
        f=[i+1,j+1]
    if d[0]:
        d[0]-=1
        j+=1
    elif d[1]:
        d[1]-=1
        i+=1
    elif d[2]:
        d[2]-=1
        j-=1
    elif d[3]:
        d[3]-=1
        i-=1
    else:
        t=int(m**(1/2))
        d = [t,t+1,t+1,t+1]
        i-=1
    m+=1

for i in a:
    print(*i)
print(*f)
