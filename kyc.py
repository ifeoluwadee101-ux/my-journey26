
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
