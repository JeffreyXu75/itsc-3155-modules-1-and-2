#Group: Sahiti Moduga, Cameron Wall, Jeffrey Xu
my_list = []
even_list = []
valueone = ""
while (valueone.upper() != "QUIT"):
    print(valueone.upper())
    valueone = input("Enter a number or QUIT to quit: ")
    if (valueone.upper() != "QUIT"):
        my_list.append(int(valueone))
print(my_list)

for x in my_list:
    if (x%2 == 0):
        even_list.append(x)
print(even_list)