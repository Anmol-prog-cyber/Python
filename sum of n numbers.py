# sum of n numbers
# n = 3
# 1 2 3 =>sum =6

# n = 4
# 1 2 3 4 => sum= 10

number = int(input("Enter a number")) #3

sumation = 0 

for n in range(1,number+1):
    sumation = sumation + n 
    
    # sumation = 0 + value of n (1) = 1 (sumation)
    # sumation = 1 + value of n (2) = 3 (sumation)
    # sumation = 3 + value of n (3) = 6 (sumation)
    
    
print("Sum of N number is ", sumation)



