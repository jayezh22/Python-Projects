# Define a class called Bank
class Bank:
    # Class attributes (shared by all instances)
    account_name = " "  # default account name
    account_Id = 0  # default account ID
    account_balance = 10000  # default account balance
    account_pin = 1234  # default PIN

    # Method to show account details
    def showdetails(self):
        print(self.account_name)  # print account name
        print(self.account_Id)  # print account ID
        print(self.account_balance)  # print account balance

    # Method to debit an amount from the account
    def debit(self, amount):
        if amount > self.account_balance:  # check if amount exceeds balance
            print("Insufficient balance\n")  # print error message
            return self.account_balance  # return current balance
        else:
            self.account_balance -= amount  # subtract amount from balance
            print("Amount has been debited\n")  # print success message
            return self.account_balance  # return updated balance

    # Method to credit an amount to the account
    def credit(self, amount):
        if amount < 0:  # check if amount is invalid
            print("Invalid amount\n")  # print error message
            return self.account_balance  # return current balance
        else:
            self.account_balance += amount  # add amount to balance
            print("Amount has been credited\n")  # print success message

    # Method to set a new PIN
    def set_pin(self, pin):
        self.account_pin = pin  # update PIN
        print("PIN has been set")  # print success message

    # Method to check if a PIN is correct
    def check_pin(self, pin):
        return self.account_pin == pin  # return True if PIN matches, False otherwise

    # Method to show transaction options
    def showoptions(self):
        print("Transaction options:-")
        print("Enter .1. to Debit")
        print("Enter .2. to Credit")
        print("Enter .3. to Show Your Account Details")
        print("Enter .4. to Set New PIN")
        print("Enter .5. to Exit")

# Create an instance of the Bank class
hdfc = Bank()

# Set account details
hdfc.account_name = input("Enter name: ")
hdfc.account_Id = input("Enter account Id: ")
hdfc.account_balance = int(input("Enter balance: "))
hdfc.account_pin = int(input("Enter PIN: "))
print()

# Main loop to handle transactions
while True:
    hdfc.showoptions()  # show transaction options
    choice = input("Select an option/number: ")

    if choice == "1":  # debit
        amount = int(input("Enter Amount to debit: "))
        if hdfc.check_pin(int(input("Enter PIN: "))):  # check PIN
            hdfc.debit(amount)  # debit amount
        else:
            print("Incorrect PIN. Transaction canceled.")

    elif choice == "2":  # credit
        amount = int(input("Enter Amount to credit: "))
        if hdfc.check_pin(int(input("Enter PIN: "))):  # check PIN
            hdfc.credit(amount)  # credit amount
        else:
            print("Incorrect PIN. Transaction canceled.")

    elif choice == "3":  # show account details
        hdfc.showdetails()

    elif choice == "4":  # set new PIN
        new_pin = int(input("Enter new PIN: "))
        hdfc.set_pin(new_pin)

    elif choice == "5":  # exit
        print("invalid number")  # should be "Exiting..." or something more informative
        break  # exit the loop