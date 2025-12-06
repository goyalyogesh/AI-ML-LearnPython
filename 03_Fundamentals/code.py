print("************************** Strings in Python ************************** ") 

word = "python3"

# word is immutable, so we create a new string by concatenation
# word[2] = 't'  # This would raise an error, 'str' object does not support item assignment
#word += " is fun"  # Concatenate
print(word) 
print(word[0])  # First character
print(word[-1])  # Last character
print(len(word)) # Length of the string
print(word[2:5]) # Slicing, starting index is inclusive, ending index is exclusive and default value of starting index is 0 and ending index is length of string
print(word[-5:-2]) # Negative indexing in slicing
print(word[::2]) # Slicing with step
print(word[::-1]) # Reversing a string using slicing
print(word.lower())  # Lowercase
print(word.upper())  # Uppercase
print(word.replace("fun", "awesome"))  # Replace substring
print(word[:])  # Full string


#string formatting
name = "Alice"
age = 30
height = 5.5       
print("My name is {}. I am {} years old and my height is {} feet.".format(name, age, height)) # .format() method in python3
print(f"My name is {name}. I am {age} years old and my height is {height} feet.")  # f-string formatting version in python3.6 and above, literal string interpolation

#index based string formatting and value based string formatting
print("My name is {0}. I am {1} years old and my height is {2} feet.".format(name, age, height)) 
print("My name is {name}. I am {age} years old and my height is {height} feet.".format(name=name, age=age, height=height))

a =5
b =10
print(f"The sum of {a} and {b} is {a + b}.")


print("*********************************************************************** ") 