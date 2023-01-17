#Group: Sahiti Moduga, Cameron Wall, Jeffrey Xu

grade = int(input("Enter a grade from 0 to 100: "))
if grade < 60:
    letter = "F"
elif grade < 70:
    letter = "D"
elif grade < 80:
    letter = "C"
elif grade < 90:
    letter = "B"
elif grade <= 100:
    letter = "A"
print("Your grade is " + letter)
