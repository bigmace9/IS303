#Mason Chandler
#Level 04 Assignment

#Input
from statistics import mean
expenses = []
number_expenses = 0
small_expense = 0
medium_expense = 0
large_expense = 0
input_expense = float(input("Enter expense here (Press 0 to Finish): "))

#Storing the Inputs
while input_expense != 0:
    if input_expense >= 0:
        expenses.append(input_expense)
        number_expenses += 1
        input_expense = float(input("Enter expense here (Press 0 to Finish): "))
    else :
        print("Invalid Number. Enter a positive number please.")
        input_expense = float(input("Enter expense here (Press 0 to Finish): "))

#Classifying Each Expense
for  number in expenses:
    if number < 25.00 :
        small_expense +=1
    elif number >= 25.00 and number <= 100.00:
        medium_expense +=1
    elif number > 100:
        large_expense +=1


#Printing and Output
print(f"\nEXPENSE OVERVIEW\n")
if len(expenses) == 0:
    print("No expenses were entered")
else:
    print(f"Total Number of Expenses: {number_expenses}")
    print(f"Total Amount of Expenses: ${sum(expenses):,.2f}")
    print(f"Average Price: ${mean(expenses):,.2f}")
    print(f"Smallest Expense: ${min(expenses):,.2f}")
    print(f"Largest Expense: ${max(expenses):,.2f}\n")
    print(f"Number of Small Expenses: {small_expense}")
    print(f"Number of Medium Expenses: {medium_expense}")
    print(f"Number of Large Expenses: {large_expense}")



