input_file_path = "C:\\Users\\Admin\\Desktop\\python\\Basics\\input5.txt"

with open(input_file_path) as f:
    x = ""
    condn1 = 0
    condn2 = 0
    condn3 = 0
    total_nicestrings = 0
    total_strings = 0
    for line in f:
        for letter in line:
            if letter == x:
                condn2 += 1
            if (
                letter == "a"
                or letter == "e"
                or letter == "i"
                or letter == "o"
                or letter == "u"
            ):
                condn1 += 1

            if letter == "b" and x == "a":
                condn3 += 1
            if letter == "d" and x == "c":
                condn3 += 1
            if letter == "q" and x == "p":
                condn3 += 1
            if letter == "y" and x == "x":
                condn3 += 1
            x = letter
        total_strings += 1
        if condn3 == 0 and condn1 >= 3 and condn2 > 0:
            total_nicestrings += 1
            x = ""
            condn1 = 0
            condn2 = 0
            condn3 = 0
        else:

            x = ""
            condn1 = 0
            condn2 = 0
            condn3 = 0
    print(total_nicestrings, total_strings)
