name = "dee"
surname = "ifeoluwa"
age = 21

#print("my name is",name,"i am","years old")
print(name+' '+str(age))

isstudent = False
print(f"{{isstudent}}  variable contains {len(str(isstudent))} characters")

# math string operation
sentence = """i love Python.
Python is very easy, Python is also very
powerful. AI depends mostly on Python.
Python can be used for.
- AI
- Web Design
- Automations
python is a highly versatile language
 """

#print(sentence)

print(f" The word 'python' occurs {sentence.count('python')} times in the above sentence.")