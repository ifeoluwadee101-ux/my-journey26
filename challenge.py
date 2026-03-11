#create a challenge app that collect info from users
#info includes :age,height,name,are you a student?,something with no value yet,a list of three bestfriends

age = input("enter your age: ")
height = input("enter your height: ")
name= input("enter your name: ")
are_you_a_student  = input("yes or no: ")
something_with_no_value_yet = input("")
a_list_of_three_bestfriends = input("list: ")

print()
print(f"i am {age} years old")
print(f"i am {height} feet")
print(f"my name is {name}")
print(f"am i a student {are_you_a_student}")
print(f"{something_with_no_value_yet}")
print(f"my bestfriends are {a_list_of_three_bestfriends}")