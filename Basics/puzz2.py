import csv

input_file_path = "C:\\Users\\Admin\\Desktop\\python\\Basics\\input2.txt"
# input_file_path = "input2.txt"

with open(input_file_path) as f:
    dimension_reader = csv.reader(f, delimiter="x")

    box_dimensions = [
        (int(length), int(width), int(height))
        for length, width, height in dimension_reader
    ]
    print(box_dimensions)

    total = 0

    for length, width, height in box_dimensions:
        m = min((length + width, width + height, height + length))
        area = (length * width * height) + 2 * m
        total += area
    print(total)

    # Map reduce