a = int(input())
for i in range(a):
    a1 = list(map(int, input().split()))
    c = sorted(a1)
    print(c[-1] + c[-2])
