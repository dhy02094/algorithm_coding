import sys
sys.stdin = open('input.txt','rt')

#220607 16:00 ~ 16:48
# A = 65 , Z = 90, 64를 뺴주자.

def DFS(L,P):
    global cnt
    if L == n:
        cnt += 1
        for j in range(P):
            print(chr(res[j]+64),end='')
        print()
    else :
        for i in range(1,27):
            if a[L] == i:
                res[P]=i
                DFS(L+1, P+1)
            elif i >= 10 and a[L] == i//10 and a[L+1] == i%10:
                res[P]=i
                DFS(L+2,P+1)

a = list(map(int, input()))
cnt = 0
n= len(a)
a.insert(n,-1)
res = [0]*(n+3)
DFS(0,0)
print(cnt)







# 1번,2번만 맞음
# def DFS(L,ans):
#     global cnt
#     if L == n :
#         cnt+=1
#         print(ans)
#     else :
#         if L < n:
#             if int(a[L:L+1]) != 0:
#                 b = chr(int(a[L:L+1])+64)
#                 DFS(L+1,ans+b)
#         if L<n-1:
#             c = int(a[L:L+2])
#             if 0 < c <= 26 :
#                 d = chr(c+64)
#                 DFS(L+2,ans+d)
#         ans=ans[:-1]

# a = input()
# cnt = 0
# n = len(a)
# DFS(0,'')
# print(cnt)
