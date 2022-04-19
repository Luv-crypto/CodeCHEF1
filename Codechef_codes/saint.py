from cgi import print_directory


a = int(input())
for i in range(a):
    a1, a2, a3 = map(int, input().split())
    b1, b2, b3 = map(int, input().split())
    if (a1 + a2 + a3) == (b1 + b2 + b3):
        print("Pass")
    else:
        print("Fail")
