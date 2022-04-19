a = int(input())
for i in range(a):
    b = int(input())
    c = b / int(4)
    if c.is_integer():
        print("Good")
    else:
        print("Not Good")
