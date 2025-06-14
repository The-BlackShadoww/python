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