a = int(input())
for i in range(a):
    a1, a2, a3 = map(int, input().split())
    if (a1 + a2 + a3) <= 2 and a1 + a2 + a3 > 0:
        print(1)
    else:
        print(0)
# optimised code
