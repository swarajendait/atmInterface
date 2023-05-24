print("Welcome to the GitATM!")
name = str(input("Enter your name: "))
account_number = str(input("Enter your Account Number: "))
print("Great you have just created your GitATM bank account!", name, "(If you quit you might want to create a new account)")

bankBalance = 0
print("Enter your choice: ")

def bank():
    choice = (input("1. Deposit Amount\n2. Withdraw Amount\n3. Check Bank Balance\n4. View Bank Info\n5. Quit\nEnter the number corresponding to the option: "))
    if choice == "1":
        print("Choice 1 is selected")
    elif choice == "2":
        print("Choice 2 is selected")
    elif choice == "3":
        print("Choice 3 is selected")
    elif choice == "4":
        print("Choice 4 is selected")
    elif choice == "5":
        print("Choice 5 is selected")
    
    if choice != ["1", "2", "3", "4", "5"]:
        print("\n\nERROR\nRetrying...")
        bank()

bank()