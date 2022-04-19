a = int(input())
for i in range(a):
    a1, a2, a3 = map(int, input().split())
    c = a1 + a3 * 2
    if c >= a2:
        print("YES")
    else:
        print("NO")
