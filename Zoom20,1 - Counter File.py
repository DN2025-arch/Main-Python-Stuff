

file_path = r"C:\Users\flori\OneDrive\Desktop\Python\CounterFile.txt"


file= open(file_path, "r")

content = file.read().split()
#print(content)
print(f"WORD COUNT: {len(content)}")

file.close()


# seek function: change filepointer position
# tell function: say    filepointer position


file= open(file_path, "r")

content = file.read()

digits = 0
uppercases = 0
lowercases = 0
special = 0
for i in content:
    if i.isdigit():
        digits += 1
    elif i.isupper():
        uppercases += 1
    elif i.islower():
        lowercases += 1
    elif not i.isalnum(): # alnum: if alphabet or number
        special += 1
##    else:
##        special += 1

print(f"UPPERCASE LETTERS: {uppercases}")
print(f"LOWERCASE LETTERS: {lowercases}")
print(f"NUMBERS: {digits}")
print(f"SPECIAL: {special}")

file.close()


file= open(file_path, "r")

content = file.readlines()
print(f"LINES: {len(content)}")

file.close()
