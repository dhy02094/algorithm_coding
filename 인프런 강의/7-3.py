import sys
sys.stdin = open('input.txt','rt')

def DFS(L,sum):
    global res
    if L == n :
        # 왜 음수가 어차피 대칭으로 다시 생기는지 이해하기!
        if 0<sum<=s:
            res.add(sum)
    else :
        DFS(L+1, sum+G[L]) # 왼
        DFS(L+1, sum-G[L]) # 오
        DFS(L+1, sum)      # 가만히
        
n = int(input())
G = list(map(int, input().split()))
s = sum(G)
res = set()
DFS(0,0)
print(s-len(res))