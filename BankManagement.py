class Bank:
    total_balance = 0
    total_loan_amount = 0
    loan = True

    @staticmethod
    def create_account(name, initial_deposit):
        Bank.total_balance += initial_deposit
        return User(name, initial_deposit)

    @classmethod
    def check_total_balance(cls):
        return cls.total_balance

    @classmethod
    def check_total_loan_amount(cls):
        return cls.total_loan_amount

    @classmethod
    def toggle_loan(cls, status):
        cls.loan = status

    @classmethod
    def is_bankrupt(cls):
        return cls.total_balance < 0

class User:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        Bank.total_balance += amount
        self.transaction_history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if Bank.total_balance > amount:
            if self.balance >= amount:
                self.balance -= amount
                Bank.total_balance -= amount
                self.transaction_history.append(f"Withdrew {amount}")
            else:
                print("Insufficient funds! ")
        else:
            print("Bank is bankrupt.")

    def transfer(self, amount, recipient):
        if Bank.total_balance > amount:
            if self.balance >= amount:
                 self.balance -= amount
                 recipient.balance += amount
                 self.transaction_history.append(f"Transferred {amount} to {recipient.name}")
                 recipient.transaction_history.append(f"Received {amount} from {self.name}")
            else:
                print("Insufficient funds!")
        else:
            print(" Bank is bankrupt.")

    def check_balance(self):
        return self.balance

    def take_loan(self,loan_amount):
        if Bank.loan:
            if loan_amount<=  2 * self.balance:
                self.balance += loan_amount
                Bank.total_loan_amount += loan_amount
                Bank.total_balance -=loan_amount
                self.transaction_history.append(f"Took a loan of {loan_amount}")
            else:
                print(f"you can't take loan more than {2*self.balance}")
        else:
            print("Loan  is currently disabled by the bank.")

    def view_transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)




if __name__ == "__main__":
    saiful = Bank.create_account("Saiful", 2000)
    islam = Bank.create_account("Islam", 1000)


    saiful.deposit(1000)
    saiful.withdraw(5000)
    saiful.transfer(1000, islam)
    saiful.take_loan(2000)


    print("Saiful balance:", saiful.check_balance())
    print("Islam balance:", islam.check_balance())
    print("Bank total balance:", Bank.check_total_balance())
    print("Bank total loan amount:", Bank.check_total_loan_amount())

    print("\n Transaction history:")
    saiful.view_transaction_history()

