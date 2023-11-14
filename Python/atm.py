print("WELCOME TO SBI ATM")
pin = input("Enter your pin:")
current = int(input("Enter Credit Amount:"))
user = {"pin": "1234", "balance": current}


def balance_enq():
    print("You have {} rupees in your account".format(user["balance"]))


def withdraw():
    amount = int(input("Enter amount to be debited:"))
    if amount > user["balance"]:
        print("Dont have sufficient balance")
    else:
        user["balance"] = user["balance"] - amount
        print("{} is debited.Remaining Balance is {}".format(amount, user["balance"]))


def deposit():
    dep = int(input("Enter amount to deposit:"))
    user["balance"] = user["balance"] + dep
    print("{} is deposited. Your current balance is {}".format(dep, user["balance"]))


if pin == user["pin"]:
    print("What do you want to do")
    print("Enter 1 to withdraw cash \nEnter 2 for Balance Enquiry \nEnter 3 for deposit cash \nEnter 4 to Quit")
    q = int(input("Enter the number:"))
    if q == 1:
        withdraw()
    elif q == 2:
        balance_enq()
    elif q == 3:
        deposit()
    elif q == 4:
        exit()
    else:
        print("Please Enter a correct value")
else:
    print("wrong pin")
