import sys
sys.stdin=open("input.txt", "r")

from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dq = deque([(v,idx) for idx, v in enumerate(a)])
    cnt = 0
    while 1:
        if dq[0][0] == max(dq)[0]:
            cnt += 1
            if dq[0][1] == m :
                print(cnt)
                break
            else :
                dq.popleft()
        else :
            # deque rotate가 음수이면 앞에껄 빼서 맨뒤로 넣어준다.
            # 양수는 뒤에껄 앞으로
            dq.rotate(-1)