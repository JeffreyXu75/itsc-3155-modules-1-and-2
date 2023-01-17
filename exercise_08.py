#Group: Sahiti Moduga, Cameron Wall, Jeffrey Xu
totalList = []
singleValue = []
for x in range(10):
    value = input("Enter a number " + str(x+1) + ": ")
    if value in totalList: 
        print("Value was found already")
        singleValue.remove(value)
    else:
        singleValue.append(value)
    totalList.append(value)
print(totalList)
print(singleValue)