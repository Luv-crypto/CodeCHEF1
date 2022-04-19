a = int(input())
for i in range(a):
    a1, a2, a3, a4, a5, a6 = map(int, input().split())
    if a2 >= a1 and a4 >= a3 and a6 <= a5:
        print("YES")
    else:
        print("NO")
