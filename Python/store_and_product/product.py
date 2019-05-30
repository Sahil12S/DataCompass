import uuid


class Product:
    def __init__(self, name, price, category):
        self.id = uuid.uuid4()
        self.name = name
        self.price = price
        self.category = category

    def get_id(self):
        return self.id

    def update_price(self, precentage_change, is_increased):
        if is_increased:
            self.price += self.price * precentage_change
        else:
            self.price -= self.price * precentage_change
        return self

    def print_info(self):
        print(
            f"ID: {self.id}\nName: {self.name}\nPrice: {self.price}\nCategory: {self.category}")
        return self
