odd = 0 
even = 0
sum = 0
for i in range(10):  
    i = eval(input(f"Enter a number {i+1}:  "))
    if i % 2 == 0:
        even += i
    else:
        odd += i
    sum += i


print(f"Sum of all Even numbers: {even}")
print(f"Sum of all Odd numbers: {odd}")
print(f"Sum of all the numbers: {sum}")

