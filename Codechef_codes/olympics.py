a = int(input())
for i in range(a):
    a1, a2, a3, a4, a5, a6 = map(int, input().split())
    if a1 + a2 + a3 > a4 + a5 + a6:
        print("1")
    else:
        print("2")
