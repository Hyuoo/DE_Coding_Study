inputs=lambda:map(int,input().split())

n,m=inputs()
x,y,d=inputs()

dr=[[-1,0],[0,1],[1,0],[0,-1]]
maps=[[*inputs()] for _ in range(n)]
dirty=[[1^maps[i][j] for j in range(m)] for i in range(n)]

c=0
while 1:
    if maps[x][y]:
        break
    if dirty[x][y]:
        dirty[x][y]=0
        c+=1
    if sum([dirty[x+tx][y+ty] for tx, ty in dr])==0:
        tx,ty=dr[d]
        x-=tx
        y-=ty
    else:
        while 1:
            d=(d-1)%4
            tx,ty=dr[d]
            if dirty[x+tx][y+ty]:
                x+=tx
                y+=ty
                break
print(c)
