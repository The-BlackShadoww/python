#Python """

#! -------------- Variables --------------
# total_cost=100
#! -------------- Variables end -----------------

#! -------------- Data types --------------
"""
name='John' # String
age=25 # Integer
is_student=True # Boolean
height=1.75 # Float
friends=['Alice', 'Bob', 'Charlie'] # List
address={'street': '123 Main St', 'city': 'New York', 'state': 'NY'} # Dictionary / map
latter=('a', 'b', 'c') # Tuple
numbers=range(0, 10) # Range
numbers2=range(0, 10, 2) # Range
numbers3=range(5) # Range
taka=None # None
#todo { set is unordered and unindexed } 
unique_numbers=set([1, 2, 3, 4, 5]) # Set - must be unique and mutable
unique_numbers2={1, 2, 3, 4, 5, 5, 2, 1} # Set - must be unique and mutable
unique_numbers3=frozenset([1, 2, 3, 4, 5, 5, 2, 1]) # Frozen set - must be unique and immutable

# Print the data types
print(type(name)) # Output: <class 'str'>
print(type(age)) # Output: <class 'int'>
print(type(is_student)) # Output: <class 'bool'>
print(type(height)) # Output: <class 'float'>
print(type(friends)) # Output: <class 'list'>
print(type(address)) # Output: <class 'dict'>
print(type(latter)) # Output: <class 'tuple'>
print(*numbers)
print(*numbers2)
print(*numbers3)
print(type(taka)) # Output: <class 'NoneType'>
print(address['street']) # Output: 123 Main St
print(unique_numbers)
print(unique_numbers2)
print(unique_numbers3)
"""
#! -------------- Data types end -------------

#! -------------- Immutability of data types --------------
"""
# a=5
# a=3.14
# a="Hello"
# a=(1, 2, 3)
a=frozenset([1, 2, 3])
first_location=id(a)

# a=6
# a=2.15
# a="World"
# a=(1, 2, 3, 4, 5)
a=frozenset([1, 2, 3])
second_location=id(a)

print(first_location)
print(second_location)
print(first_location==second_location)
"""
#! -------------- Immutability of data types end ------------

#! -------------- Mutability of data types --------------
"""
# l=[1, 2, 3]
# l={"a":1, "b":2, "c":3}
l={1, 2, 3}
first_location=id(l)

# l.append(4)
# l[1]=5
# l['a']=5
l.add(4)
second_location=id(l)

print(l)
print(first_location)
print(second_location)
print(first_location==second_location)
"""
#! -------------- Mutability of data types end ------------

#! -------------- Type conversions --------------
"""
x="123"
j=123
y=int(x)
z=float(x)
a=str(j)
# s=set(j) # j is a number so it can not be converted to set
# name="jebal"
# name_init=int(name) 

# try:
#     name="jebal" # this string can not be converted to int
#     name_init=int(name) 
# except Exception as e:
#     print(e)

print(x)
print(y)
print(z)
print(type(a))
"""
#! -------------- Type conversions end ------------

#! -------------- console projects --------------
"""
#greeting program
name=input("Enter your name: ") 
print("Hello "+ name + " !")

# addition program
num1=int(input("Enter first number: ")) # input always return string
num2=int(input("Enter second number: "))
print(num1+num2)

# temperature program
celsius=int(input("Enter temperature in celsius: "))
celsius=float(celsius)
fahrenheit=(celsius*1.8)+32
print("Temperature in fahrenheit: "+ str(fahrenheit))

# interest program
principle=float(input("Enter principle amount: "))
rate=float(input("Enter rate: "))
time=float(input("Enter time: "))

interest=(principle*rate*time)/100
print("Interest is: "+ str(interest))
"""
#! -------------- console projects end ------------

#! -------------- String Slicing --------------
"""
text="Hello World"
print(text[0:5]) # Hello
print(text[6:]) # World
print(text[:5]) # Hello
print(text[-5:]) # World
print(text[0::2]) # HloWrd
print(text[::-1]) # dlroW olleH
"""
#! -------------- String Slicing end ------------

#! -------------- String Repetition --------------
'''
name="Jebal "
print(name*3)
'''
#! -------------- String Repetition end ------------

#! -------------- String concatenation --------------
'''
name="Jebal"
print("Hello "+ name)

combined="".join(["Hello", " ", name])
print(combined)

# formatted_string=f"Hello {name}"
# formatted_string="{} {} !".format("Hello", name)
formatted_string="%s %s"%("Hello", name)
print(formatted_string)
'''
#! -------------- String concatenation end ------------

#! -------------- String Methods --------------
'''
text="Hello World"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())
print(text.replace("World", "Universe"))
print(text.split(" "))
print(text.strip())
print(text.lstrip())
print(text.rstrip())
'''
#! -------------- String Methods end ------------

#! -------------- String Methods for checking and counting --------------
'''
text="Hello World"

print(text.startswith("Hello"))
print(text.endswith("World"))
print(text.count("l"))
print(text.find("l"))
print(text.index("l"))
print(text.isalnum())
print(text.isalpha())
print(text.isdigit())
print(text.isspace())
print(text.istitle())
'''
#! -------------- String Methods for checking and counting end ------------

#! -------------- Numbers and Math --------------
"""
a=10
b=3
c=3.14

print(a+b) # addition
print(a-b) # subtraction
print(a*b) # multiplication
print(a/b) # division
print(a%b) # modulus
print(a//b) # floor division
print(a**b) # a to the power of b
"""
#! -------------- Numbers and Math end ------------

#! -------------- Numbers and Math Type conversion --------------
"""
x=10
y=3.14

print("Int to Float: ", float(x))
print("Float to Int: ", int(y))
print("Complex: ", complex(x))
print("Complex: ", complex(x, y))
"""
#! -------------- Numbers and Math Type conversion end ------------

#! -------------- Math --------------
'''
import math
x=10
y=5

# Basic math
print("Square Root: ", math.sqrt(x))
print("Power: ", math.pow(x, y))
print("Floor: ", math.floor(x))
print("Ceil: ", math.ceil(x))
print("Absolute value: ", math.fabs(x))
print("Factorial: ", math.factorial(x))
# GCD and LCM
print("GCD: ", math.gcd(x, y))
print("LCM: ", math.lcm(x, y))
# Logarithmic functions
print("Log: ", math.log(x))
print("Log10: ", math.log10(x))
# Trigonometric functions
print(math.sin(math.radians(90))) 
print(math.cos(math.radians(90))) 
print(math.tan(math.radians(90))) 
print(math.sinh(math.radians(90))) 
print(math.cosh(math.radians(90))) 
print(math.tanh(math.radians(90)))
# constants
print("Pi: ", math.pi)
print("E: ", math.e)
'''
#! -------------- Math end ------------

#! -------------- Math Operator Precedence --------------
'''
# PEMDAS
# Parentheses, Exponents, Multiplication, Division, Addition, Subtraction

# result=(2+3)*4
result=2+3*4
print(result)
'''
#! -------------- Math Operator Precedence end ------------

#! -------------- Control Flow --------------
'''
#todo if, elif, else
# age=70
# if age >= 18:
#     print("You are an adult")
#     if age >= 65:
#         print("You are a senior")
# elif age < 18:
#     print("You are a minor")
# else:
#     print("You are an adult")

# Ternary operator
# print("You are an adult" if age >= 18 else "You are a minor")

#todo for loop
# fruitsList=["apple", "banana", "cherry"]
# for eachFruit in fruitsList:
#     print(eachFruit)

# word="Hello" 
# for eachLetter in word:
#     print(eachLetter)

# range(0, 10)
# for eachNumber in range(0, 100): # 0 to 99
#     print(eachNumber)

# marks={"English": 90, "Math": 80, "Science": 70} # dictionary
# # for eachSubject in marks:
# #     print(eachSubject)

# for subject,marks in marks.items():
#     print(subject, marks)

# uniq_numbers={1, 2, 3, 4, 5} # set
# for eachNumber in uniq_numbers:
#     print(eachNumber)

# for num in range(10):
#     if num == 5:
#         # break # break the loop
#         continue # it will skip the current iteration
#     print(num)

#todo while loop
# starting point, ending point condition, increment/decrement

# List
# fruitsList=["apple", "banana", "cherry"]
# index=0
# while index < len(fruitsList):
#     print(fruitsList[index])
#     index+=1

# # String
# word="Hello"
# while index < len(word):
#     print(word[index])
#     index+=1

# # break and continue
# index2=0
# end=10
# while index2 < end:
#     if index2 == 5:
#         # break
#         index2+=1 # Increment index to avoid infinite loop
#         continue
#     print(index2)
#     index2+=1

# # dictionary
# examResult={"English": 90, "Math": 80, "Science": 70}
# keys=list(examResult.keys()) # list of keys
# values=list(examResult.values()) # list of values

# index3=0
# while index3 < len(keys):
#     print(keys[index3], values[index3])
#     index3+=1

# # set
# my_set= {1, 2, 3, 4, 5} 
# my_set_list=list(my_set)

# index4=0
# while index4 < len(my_set_list):
#     print(my_set_list[index4])
#     index4+=1


#todo Logical Operators
# and, or, not

# age=20
# has_permission=True
# is_vip=False

# if age >= 18 or has_permission:
#     print("You are an adult and have permission")
# else:
#     print("You are not an adult")

# if age>18 and has_permission and not is_vip:
#     print("You are an adult and have permission and not a VIP")
# else:
#     print("You are not an adult")
'''
#! -------------- Control Flow end ------------

