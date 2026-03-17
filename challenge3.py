dirty = "968-Maria, ( D@t@ Engineer );; 27y.."
clean = print(f" name:{dirty[4:9].lower()} | role:{dirty[12:26].lower().replace('@','a')} | age:{dirty[31:33]}")

print(clean)
print("*"*50)
print(dirty)
print("*"*50)

