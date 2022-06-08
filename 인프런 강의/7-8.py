import sys
sys.stdin = open('input.txt','rt')
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
Q = deque()
cnt = 0
Q.append((n//2,n//2))
ch[n//2][n//2] = 1
cnt += tree[n//2][n//2]
L = 0
while 1:
    if L == n//2 :
        break
    size = len(Q)
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0 :
                ch[x][y] = 1
                cnt += tree[x][y]
                Q.append((x,y))
    L += 1
print(cnt)