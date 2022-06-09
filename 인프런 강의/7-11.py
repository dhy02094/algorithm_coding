import sys
sys.stdin = open('input.txt','rt')

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def DFS(x,y):
    global cnt
    if x==c and y==d:
        cnt += 1
    else :
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<=n-1 and 0<=yy<=n-1 and ch[xx][yy]==0 and board[x][y] < board[xx][yy]:
                ch[xx][yy] = 1
                DFS(xx,yy)
                ch[xx][yy] = 0

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
mi = 2147000000
mip = []
ma = -2147000000
map = []
for i in range(n):
    for j in range(n):
        if board[i][j] < mi : 
            mi = board[i][j]
            mip = [i,j]
        if board[i][j] > ma :
            ma = board[i][j]
            map = [i,j]
cnt = 0
a,b = mip[0],mip[1]
c,d = map[0],map[1]
ch[a][b] = 1
DFS(a,b)
print(cnt)

