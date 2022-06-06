import sys
sys.stdin = open('input.txt','rt')

def DFS(L, sum, time):
    global res
    if time > m :
        return
    if L == n :
        if sum > res :
            res = sum
    else :
        DFS(L+1, sum+pv[L], time+pt[L])
        DFS(L+1, sum, time)

n, m = map(int, input().split())
pv = []
pt = []
for _ in range(n):
    a,b = map(int, input().split())
    pv.append(a)
    pt.append(b)
res = -2147000000
DFS(0,0,0)
print(res)