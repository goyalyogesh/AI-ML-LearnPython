print("***************************")
age =13
if(age > 18):
    print("child")
    print("You cant drive.")
elif(age >= 13 and age <= 19):
    print("teenager")
else:
    print("adult")
print("***************************")
color = "red"
match color:
    case "red":
        print("The color is red")
    case "blue":
        print("The color is blue")
    case "green":
        print("The color is green")
    case _:
        print("Unknown color")

print("********** while loop*****************")

i = (6); #iterator
while(i <= 10):
    print(i)
    i += 1
print("value of counter after while loop is :", i)

print("*********range function******************")

for j in range(5): # 0 to n-1 numbers
    print(j)  
print("value of counter after for loop is :", j)

word = "artificial intelligence"

ans = 0 
for letter in word:
    if letter == 'i':
        ans += 1
print("Number of i's in the word is :", ans)

print("***********Range start end step****************")

for k in range(2, 10, 2): # start, end, step - start and step are optional
    print(k)

print("*********break continue******************")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


for fruit in fruits:
    if(fruit == "banana"):
        continue
    print(fruit)


for fruit in fruits:
    if(fruit == "banana"):
        break
    print(fruit)


print("***********For loop ****************")

hello = str("Hello");

for char in hello: # in is membership operator
    print(char)

if 'H' in hello:
    print("H is present in hello")

sum =0 
for num in range(1, 7): # 1 to 6
    sum += num
print("Sum from 1 to 6 is :", sum)

print("**********Function *****************") # block of code which performs a specific task

def greet(name):
    return "Hello " + name  
print(greet("Yogesh")) # function call

print("************Function Sum***************")

def add(a, b=1): #parameters
    return a + b
result = add(5,10)
print("Sum is:", result)

print("************Factorial***************")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)             
print("Factorial of 5 is:", factorial(5))

def calc_factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact
print("Factorial of 6 is:", calc_factorial(6))

print("**********Outer Function*****************")

def outer_function():
    def inner_function():
        return "Hello from inner function"
    return inner_function()
print(outer_function())

print("*************Lambda Function**************")

lambda_add = lambda x, y: x + y # high order function
print("Sum using lambda:", lambda_add(5, 10))

lambda_square = lambda x: x * x
print("Square using lambda:", lambda_square(6))

print("***************************")