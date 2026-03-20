# Global Variables #

passmark = 50
bonusrate = 0.05


# Function Defintions #


def calculatebonus(mark):
    bonus = mark * bonusrate
    return bonus


def calculateaverage(marks):
    total = 0

    for m in marks:
        total = total + m

    return total / len(marks)


def determineresult(average):
    if average >= passmark and average <= 100:
        return "Pass"
    elif average > 100:
        return "Invalid"
    else:
        return "Fail"


# Main Program #

studentname = input("Enter student name: ")
numberofmarks = int(input("How many tasks? "))

marks = []

count = 0

while count < numberofmarks:
    mark = float(input("Enter grade as a percent: "))
    marks.append(mark)
    count += 1

average = calculateaverage(marks)
bonus = calculatebonus(average)

finalmark = min(average + bonus, 100)

result = determineresult(finalmark)

eligibleforaward = (finalmark >= 90 and result == "Pass") or not (finalmark < 50)

print(f"Student: {studentname}")
print(f"Average: {average}")
print(f"Bonus: {bonus}")
print(f"Finalmark: {finalmark}")
print(f"Result: {result}")
print(f"Award Eligible: {eligibleforaward}")
