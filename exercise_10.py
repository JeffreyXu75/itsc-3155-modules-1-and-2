#Group: Sahiti Moduga, Cameron Wall, Jeffrey Xu

string = input("Enter a string: ")

largelist = []
for i in range(0, len(string)):
    largelist.append(string[i])

list = []
x=0
for i in range(0,len(largelist),3):
    smalllist = []
    if i+3 <= len(largelist):
        for j in range(i, i+3):
            smalllist.append(largelist[j])
        list.append(smalllist)
rem = len(largelist) % 3
if rem != 0:
    smalllist = []
    for i in range(len(largelist)-rem, len(largelist)):
        smalllist.append(largelist[i])
    list.append(smalllist)
print(list)