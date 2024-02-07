correct_guess = 7
limit = 3
i = 1
while i <= limit:
    enter_value = int(input("Enter Number 0 To 9 "))
    i += 1
    if enter_value == correct_guess:
        print("Your Guess correct You won ")
        break
else:
    print("Sorry ,You Are reached Your Limit")
