class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def deposit(self):
        amount = float(input("Введите сумму для пополнения: "))
        self._balance += amount
        print(f"Текущий баланс: {self._balance}")

    def _reset_balance(self):
        self._balance = 0
        print("Баланс сброшен.")

    def __jackpot_bonus(self):
        self._balance *= 10
        print(f"Баланс после джекпота: {self._balance}")

    def _merge_balance(self, other):
        self._balance += other._balance
        print(f"Суммарный баланс: {self._balance}")



account1 = Bank("Иван", 2000)
account1.deposit()
account1._reset_balance()
account1._Bank__jackpot_bonus()

account2 = Bank("Ольга", 700)
account1._merge_balance(account2)

