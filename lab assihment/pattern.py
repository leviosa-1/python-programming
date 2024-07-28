def right_angle_pyramid(row):
    for i in range(1,row+1):
        for j in range(row-i):
            print(" ",end='')
        for k in range(i):
            print("*",end='')
        print()

def pyramid(row):
    for i in range(row):
        # Print pace before the aterik
        for j in range(row - i - 1):
            print(" ", end="")
        
        # Print aterik for the current row
        for k in range(2 * i + 1):
            print("*", end="")
        
        # Move to the next line after completing a row
        print()

row=int(input("enter row of pyramid you want to print:"))
right_angle_pyramid(row)
pyramid(row)
