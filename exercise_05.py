#Group: Sahiti Moduga, Cameron Wall, Jeffrey Xu
mylist = []

for i in range(5):
    x = input("Enter a number: ")
    x = int(x)
    mylist.append(x)


mylist2 = []

for i in range(5):
    n = input("Enter another number: ")
    n = int(n)
    mylist2.append(n)

common = list(set(mylist) & set(mylist2))

print("First List: ", mylist)
print("Second List: ", mylist2)
print("Common List: ", common)
