column = eval(input("Enter number of columns --->    "))
for x in range (1, 11):
    for y in range(1, column + 1):
        print(f"*",end=" ")
    print()