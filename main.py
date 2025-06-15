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

#! -------------- List --------------
'''
fruitsList=["apple", "banana", "cherry"]
moreFruitsList=["orange", "grape"]

print(fruitsList)
print(fruitsList[0]) # get an element from the list
print(fruitsList.append("orange")) # add an element to the end of the list
print(fruitsList.remove("apple")) # remove an element from the list
print(fruitsList.index("banana")) # get the index of an element in the list
print(fruitsList.insert(1, "kiwi")) # insert an element at a specific index in the list
print(fruitsList.pop(1)) # remove an element at a specific index in the list
print(fruitsList.extend(moreFruitsList)) # add multiple list elements to the end of the list
print(fruitsList.count("apple")) # count the number of times an element appears in the list
print(fruitsList.sort()) # sort the list in ascending order
print(fruitsList.reverse()) # reverse the order of the list
print(fruitsList.copy()) # copy the list
print(len(fruitsList)) # get the length of the list
print(fruitsList.clear()) # remove all elements from the list

print(fruitsList[0:2]) # get a slice of the list
print(fruitsList[:2]) # get a slice of the list
print(fruitsList[2:]) # get a slice of the list
print(fruitsList[-2:]) # get a slice of the list
'''
#! -------------- List end ------------

#! -------------- Tuples --------------
'''
fruitsTuple=("apple", "banana", "cherry")
print(fruitsTuple)
print(fruitsTuple[0]) # get an element from the tuple
print(len(fruitsTuple)) # get the length of the tuple
print(fruitsTuple.count("apple")) # count the number of times an element appears in the tuple
print(fruitsTuple.index("banana")) # get the index of an element in the tuple

# fruitsList=list(fruitsTuple) # convert a tuple to a list
# fruitsTuple=tuple(fruitsList) # convert a list to a tuple

print(fruitsTuple[1:3]) # get a slice of the tuple
'''
#! -------------- Tuples end ------------

#! -------------- Sets --------------
'''
fruitsSet={"apple", "banana", "cherry"}
# print(fruitsSet)
# print(fruitsSet.add("orange")) # add an element to the set
# print(fruitsSet.remove("apple")) # remove an element from the set
# print(fruitsSet.update({"orange", "grape"})) # add multiple set elements to the set
print(fruitsSet.update(["orange", "grape"])) # add multiple set elements to the set
print(fruitsSet)
# print(fruitsSet.clear()) # remove all elements from the set

set1={1, 2, 3}
set2={3, 4, 5}
result=set1.union(set2) # get the union of two sets
print(result)
result=set1.intersection(set2) # get the intersection of two sets
print(result)
result=set1.difference(set2) # get the difference of two sets
print(result)
result=set1.symmetric_difference(set2) # get the symmetric difference of two sets
print(result)
result=set1.issubset(set2) # check if one set is a subset of another set
print(result)
result=set1.issuperset(set2) # check if one set is a superset of another set
print(result)
'''
#! -------------- Sets end ------------

#! -------------- Dictionary ------------
'''
person={
    "name":"John",
    "age":30,
    "city":"New York",
    "country":"USA"
}

print(person)
print(person["name"])
print(person.get("age"))
print(person.keys()) # get the keys of the dictionary
print(person.values()) # get the values of the dictionary
print(person.items()) # get the key-value pairs of the dictionary
print(person.pop("name")) # remove a key-value pair from the dictionary and return the value

person["name"]="Jane" # update a key-value pair in the dictionary
person.update({"age":31, "city":"Los Angeles"}) # update multiple key-value pairs in the dictionary

# print(person.clear()) # remove all key-value pairs from the dictionary
print(person)
'''
#! -------------- Dictionary end ------------

#! -------------- Functions ------------
'''
def say_hello(name):
    print("Hello " +  name) 

say_hello("Jebal")

def add_numbers(*numbers): # *args this is a tuple
    total=0
    for num in numbers:
        total+=num
    return total

    # print(numbers)

print(add_numbers(1,2,3,4,5))
# add_numbers(50, 100, 150, "hello", "world", True)
    
def introduce(**person): # **kwargs this is a dictionary
    print(person)
    print(person["name"])
    for key, value in person.items():
        print(key + ": " + str(value))

introduce(
    name="Jebal", 
    age=20,
    city="Dhaka"
)

def add_two(a, b):
    return a + b

result=add_two(1, 2) # when a function returns a value, it becomes equivalent to that returned value and we can store it in a variable
print(result)


def add_multiple(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    # return sum, sub, mul, div # this will return as a tuple
    # return [sum, sub, mul, div] # this will return as a list
    return {"sum":sum, "sub":sub, "mul":mul, "div":div} # this will return as a dictionary

result2=add_multiple(1, 2)
print(result2)

# result3=lambda: 2+2
result3=lambda x,y: x+y
print(result3(10, 20))


#todo variable scope
x=10 # global variable
def myFun():
    x=10 # local variable
    y=20
    print(x+y)
myFun()
print(x)
'''
#! -------------- Functions end ------------

#! -------------- File ------------
'''
#todo Create
with open("example.text", "w") as file:
    print("file created")
    #todo write a string to the file
    file.write("Hello World") 

with open("example.text", "r") as file:
    #todo read the file
    content=file.read()
    print(content)
    
import os

# #todo rename the file
# os.rename("example.text", "example2.text")

#todo delete the file
os.remove("example.text")
'''
#! -------------- File end ------------

#! -------------- Directory ------------
'''
import os

#todo create a directory
# os.mkdir("new")

#todo read a directory
# fileList=os.listdir("new")
# print(fileList)

# for file in fileList:
#     print(file)

#todo write a file to the directory
# with open("new/text.txt", "w") as file:
#     file.write("Hello World")

#todo rename a directory
# os.rename("new", "new_directory")

#todo delete a file
# os.remove("new_directory/text.txt")

#todo remove a directory
# os.rmdir("new_directory")

'''
#! -------------- Directory end ------------

#! -------------- Zip files ------------
'''
import zipfile

#todo create a zip file
# with zipfile.ZipFile("new.zip","w") as zip:
#     print("zip file created")
#     zip.write("demo1.txt")
#     zip.write("demo2.txt")

#todo Extract from a zip file
# with zipfile.ZipFile("new.zip", "r") as zip:
#     print("zip file extracted")
#     zip.extractall()
#     extracted_files=zip.namelist()
#     print(extracted_files)

#todo make zip from a directory
# import shutil
# shutil.make_archive("new_zip", "zip", "new")
'''
#! -------------- Zip files end ------------

#! -------------- CSV files ------------
'''
import csv

#todo create a csv file
# data=[
#     ["name", "age", "city"],
#     ["Jebal", 20, "Dhaka"],
#     ["John", 30, "New York"],
#     ["Jane", 25, "London"]
# ]

# with open("new.csv", "w") as file:
#     csv_file=csv.writer(file)
#     csv_file.writerows(data)
#     print("csv file created")
    
#todo read a csv file
data=[]
with open("new.csv", "r") as file:
    content=csv.reader(file)
    print(content)
    for row in content:
        # print(row)
        data.append(row)
        print(data)
'''
#! -------------- CSV files end ------------

#! -------------- Exceptions and Error handling (try-except) ------------
'''
#todo simple/single error
try:
    result=10/0
    print(result)
except ZeroDivisionError:
    print(ZeroDivisionError)

#todo multiple error
try:
    with open("neww.txt", "r") as file:
        content=file.read() # this will throw an error
        result=10/int(content) # this will throw an error
        print(result) # this will throw an error
except FileNotFoundError:
    print(FileNotFoundError)
except ValueError:
    print(ValueError)
except ZeroDivisionError:
    print(ZeroDivisionError)
except TypeError:
    print(TypeError)

try:
     with open("neww.txt", "r") as file:
        content=file.read() # this will throw an error
        result=10/int(content) # this will throw an error
        print(result) # this will throw an error
except Exception as e:
    print(e)
'''
#! -------------- Exceptions and Error handling (try-except) end ------------

#! -------------- Exceptions and Error handling (finally) ------------
'''
#todo simple/single error 
try:
    result=10/0
    print(result)
except ZeroDivisionError:
    print(ZeroDivisionError)
finally:
    print("finally block")

#todo multiple error
try:
    with open("neww.txt", "r") as file:
        content=file.read() # this will throw an error
        result=10/int(content) # this will throw an error
        print(result) # this will throw an error
except Exception as e:
    print(e)
finally:
    print("finally block")
'''
#! -------------- Exceptions and Error handling (finally) end ------------

#! -------------- JSON ------------
'''
import json

#todo python objet --> json string
# personOBJ={"name": "Jebal", "age": 20, "city": "Dhaka", "titles": ["Engineer", "Developer"]}
# personJSON=json.dumps(personOBJ, indent=4)
# print(personJSON)


#todo json string --> python objet
# personJSON='{"name": "Jebal", "age": 20, "city": "Dhaka", "titles": ["Engineer", "Developer"]}'
# personOBJ=json.loads(personJSON)
# print(personOBJ)


#todo python objet --> json string --> File write
# personOBJ={"name": "Jebal", "age": 20, "city": "Dhaka", "titles": ["Engineer", "Developer"]}
# with open("person.json", "w") as personJSONFile:
#     json.dump(personOBJ, personJSONFile, indent=4)
#     print("json file created")

#todo JSON File read --> python object --> JSON String
with open ("person.json", "r") as personOBJFile:
    personOBJ=json.load(personOBJFile)
    print(personOBJ)
    personJSON=json.dumps(personOBJ, indent=4)
    print(personJSON)

'''
#! -------------- JSON end ------------

#! -------------- Date and Time ------------
'''
import datetime

#todo current date and time
now=datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
print(now.date())
print(now.time())
print(now.weekday())
print(now.timestamp())

# YYYY-MM-DD, YYYY-DD-MM, DD/MM/YYYY, MM/DD/YYYY

# formatted_datetime=now.strftime("%d/%m/%y")
formatted_datetime=now.strftime("%d/%m/%y %H:%M:%S")
print(formatted_datetime)

#todo calculating date time difference
date1= datetime.datetime(2024, 9, 1)
date2= datetime.datetime(2023, 9, 1)

difference=date1 - date2
print(difference)

new_date=date1+datetime.timedelta(days=10)
print(new_date)
'''
#! -------------- Date and Time end ------------

#! -------------- OOP ------------
#todo create a class
class MyClass:
    x=10 # class variable
    y=30
    z=40
    def addTwo(self, a, b): # class method
        sum=self.x + self.y + self.z + a + b
        print(sum)
    def addNew(self):
        self.addTwo(500, 100)

#todo create an object
obj1=MyClass() # this will create an object of MyClass class
print(obj1.x)
obj1.addTwo(5, 10)
obj1.addNew()

#todo create constructor
class MyClass2:
    x=10
    y=30

    #? constructor method it will be called automatically and doesn't return any value
    # def __init__(self, a, b):
    #     sum=self.x + self.y + a + b
    #     print(sum)

    def __init__(self, z, x):
        self.z = z # instance variable
        self.x = x # instance variable and it will change the value of x variable
    
    def addTwo(self): # instance method
        print(self.x + self.y + self.z)
        
obj2=MyClass2(50, 100)
print(obj2.z)
print(obj2.x)
obj2.addTwo()
#! -------------- OOP end ------------