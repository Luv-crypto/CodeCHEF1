a = int(input())
for i in range(a):
    a1, a2, a3 = map(int, input().split())
    c = a1 + 1
    if c * a3 >= a2:
        print("YES")
    else:
        print("NO")
