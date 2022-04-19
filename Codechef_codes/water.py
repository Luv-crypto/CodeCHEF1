a = int(input())
for i in range(a):
    a1, a2, a3, a4 = map(int, input().split())
    c = int(a3 / 2) + a2
    d = a1 * c
    if d <= a4:
        print("YES")
    else:
        print("NO")
