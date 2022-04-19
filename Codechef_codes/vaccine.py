a = int(input())
for i in range(a):
    a1, a2, a3 = map(int, input().split())
    a1 in range(a2, a3)
    if a1 < a2:
        print("Too Early")
    elif a1 > a3:
        print("Too Late")
    else:
        print("Take second dose now")
