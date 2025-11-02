factorial_number = int(input("enter number to calculate factorial"))
number=1
factorial =1
while factorial <= factorial_number:
    factorial =factorial * number
    number = number + 1

print("factorial is ",factorial)
