from bank_teller import BankAccount

balance = 0
op_num = 0
options = ""
transacting = True

account_name = input("Please input account name: ")
my_account = BankAccount(account_name, balance)

ops = ["balance", "deposit", "withdraw"]
for op in ops:
    op_num +=1
    options += f"[{op_num}] {op.capitalize()} "
while transacting:
    choice = int(input(f"Greetings {account_name.capitalize()}! Welcome to PyBank. How can we help you today?: {options}: "))
    
    if choice == 1:
        my_account.display_balance()
    elif (choice == 2) or (choice == 3):
        amount = float(input(f"Please input desired amount [P]: "))
        if choice == 2:
            my_account.deposit(amount)
        else: 
            my_account.withdraw(amount)
    elif choice == "off":
        break
    else: 
        print("Invalid choice ...")

print("Thank you for using PyBank!")
# # TODO: Create an instance of the BankAccount class
# my_account = BankAccount("John Doe", 1000)  # Owner: John Doe, Initial Balance: $1000

# # TODO: Call the deposit method
# my_account.deposit(500)  # Deposit $500, New Balance: $1500

# # TODO: Call the withdraw method
# my_account.withdraw(200)  # Withdraw $200, New Balance: $1300

# # TODO: Call the display_balance method
# my_account.display_balance()  # Should show the current balance of $1300

# # TODO: Try withdrawing more money than the balance to see what happens
# my_account.withdraw(2000)  # Should show an "Insufficient funds" message
