# Write a class that meets these requirements.
#
# Name:       ReceiptItem
#
# Required state:
#    * quantity, the amount of the item bought
#    * price, the amount each one of the things cost
#
# Behavior:
#    * get_total()          # Returns the quantity * price
#
# Example:
#    item = ReceiptItem(10, 3.45)
#
#    print(item.get_total())    # Prints 34.5


class ReceiptItem:
    def _init_(self, quantity, price):
        self.price = price
        self.quantity = quantity

    def get_total(self):
        self.quantity * self.price
