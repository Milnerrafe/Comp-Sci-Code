totalscore = 0
continuevar = "Y"

while continuevar == "Y":
    score = int(input("Plese enter Score: "))
    totalscore = totalscore + score

    continuevar = input("Would you like to continue? Enter Y or N: ")

print(totalscore)
