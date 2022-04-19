a = int(input())
for i in range(a):
    a1, a2, a3, a4, a5 = map(int, input().split())
    b = a1 / a3
    c = a2 / a4
    d = min(b, c)
    if d >= a5:
        print("YES")
    else:
        print("NO")
