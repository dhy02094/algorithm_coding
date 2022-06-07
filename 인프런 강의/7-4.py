import sys
sys.stdin = open('input.txt','rt')

# 52분
# L을 지정하지 않을시 중복되는 경우를 끊임없이 센다. 항상 L을 써서 스탑 스킬 생각을 하자.
def DFS(L, sum):
    global cnt
    if sum > t :
        return
    if L == k :
        if sum == t:
            cnt += 1
    else :
        for i in range(cc[L]+1):
            DFS(L+1, sum+(cv[L]*i))
                
t = int(input())
k = int(input())

cv = []
cc = []
for _ in range(k):
    a, b= map(int, input().split())
    cv.append(a)
    cc.append(b)
cnt = 0
DFS(0,0)
print(cnt)