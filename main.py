class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        transaction = {
            'amount': amount,
            'description': description
        }
        self.ledger.append(transaction)

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction['amount']
        return balance

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            transaction = {
                'amount': -amount,
                'description': description
            }
            self.ledger.append(transaction)
            return True
        return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def __str__(self):
        output = self.name.center(30, '*') + '\n'

        for transaction in self.ledger:
            description = transaction['description'][:23]
            amount = f"{transaction['amount']:.2f}"

            output += f"{description:<23}{amount:>7}\n"

        output += f"Total: {self.get_balance():.2f}"

        return output


def create_spend_chart(categories):
    # Calculate total spending for all categories
    total_spent = 0
    spent = []

    for category in categories:
        category_spent = 0

        for transaction in category.ledger:
            if transaction['amount'] < 0:
                category_spent += -transaction['amount']

        spent.append(category_spent)
        total_spent += category_spent

    # Calculate percentages
    percentages = []

    for amount in spent:
        percentage = int((amount / total_spent) * 100)
        percentage = (percentage // 10) * 10
        percentages.append(percentage)

    output = "Percentage spent by category\n"

    # Create bars from 100 to 0
    for level in range(100, -1, -10):
        output += f"{level:>3}|"

        for percentage in percentages:
            if percentage >= level:
                output += " o "
            else:
                output += "   "

        output += " \n"

    # Horizontal line
    output += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names vertically
    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        output += "     "

        for category in categories:
            if i < len(category.name):
                output += category.name[i] + "  "
            else:
                output += "   "

        output += "\n"

    return output.rstrip("\n")
