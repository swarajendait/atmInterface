import os
print("Welcome to the GitATM!")

# File path
login_file = "data/login.txt"

# Check if login file exists, create it if not
if not os.path.isfile(login_file):
    open(login_file, "w").close()

# Load login information from file
def loadLoginData():
    with open(login_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            username, password, balance = line.strip().split(":")
            usernameList.append(username)
            passwordList.append(password)
            balanceList.append(float(balance))

# Save login information to file
def saveLoginData():
    with open(login_file, "w") as file:
        for username, password, balance in zip(usernameList, passwordList, balanceList):
            file.write(f"{username}:{password}:{balance}\n")

# Login List
usernameList = []
passwordList = []
balanceList = []

# Load login data from file
loadLoginData()

def createAcc():
    usernameSignUp = input("Enter your new username: ")
    if usernameSignUp in usernameList:
        print("An account with that username already exists!")
        error = input("Type 'retry' to retry OR type 'login' to login: ")
        if error == 'retry':
            createAcc()
        elif error == 'login':
            checkLoginSystem()
    else:
        usernameList.append(usernameSignUp)
        passwordSignUp = input("Enter your new password: ")
        passwordList.append(passwordSignUp)
        balanceSignUp = float(input("Enter the initial bank balance: "))
        balanceList.append(balanceSignUp)
        print("You have successfully created your account!\n\nNow please login again!")
        checkLoginSystem()

def bank():
    choice = input("1. Deposit Amount\n2. Withdraw Amount\n3. Check Bank Balance\n4. View Bank Info\n5. Quit\nEnter the number corresponding to the option: ")
    if choice == "1":
        depositInptAmt = int(input("\nEnter amount to be deposited: "))
        balanceList[currentUserIndex] += depositInptAmt 
        print("Your new balance is ₹", balanceList[currentUserIndex], "\n")
        saveLoginData()
        bank()
    elif choice == "2":
        withdrawInptAmt = int(input("\nEnter amount to be withdrawn: "))
        if withdrawInptAmt > balanceList[currentUserIndex]:
            print("Insufficient balance!")
            bank()
        else:
            balanceList[currentUserIndex] -= withdrawInptAmt
            print("Your new balance is ₹", balanceList[currentUserIndex], "\n")
            saveLoginData()  
            bank()
    elif choice == "3":
        print("\nYour bank balance is: ₹", balanceList[currentUserIndex], "\n")
        bank()
    elif choice == "4":
        print("\nUsername:", usernameList[currentUserIndex], "\nPassword:", passwordList[currentUserIndex], "\nBank Balance: ₹", balanceList[currentUserIndex], "\n")
        bank()
    elif choice == "5":
        print("Thank you for using GitATM!")
        print("Credits: Swaraj Endait")
        quit()
    else:
        print("\n\nERROR\nRetrying...")
        bank()

def checkLoginSystem():
    usernameLogin = input("Username: ")
    if usernameLogin in usernameList:
        indexOfUser = usernameList.index(usernameLogin)
        passwordLogin = input("Password: ")
        if passwordList[indexOfUser] == passwordLogin:
            print("\n\n...\nSuccessfully logged in!")
            global currentUserIndex
            currentUserIndex = indexOfUser
            bank()
        else:
            print("Password does not match!")
            error = input("If you want to create a new account, type 'cracc'. Otherwise, type 'retry' to retry: ")
            if error == "cracc":
                createAcc()
            elif error == "retry":
                checkLoginSystem()
            else:
                print("Invalid input. Please try again.")

    else:
        print("Username not found!")
        error = input("If you want to create a new account, type 'cracc'. Otherwise, type 'retry' to retry: ")
        if error == "cracc":
            createAcc()
        elif error == "retry":
            checkLoginSystem()
        else:
            print("Invalid input. Please try again.")

checkLogin = input("Are you an existing user? ")
if checkLogin.lower() == "yes" or checkLogin.lower() == "y":
    checkLoginSystem()
elif checkLogin.lower() == "no" or checkLogin.lower() == "n":
    print("You are going to create a new account!")
    createAcc()

# Save login data to file
saveLoginData()