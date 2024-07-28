def print_triangle(rows):
    num=1
    for i in range(1, rows + 1):
        # Print digits
        for j in range(1, i + 1):
            print(num, end=" ")
            num+=1
       
        print()

num_rows = int(input("Enter the number of rows for the triangle: "))
print_triangle(num_rows)
