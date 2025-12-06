# Lists, Tuples , Dictionaries, Sets in Python
print("************************** Lists in Python ************************** ")
#mutable sequence of values
my_list = [1, 2, 3, "99", "abc", 5.5]
print(my_list)  # Print the entire list
print(my_list[0])  # First element
print(my_list[-1])  # Last element
print(len(my_list))  # Length of the list

#List methods  append, insert, remove, pop, clear, index, count, sort, reverse


my_list.append(6)  # Append an element
print(my_list)
my_list.remove(3)  # Remove an element
print(my_list)
print(my_list[2:4])  # Slicing
my_list[0] = 1.0  # Modify an element
print(my_list)

my_list.insert(6, "7.5")  # Insert an element at index 6
print(my_list)

my_list.sort(key=str)  # Sort the list (convert all to string for comparison)
print(my_list)
my_list.sort(key=str, reverse=True)  # Sort the list in descending order
print(my_list)
my_list.reverse()  # Reverse the list
print(my_list)
my_list.sort(key=lambda x: str(x))  # Sort the list (convert all to str for comparison)
print(my_list)

print("*********************************************************************** ")


print("************************** Tuples in Python ************************** ")
#immutable sequence of values

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[:])  # Print the entire tuple           

#we cant create single element tuple like this my_tuple = (1) , it will be considered as integer
my_single_element_tuple = (1,)  # Correct way to create a single element tuple
print(my_single_element_tuple)

print(my_tuple[0])  # First element
print(my_tuple[-1])  # Last element
print(len(my_tuple))  # Length of the tuple
print(my_tuple[1:4])  # Slicing
#my_tuple[0] = 10  # This would raise an error, 'tuple' object does not support item assignment
print(my_tuple.index(3))  # Index of an element, returns 1st occurance of element
print(my_tuple.count(2))  # Count of an element , count total occurances of element

#tuple unpacking
a, b, c, d, e = my_tuple
print(a, b, c, d, e)
print(a); #print(b); #printing multiple variables in new lines


#swapping values using tuple unpacking
x = 10
y = 20
x, y = y, x
print(x, y) 

#tuple methods are limited as tuples are immutable 

print("*********************************************************************** ")

print("************************** Dictionaries in Python ************************** ")
#key-value pairs, unordered, mutable
my_dict = {"name": "John", "age": 25, "city": "New York"}
print(my_dict)  # Print the entire dictionary
print(my_dict["name"])  # Access value by key
print(len(my_dict))  # Length of the dictionary
my_dict["age"] = 26  # Modify value
print(my_dict)
my_dict["country"] = "USA"  # Add new key-value pair
print(my_dict)
del my_dict["city"]  # Remove key-value pair
print(my_dict)
print(my_dict.keys())  # Get all keys
print(my_dict.values())  # Get all values
print(my_dict.items())  # Get all key-value pairs       
print(my_dict.get("name"))  # Access value by key using get() method
print(my_dict.get("city", "Not Found"))  # Access non-existing key with default value
print(my_dict.pop("age"))  # Remove key-value pair and return value
print(my_dict)
#my_dict.clear()  # Clear the dictionary

print(type(list(my_dict.keys())))  # Get all keys

my_dict.update({"age": 30, "city": "Los Angeles"})  # Update multiple key-value pairs
print(my_dict)
print("*********************************************************************** ")

print("************************** Sets in Python ************************** ")
#unordered collection of unique elements , Sets are mutable but elements are immutable , sets are unordered , so we cant access elements using index
my_set = {1, 2, 3, 4, 5, 2, 3}  # Duplicates will be ignored
print(my_set)  # Print the entire set
my_set.add(6)  # Add an element
#print(my_set[0])  # This would raise an error, 'set' object is not subscriptable
my_set.remove(2)  # Remove an element
print(my_set)
print(len(my_set))  # Length of the set     
my_set.discard(10)  # Remove an element if it exists, does nothing if it doesn't
print(my_set)
my_set.pop()  # Remove and return an arbitrary element
print(my_set)
my_set.add(3)  # Adding existing element does nothing
print(my_set)   
print(3 in my_set)  # Check membership
print(10 in my_set)  # Check membership 

#my_set[0] = 10  # This would raise an error, 'set' object does not support item assignment

empty_set = set()  # Creating an empty set
print(type(empty_set))  # <class 'set'>

empty_set = {}  # This creates an empty dictionary, not a set
print(type(empty_set))  # <class 'dict'>


my_set2 = {4, 5, 6, 7, 8}
print(my_set.union(my_set2))  # Union
print(my_set.intersection(my_set2))  # Intersection
print(my_set.difference(my_set2))  # Difference
print(my_set.symmetric_difference(my_set2))  # Symmetric Difference
print(my_set.issubset({1, 3, 4, 5, 6}))  # Subset
print(my_set.issuperset({1, 3, 4}))  # Superset
print(my_set.isdisjoint({7, 8, 9}))  # Disjoint

# Given a list of tuples with info(name,subject),
list = [("Alice", "Math"), ("Bob", "Math"), ("Alice", "Science"), ("Bob", "Science")]

list = [
    ("Alice", "Math"),
    ("Bob", "Math"),
    ("Alice", "Science"),
    ("Bob", "Science"),
    ("Charlie", "Math"),
    ("Charlie", "History"),
]

#List all unique courses
courses = set()
for entry in list:
    courses.add(entry[1])
print("Courses:", courses)
# list students enrolled in each course
course_students = {}    
for entry in list:
    name, subject = entry
    if subject not in course_students:
        course_students[subject] = set()
    course_students[subject].add(name)
print("Course Students:", course_students)

#create dictionary (student, set of subjects)
student_courses = {}
for entry in list:
    name, subject = entry
    if name not in student_courses:
        student_courses[name] = set()
    student_courses[name].add(subject)
print("Student Courses:", student_courses)

dict = {}
for name, course in list:
    if(dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print("Dictionary:", dict)
print("*********************************************************************** ")