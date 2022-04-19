a = int(input())
for i in range(a):
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = map(int, input().split())
    if a1 + a3 + a5 + a7 + a9 > a2 + a4 + a6 + a8 + a10:
        print(1)
    elif a1 + a3 + a5 + a7 + a9 < a2 + a4 + a6 + a8 + a10:
        print(2)
    else:
        print(0)
