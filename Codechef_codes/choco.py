a = int(input())
for i in range(a):
    a1, a2, a3 = map(int, input().split())
    e = (a1 - a2) * a3
    print(e)
