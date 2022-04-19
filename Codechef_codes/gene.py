a1, a2 = map(str, input().split())
if a1 == "R" or a2 == "R":
    print("R")
elif a1 == "B" and a2 != "R" or a2 == "B" and a1 != "R":
    print("B")
elif a1 == a2 == "R":
    print("R")
elif a1 == a2 == "B":
    print("B")
else:
    print("G")
