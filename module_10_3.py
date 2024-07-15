from threading import Thread, Lock


class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.lock = Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Deposited {amount}, new balance is {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}, new balance is {self.balance}")
            else:
                print(f"Not enough money. Current balance: {self.balance}")


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(6):
        account.withdraw(amount)


if __name__ == "__main__":
    account = BankAccount(1000)

    deposit_thread = Thread(target=deposit_task, args=(account, 100))
    withdraw_thread = Thread(target=withdraw_task, args=(account, 300))

    deposit_thread.start()
    withdraw_thread.start()

    deposit_thread.join()
    withdraw_thread.join()
