from traceback import print_tb


a = int(input())
for i in range(a):
    a1, a2 = map(int, input().split())
    if a1 and a2 > 0:
        print("Solution")
    elif a1 == 0:
        print("Liquid")
    elif a2 == 0:
        print("Solid")
