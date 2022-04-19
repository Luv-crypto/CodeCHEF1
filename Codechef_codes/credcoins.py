a = int(input())
for i in range(a):
    a1, a2 = map(int, input().split())
    c = int((a1 * a2) / int(100))
    if c >= 1:
        print(c)
    else:
        print(int(0))
