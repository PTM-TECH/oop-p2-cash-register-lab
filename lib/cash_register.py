class CashRegister:
    def __init__(self, discount=0):
        # Initialize a CashRegister object.
        # Args:discount (int): percentage discount to apply (0-100). 
        # Default is 0.
        if not isinstance(discount, int) or not (0 <= discount <= 100):
            print("Not valid discount")
            self.discount = 0
        else:
            self.discount = discount

        self.total = 0
        self.items = []  # List of item names
        self.previous_transactions = []  # List of dicts {item, price, quantity}

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Ensure discount is integer between 0-100 inclusive
        if not isinstance(value, int) or not (0 <= value <= 100):
            print("Not valid discount")
            self._discount = 0
        else:
            self._discount = value

    def add_item(self, item, price, quantity=1):
        """Add an item to the cash register."""
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })
        
        # print(f"Added {quantity} x {item} at ${price:.2f} each. Total is now ${self.total:.2f}")
    def apply_discount(self):
        if self.total == 0:
            print("There is no discount to apply.")
            return

        if self.discount == 0:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        #Remove last transaction completely.
        if not self.previous_transactions:
            print("No transactions to void.")
            return

        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]

        for _ in range(last_transaction["quantity"]):
            self.items.remove(last_transaction["item"])

        # Format total as integer to match test expectations
        print(f"Voided last transaction: {last_transaction['quantity']} x {last_transaction['item']}. Total is now ${int(self.total)}.")


# Example usage
if __name__ == "__main__":
    register = CashRegister(discount=20)
    register.add_item("T-shirt", 15.0, 2)
    register.add_item("Hat", 10.0)
    register.apply_discount()
    register.void_last_transaction()