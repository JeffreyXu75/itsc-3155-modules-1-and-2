
string = input("Enter a string: ")
up = ""
low = ""
for i in string:
    if i.islower():
        low = low + i
    elif i.isupper():
        up = up + i

print(low+up)
