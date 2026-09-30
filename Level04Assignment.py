#Mason Chandler
#Level 04 Assignment

#Input
expenses = []
number_expenses = 0
input_expense = float(input("Enter expense here (Press 0 to Finish): "))

#Storing the Inputs
while input_expense != 0:
    if input_expense >= 0:
        expenses.append(input_expense)
        input_expense = float(input("Enter expense here (Press 0 to Finish): "))
    else :
        print("Invalid Number. Enter a positive number please.")
        input_expense = float(input("Enter expense here (Press 0 to Finish): "))

#Classifying Each Expense
for each input_expense in expenses:
    if input_expense < 25.00 :
        print ("Small Expense")
    elif input_expense >= 25.00 or <= 100.00:
        print ("Medium Expense")
    elif input_expense > 100:
        print ("Large Expense")




print(expenses)
print (sum(expenses))


