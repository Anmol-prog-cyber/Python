


''' 

data types 

int ----------> integer (Numbers) (0,1,2,....) 
str ----------> string  (collection of characters) ("anmol)

'''


#1. input("string") function will use print() internally and 
#   print the string in console that is provided in input() function

#2. input() will wait for the user to provide some input at run time

#a=10 # initialized value 10 to variable a

a = input("Enter number1 ") # takes input at run time from user
b = input("Enter number2 ") # takes input at run time from user

#input() treats all user input as string(sequence of charater) by default

#type() function will display you want type of data ( integer(int), string(str).....) does variable holds
print(type(a))
print(type(b))

#since we want to add numbers(intergers 0,1,2,3) we have to convert string to intergers

c = int(a) + int(b) # string type is convereted to integer :type casting

# type casting is converting from one data type to another data type


print("sum",c)

'''
summary:

1. input()       -------> takes input from user at run time
                 -------> it treats input as string by default
              
2. data types    -------> int , string 

3. type()        -------> help us to find the data type of variable

4. type casting  -------> converting data type from one type to another
                 

'''
