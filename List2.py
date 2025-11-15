print("List concepts")
a = 10 #  variable(a) and variable can store only one value

# Data structure : if you want to store more than one value to single entity then we use data structure

# Types of data structures in python
"""
1. List ----> [] ----> square/matrix bracket
2. set -----> () ----> parenthesis/small bracket
3. dictionary ----> { } ----> curley/set bracket
4. tuple ----> () ----> parenthesis
"""
# List data structure to hold multiple values
# can contain many elements ( same set of elements or different set of element)

'''
------------------------------------
creating list
------------------------------------
data types
integer     -------> example [10,20,30,40]
float/decimal --------> example 10.5, 89.5
character ------->  'e' 'n' 'g' 'l' 'i' 's' 'h'
string --------> example "English" , "maths"

'''
number = [1,2,3,4] # list hold integers
subjects = ["English","Maths","SC","Computer" ] # list holding strings
percentage = [86.5,98,66.4] # list holding floating values
character = ['a','b','c'] # list holding character

'''
--------------------------------
print list
--------------------------------
'''

print("Number list ",number)
print("Subject list",subjects)
print("Percentage list",percentage)
print("Character list", character)

'''
accessing element by element in list and printing list
for loop
'''

for val in subjects:
    print(val)

print("Percentage list",percentage)
for red in percentage:
    print(red)
Freinds=['Grady Holtkamp','Viggo Rouse','Carter Campbell']
print('Freinds',Freinds)
for blue in Freinds:
    print(blue)
