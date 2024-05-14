# Coffee
# name, price
# get_name, get_price

class Coffee:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def get_name(self):
        return f"{self.name}"
    def get_price(self):
        return f"{self.price}"
