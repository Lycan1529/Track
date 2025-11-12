#first declarations of var e.g.: budget, expanses and so on

#thne definitions of functions e.g.: add_expense(), view_budget(), etc
income = float(input("Enter your total income: "))
inputbudget = input("Enter you r total budget: ")


#we want to have validation for the input values and error handling, and storing them in a file



expenses2 = float(input("Enter an expense amount (or 0 to finish): "))
if expenses2 == 0:
        break
    expenses += expenses2
    budget = inputbudget - expenses
    print("You have", budget, "left in your budget.")

# Ask for the total budget
inputbudget = float(input("Enter your total budget: "))

# Start with 0 expenses
expenses = 0

# Loop while total expenses are less than the budget
while expenses < inputbudget:
    expenses2 = float(input("Enter an expense amount (or 0 to finish): "))

    # Stop the loop if the user enters 0
    if expenses2 == 0:
        break

    # Add new expense to total
    expenses += expenses2

    # Calculate remaining budget
    budget = inputbudget - expenses

    # Show user how much budget is left
    print("You have", budget, "left in your budget.")
    budgetfile = open("budget.txt")





# After loop ends
print("Total spent:", expenses)
print("Remaining budget:", inputbudget - expenses)
savefile = open("budget.txt", "w")
savefile.write("Total Budget: " + str(inputbudget) + "\n")
savefile.write("Total Expenses: " + str(expenses) + "\n")
savefile.write("Remaining Budget: " + str(inputbudget - expenses) + "\n")
savefile.close()



