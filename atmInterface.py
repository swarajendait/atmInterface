print("Welcome to the GitATM!")

#Login List
usernameList = ["Swaraj"]
passwordList = ["abcsss"]
# Note the 1st item of the username list corresponds to the 1st item of the password(s) list

# FUNCTIONS
def createAcc():
        usernameSignUp = str(input("Enter your new username: "))
        usernameList.append(usernameSignUp)

        passwordSignUp = str(input("Enter your new password: "))
        passwordList.append(passwordSignUp)
        print("You have successfully created your account!\n\nNow Please Login Again!")
        checkLoginSystem()


def bank():
    choice = str(input("1. Deposit Amount\n2. Withdraw Amount\n3. Check Bank Balance\n4. View Bank Info\n5. Quit\nEnter the number corresponding to the option: "))
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
    elif choice != ["1", "2", "3", "4", "5"]:
        print("\n\nERROR\nRetrying...")
        bank()

def checkLoginSystem():
    try:
        usernameLogin = str(input("Username: "))
        checkUserList = usernameList.index(usernameLogin)
        if checkUserList == usernameList.index(usernameLogin):
            indexOfcheckUserList = checkUserList 
            passwordLogin = str(input("Password: "))
            checkPasswordList = passwordList.index(passwordLogin)
            if checkPasswordList == indexOfcheckUserList:
                print("\n\n...\nSuccesfully logged In!")
                bank()
    except ValueError:
        error = str(input("Password does not match! (If you want to create a new account type 'cracc' OR type 'retry' to retry): "))
        if error == "cracc":
            createAcc()
        elif error == "retry":
            checkLoginSystem()
        else:
            print("-Error-\n please type cracc")

checkLogin = input("Are you an existing user? ")
if checkLogin == "yes" or checkLogin == "y" or checkLogin == "Y" or checkLogin == "YES":
    checkLoginSystem()
elif checkLogin == "no" or checkLogin == "n" or checkLogin == "NO" or checkLogin == "N":
    print("You are going to create a new account!!")
    createAcc()