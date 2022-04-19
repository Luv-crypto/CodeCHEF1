a = int(input())
for i in range(a):
    a1, a2 = map(int, input().split())
    if a1 == 0:
        print(0)
    elif a1 < a2:
        print(-1)
    elif a1 % a2 == 0:
        print(a1 // a2)
    else:
        print(-1)
