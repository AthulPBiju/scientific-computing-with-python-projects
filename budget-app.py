class Category:
    #__init__()
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        title = self.category.center(30, "*")
        items = ""
        for i in self.ledger:
            desc = i['description'][:23]
            amt = f"{i['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + "\n" + items + total



    #Deposit
    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    #Withdraw
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    #Balance
    def get_balance(self):
        return sum(i['amount'] for i in self.ledger)

    #Transfer
    def transfer(self, amount, budget):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget.category}")
            budget.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    #Check funds
    def check_funds(self, amount):
        return amount <= self.get_balance()

#Chart       
def create_spend_chart(categories):
    chart = "Percentage spent by category\n"

    spent = [sum(-item['amount'] for item in c.ledger if item['amount'] < 0) for c in categories]
    total_spent = sum(spent)
    percentages = [int((amt / total_spent) * 100) // 10 * 10 for amt in spent]

    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for p in percentages:
            chart += " o " if p >= i else "   "
        chart += " \n"  

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(c.category) for c in categories)
    for i in range(max_len):
        chart += "     "
        for c in categories:
            chart += (c.category[i] + "  ") if i < len(c.category) else "   "
        chart += "\n"

    return chart.rstrip("\n")