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

print("***************************")
i = (6); #iterator
while(i <= 10):
    print(i)
    i += 1
print("value of counter after while loop is :", i)
print("***************************")
j = 10; #iterator
for j in range(5):
    print(j)  
print("value of counter after for loop is :", j)
print("***************************")
for k in range(2, 10, 2): # start, end, step
    print(k)
print("***************************")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print("***************************")
for fruit in fruits:
    if(fruit == "banana"):
        continue
    print(fruit)
print("***************************")
for fruit in fruits:
    if(fruit == "banana"):
        break
    print(fruit)

    
print("***************************")