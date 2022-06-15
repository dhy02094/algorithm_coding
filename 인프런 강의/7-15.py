import sys
sys.stdin = open('input.txt', 'rt')
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
day = [[0]*m for _ in range(n)]
Q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            Q.append((i,j))

while Q:
    tmp = Q.popleft()
    for k in range(4):
        x = tmp[0] + dx[k]
        y = tmp[1] + dy[k]
        if 0<=x<n and 0<=y<m and board[x][y]==0:
            board[x][y] = 1
            day[x][y] = day[tmp[0]][tmp[1]] + 1
            Q.append((x,y))

flag = 1
for i in range(n):
    for j in range(m):
        if board[i][j]==0:
            flag+=1
result = 0
if flag == 1:
    for i in range(n):
        for j in range(m):
            if day[i][j] > result :
                result = day[i][j]
    print(result)
else :
    print(-1)
        

