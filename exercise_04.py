#Group: Sahiti Moduga, Cameron Wall, Jeffrey Xu
n = input("Enter a number: ")
n = int(n)

mylist = []

for i in range(n): 
    x = input ("Enter a float: ")
    x = float(x)
    mylist.append(x)

print("List: ", mylist)

mean = sum(mylist) / n
print("Average: ", mean)
