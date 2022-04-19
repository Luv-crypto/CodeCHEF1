a = int(input())
for i in range(a):
    a1, a2, a3, a4 = map(int, input().split())
    if a1 * a2 <= a3 * a4:
        print("Yes")
    else:
        print("No")
