class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    @property
    def balance(self) -> int:
        return self.amount

    def handle_transaction(self, transaction_amount: int) -> str:
        if self.amount + transaction_amount <= 0:
            raise ValueError("sorry cannot go in debt!")

        self.amount += transaction_amount
        self._transactions.append(transaction_amount)

        return f"New balance: {self.amount}"

    def add_transaction(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

        return self.handle_transaction(amount)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return self._transactions[::-1]  # reversed(self._transactions)

    def __gt__(self, other):
        return self.amount > other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __add__(self, other):
        new_object = Account(f"{self.owner}&{other.owner}", sum([self.amount, other.amount]))
        new_object._transactions = self._transactions.copy()
        new_object._transactions.extend(other._transactions)

        return new_object


acc = Account('bob', 10)
acc2 = Account('john')

print(acc)
print(repr(acc))

acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)

print(acc.balance)
print(len(acc))

for transaction in acc:
    print(transaction)

print(acc[1])
print(list(reversed(acc)))

acc2.add_transaction(10)
acc2.add_transaction(60)

print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)

acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
