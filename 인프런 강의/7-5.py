import sys
sys.stdin = open('input.txt','rt')

def DFS(L,a,b,c):
    global res
    if L == n :
        if (max(a,b,c) - min(a,b,c)) < res and a!=b and b!=c and a!=c:
            res = max(a,b,c) - min(a,b,c)
    else :
        DFS(L+1, a+cv[L],b,c)
        DFS(L+1, a, b+cv[L],c)
        DFS(L+1, a,b,c+cv[L])            

n = int(input())
cv = []
for _ in range(n):
    cv.append(int(input()))
res = 2147000000
DFS(0,0,0,0)
print(res)

