class Account:
    def __init__(self, name, acc_nr):
        self.balance = 0.0
        self.owner = name
        self.bank_acc = acc_nr
        self.o_limit = 100
        self.interest_rate = 0.01
        self.borrow_rate = -0.1

    def check_balance(self):
        return self.balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Cant deposit negative amount")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Cant withdraw negative amount")
        if self.balance - amount <= self.o_limit:
            self.balance -= amount
        else:
            raise ValueError("overdraft limit exceeded")

    def add_interest(self):
        if self.balance > 0:
            interest = self.balance * self.interest_rate
            self.balance += interest
        else:
            borrow = self.balance * self.borrow_rate
            self.balance -= borrow

class CreditAccount(Account):
    def __init__(self, name, acc_nr, limit):
        Account.__init__(self, name, acc_nr)
        self.overdraft_limit = limit
        self.borrow_rate = self.borrow_rate
        self.withdraw_charge = 0.01

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError ("Cant withdraw negative amount")
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            self.balance -= self.withdraw_charge * amount
        else:
            raise ValueError("overdraft limit exceeded")

    def change_borrow_rate(self, new_rate):
        self.borrow_rate = new_rate

acc_1 = Account("me", "1234")
acc_2 = CreditAccount("you", "5678", 2000)
acc_1.deposit(200)
print(acc_1.check_balance())
acc_2.deposit(300)
acc_2.withdraw(500)
print(acc_2.check_balance())