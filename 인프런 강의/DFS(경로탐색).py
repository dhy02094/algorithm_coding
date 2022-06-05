import sys
sys.stdin=open("input.txt", "r")

# 문제설명
# 섹션6 15번
# 경로를 탐색하는데 1번에서 5번을 가는 가지수 세는 코드

def DFS(v):
    global cnt
    if v == n :
        cnt+=1
        print(path)
    else :
        for i in range(1, n+1):
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i] = 0
                
n, m = map(int, input().split())
g = [[0] * (n+1) for _ in range(n+1)]
ch = [0] * (n+1)
path =[1]
for i in range(m):
    a,b = map(int, input().split())
    g[a][b] = 1
cnt = 0
ch[1]=1
DFS(1)
print(cnt)
