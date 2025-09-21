# whether Number is even number or odd number
'''
even --> 2 , 4 , 6 ,8 , 10 .....
odd  --> 1, 3, 5, 7, 9 .....

Hint : operator Modulus or remainder operator %

reminder = Number % 2

if reminder is zero it is even
f reminder is not zero it is odd

example :
Number =2
reminder = Number % 2 (even)

Number = 3
reminder = Number % 2 (odd)

'''

number = int(input("Enter any number"))

reminder = number % 2

if reminder == 0:
    print("Number is even")
else:
    print("Number is odd")
