#python challenge
#create 5 variables -each with a different data type
age = 19
height = 3.25
name = "dee"
is_student = True
eaten = None
name_of_friends = ["dee", "loviee", "marvel"]

print(f"i am {age} years old")
print(f"age is a {type(age)} data type")
print(f"my age contains {age.bit_length()} bits")
print()
print(f"my height is {height} meters")
print(f"height is a {type(height)} data type")
print(f"my height contains{height.hex()} bits")
print()
print(f"my name is {name}")
print(f"name is a {type(name)} data type")
print(f"my name contains{len(name)} characters")
print()
print(f"i am a student: {is_student}")
print(f"is_student is a {type(is_student)} data type")
print()
print(f"i have eaten: {eaten} today")
print(F"eaten is a {type(eaten)} data type")
print()
print(f"my friends are {name_of_friends}")
print(f"name of friends is{type(name_of_friends)} data type")
print(f"my name_of_friends contain {len(name_of_friends)} item")
