class atm:
    def __init__(self , balance=1000):
        self.balance = balance


    def check_balance(self):
        print(f"\n Available Balance: {self.balance:.2f}")


    def deposit(self):
        Amount=int (input("Enter the deposit amount: "))
        if Amount > 0:
            self.balance +=Amount
            print("Deposited Succesfully. ")
        else:
            print("Invalid Amount.")

    def withdraw(self):
        Amount=int(input("Enter the Withdraw amount"))
        if Amount<=0:

            print("Invalid amount.")
        elif Amount > self.balance:
            print("Insufficient Balance: ")
        else:
            self.balance -= Amount
            print(f"Rs:{Amount:.2f} Withdrawn Successfully. ")

    def menu(self):
        while True:
            print("\n****ATM Transaction****")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice=input("Enter your choice: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice =="4":
                print("Thankyou Visit again. ")
            else:
                print("Invalid Choice,Please enter the correct choice. ")


atm=atm()
atm.menu()