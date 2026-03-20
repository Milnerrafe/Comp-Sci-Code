


print("Hello, welcome to Marks Book")

count = 0

studentName = input("What is the name of the student: ")

marks = []

runstillone = True

while runstillone:
    count += 1

    runstilltwo  = True

    

    while runstilltwo:

        try:

           inputnumber = int(input(f"Enter Marks for test {count}: "))

           if inputnumber > 0 and inputnumber < 100:

               marks.append(inputnumber)
               runstilltwo = False

           else:
               print("Make sure the number is bewteen 1 and 100")


        except ValueError:

            print("That is not a number, enter a number beween 1 and 100")
        


        
    if count >= 5:
        runstillone = False



asum = 0
avgrage = 0

for i in marks:
    asum += i

average = asum/len(marks)


grade = ""

if average < 50:
    
    grade = "E"

elif average > 50 and average < 59:

    grade = "D"

elif average > 60 and average < 69:

    grade = "C"

elif average > 70 and average < 79:

    grade = "B"

elif average > 80:

    grade = "A"



print("\n")
print("\n")
print("\n")

print(f"Student Name: {studentName}")
print("----------------------------")
print(f"Average Score: {average}")
print("----------------------------")
print(f"Letter Grade: {grade}")














    
    
