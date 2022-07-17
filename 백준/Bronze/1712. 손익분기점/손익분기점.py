## 백준 기본수학1단계 1.손익분기점(1712)

A, B, C = map(int, input().split()) 

if B >= C:
    print(-1)
else:
    print(A//(C-B)+1)

