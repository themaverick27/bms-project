import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    # Load existing data
    try:
        if Path(database).exists():
            with open(database, 'r') as fs:
                data = json.loads(fs.read())
        else:
            print("No database file found. Creating a new one.")
    except Exception as err:
        print(f"Error occurred as {err}")
        data = []

    # update JSON file
    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    # Generate Account Number
    @classmethod
    def __generateAccountNum(cls):
        alpha   = random.choices(string.ascii_letters, k = 3)
        digit   = random.choices(string.digits, k = 4)
        special = random.choices("!@#$%^&*", k = 1)
        id = alpha + digit + special
        random.shuffle(id)
        return "".join(id)

    # Create Bank Account
    def createAccount(self):
        info = {
            "name"      : input("Enter your name: "),
            "age"       : int(input("Enter your age: ")),
            "email"     : input("Enter your email: "),
            "pin"       : int(input("Enter your pin (4 digit): ")),
            "accountNum": Bank.__generateAccountNum(),
            "balance"   : 0
        }

        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("Sorry, You cannot create account.")
        else:
            print("Account has been created successfully!")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number!")

            Bank.data.append(info) # data = [{info}]
            Bank.__update()

    # Deposit Money
    def depositMoney(self):
        account_num = input("Enter your account number: ")
        account_pin = int(input("Enter your account pin: "))

        user_data = [i for i in Bank.data if i['accountNum'] == account_num and i['pin'] == account_pin]
        if user_data == False:
            print("No data found!")
        else:
            amount = int(input("Enter your amount to be deposit: "))
            if amount > 10000:
                print("Amount more than 10,000 can't be deposit!")
            elif amount <= 0:
                print("Amount must be greater than 0.")
            else:
                user_data[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully!")

    # Withdraw Money
    def withdrawMoney(self):
            account_num = input("Enter your account number: ")
            account_pin = int(input("Enter your account pin: "))
    
            user_data = [i for i in Bank.data if i['accountNum'] == account_num and i['pin'] == account_pin]
            if user_data == False:
                print("No data found!")
            else:
                amount = int(input("Enter your amount to be withdraw: "))
                if amount > user_data[0]['balance']:
                    print("No sufficient balance in the bank account!")
                elif amount <= 0:
                    print("Amount must be greater than 0.")
                else:
                    user_data[0]['balance'] -= amount
                    Bank.__update()
                    print("Amount withdraw successfully!")

    # Bank Details
    def bankDetails(self):
        account_num = input("Enter your account number: ")
        account_pin = int(input("Enter your account pin: "))

        user_data = [i for i in Bank.data if i['accountNum'] == account_num and i['pin'] == account_pin]
        if user_data == False:
            print("No data found!")
        else:
            for i in user_data[0]:
                print(f"{i} : {user_data[0][i]}")

    # Update Bank Details
    def updateBankDetails(self):
        account_num = input("Enter your account number: ")
        account_pin = int(input("Enter your account pin: "))

        user_data = [i for i in Bank.data if i['accountNum'] == account_num and i['pin'] == account_pin]
        if user_data == False:
            print("No data found!")
        else:
            print("press 1 for updating your name")
            print("press 2 for updating your email")
            print("press 3 for updating your pin")

            user_choice = int(input("Enter your response: "))
            if user_choice == 1:
                new_name = input("Enter new name: ")
                user_data[0]['name'] = new_name
                Bank.__update()
                print("Name updated successfully!")

            elif user_choice == 2:
                new_email = input("Enter new email: ")
                user_data[0]['email'] = new_email
                Bank.__update()
                print("Email Updated successfully!")

            elif user_choice == 3:
                new_pin = input("Enter new pin: ")
                user_data[0]['pin'] = new_pin
                Bank.__update()
                print("Pin Updated successfully!")
            else:
                print("Invalid Choice!")

    # Delete Account
    def deleteAccount(self):
        account_num = int(input("Enter your account number: "))
        account_pin = int(input("Enter your account pin: "))

        user_data = [i for i in Bank.data if i['accountNum'] == account_num and i['pin'] == account_pin]
        if user_data == False:
            print("No data found!")
        else:
            print("press 1 for delete account confirmation")
            print("press 2 for stop the process")

            user_choice = int(input("Enter your choice: "))
            if user_choice == 1:
                index = Bank.data.index(user_data[0])
                Bank.data.pop(index)
                print("Account deleted successfully!")
                Bank.__update()

            elif user_choice == 2:
                print("Stopped!")
            else:
                print("Invalid Choice!")


user = Bank()

print("press 1 for creating a bank account")
print("press 2 for Deposit money in the account")
print("press 3 for Withdraw money from the account")
print("press 4 for bank details")
print("press 5 for updating the bank details")
print("press 6 for deleting your bank account")

user_response = int(input("Please tell me your response: "))

if user_response == 1:
    user.createAccount() 
elif user_response == 2:
    user.depositMoney()
elif user_response == 3:
    user.withdrawMoney()
elif user_response == 4:
    user.bankDetails()
elif user_response == 5:
    user.updateBankDetails()
elif user_response == 6:
    user.deleteAccount()
else:
    print("Invalid Choice!")