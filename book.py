#! usr/bin/env python3

class Book:
    def __init__(self, title, author, price, qty):
        self.title = title
        self.author = author
        self.price = price
        self.qty = qty

    def get_discount_percent(self):
        if self.qty > 100:
            return .50
        elif self.qty > 50:
            return.25
        elif self.qty > 25:
            return .25
        else:
            return .10
    def get_discount_amount(self):
        return self.price * self.get_discount_percent()
    def get_discounted_price(self):
        return self.price - self.get_discount_amount()
