print("Hello world","with python") 

# python3 01_Fundamentals/code.py
# Indentation is important in python
# python is case sensitive language
# python is dynamically typed language


name = "yogesh";
age= 30
print("Hello",name, age-5)


#Data Types in python - Int, Float, String, Boolean, NoneType
a = 10          # Int
b = 10.5        # Float
c = "Yogesh"    # String
d = True        # Boolean
e = None        # NoneType  

print(type(a))  #<class 'int'>
print(type(b))  #<class 'float'>         
print(type(c))  #<class 'str'>
print(type(d))  #<class 'bool'>
print(type(e))  #<class 'NoneType'>

print(not(a < b))  # False

ans1 = int(5 + 10.5)  # Type casting float to int
ans2 = 5 + 10.5          # No type casting, ans2 will be float
print(ans1)          # 15
print(ans2)         # 15.5

val = bool(10)   # Type casting int to boolean
print(val)      # True


name = input("Enter your name: ")  # Input from user , bydefault input is string
print("Hello", name)

#sum of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("Sum:", sum)





