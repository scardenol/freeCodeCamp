class Category:

  def __init__(self, category):
    self.name = category
    self.ledger = []

  def get_balance(self):
    return sum(x["amount"] for x in self.ledger)

  def check_funds(self, amount):
    return self.get_balance() >= amount

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.deposit(-amount, description)
      return True
    else:
      return False

  def get_withdrawals(self):
    return sum([-item["amount"] for item in self.ledger if item["amount"] < 0])

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False

  def __str__(self):
    output = self.name.center(30, "*") + "\n"
    for item in self.ledger:
      left = item["description"][:23]
      right = "{:.2f}".format(item["amount"])
      output += left.ljust(23) + right.rjust(7) + "\n"
    output += "Total: " + "{:.2f}".format(self.get_balance())
    return output


def create_spend_chart(categories):
  total_spent = sum([category.get_withdrawals() for category in categories])
  percentages = [
      int(category.get_withdrawals() / total_spent * 10) * 10
      for category in categories
  ]
  output = "Percentage spent by category\n"
  for i in range(100, -1, -10):
    output += str(i).rjust(3) + "| "
    for percentage in percentages:
      if percentage >= i:
        output += "o  "
      else:
        output += "   "
    output += "\n"
  output += "    " + ("---" * len(categories)) + "-\n"
  longest_name_length = max([len(category.name) for category in categories])
  for i in range(longest_name_length):
    output += "     "
    for category in categories:
      if len(category.name) > i:
        output += category.name[i] + "  "
      else:
        output += "   "
    if i < longest_name_length - 1:
      output += "\n"
  return output
