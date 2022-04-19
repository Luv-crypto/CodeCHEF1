a = int(input())
for i in range(a):
    a1, a2 = map(int, input().split())
    s = a2 * (a2 + 1) / 2
    for i in range(a1 - 1):
        s = s * (s + 1) / 2
    print(int(s))
