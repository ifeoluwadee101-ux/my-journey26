<<<<<<< HEAD
#print("customer profile")
#print("my name is mitchell")
#print("my surname is king")
#print("my gender is female")
#print("i am 25 years old")
#print("i am from kogi state")
#print("i am a doctor")

("customer profile:")
name = input(" name: ")
surname = input("surname: ")
gender = input("sex: ")
age = input("age: ")
state = input("state of origin: ")
occupation = input("occupation: ")
print("customer profile")
print("my name is",name)
print("my surname is",surname)
print("my gender is",gender)
print("i am",age,"years old")
print("i am from",state,"state")
print("i am a",occupation)
=======
#create a kyc app that collect info from users
#info includes :name,surname,age,gender,state of origin,occupation,tribe

name = input("enter your first name: ")
surname = input("enter your surname: ")
age = input("enter your age: ")
gender  = input("are you male or female: ")
state = input("enter your state of origin: ")
occupation = input("what is occupation: ")
tribe = input("what nigerian tribe are you from: ")
print()
# print("customer profile:\n\t")
# print("\tfull name -",name,surname)
# print("\tage -",age)
# print("\tgender -",gender)
# print("\tstate of origin -",state)
# print("\toccupation -",occupation)
# print("\ttribe -",tribe)
print(f""" customer profile:\n\t
            ->full name: {name} {surname}\t
            ->age: {age}\t
            ->gender: {gender}\t
            ->occupation: {occupation}\t
            ->tribe:{tribe}\t
      """)
>>>>>>> staging
