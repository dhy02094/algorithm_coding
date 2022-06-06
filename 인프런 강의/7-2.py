import sys
sys.stdin = open('input.txt', 'rt')

def DFS(L, sum):
    global res
    if L == n+1 :
        if sum > res :
            res = sum
    else :
        if L + t[L] <= n+1 :
            DFS(L+t[L], sum+p[L])
        DFS(L+1, sum)
             

n = int(input())
t = [0]
p = [0]
for _ in range(n):
    a,b = map(int, input().split())
    t.append(a)
    p.append(b)
res = -2147000000
DFS(1,0)
print(res)