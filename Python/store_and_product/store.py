class Store:
    def __init__(self, name):
        self.name = name
        self.products = list()

    def add_product(self, new_product):
        self.products.append(new_product)
        print("New product added")
        print("-"*10)
        new_product.print_info()
        print("="*10)
        return self

    def sell_product(self, id):
        print("Product Sold")
        print("-"*10)
        for i in range(len(self.products)):
            if self.products[i].id == id:
                self.products[i].print_info()
                del self.products[i]
                break
        print("="*10)
        return self

    def inflation(self, percent_increase):
        print(f"Inflating prices by {percent_increase}")
        for i in range(len(self.products)):
            self.products[i].update_price(percent_increase, True)

        print("New prices")
        print("-"*10)
        for i in range(len(self.products)):
            self.products[i].print_info()
            print("-"*10)
        print("="*10)
        return self

    def set_clearance(self, category, percent_discount):
        print(f"Clearance discount of {percent_discount}")

        for i in range(len(self.products)):
            if self.products[i].category == category:
                self.products[i].update_price(percent_discount, False)
        print("New prices")
        print("-"*10)
        for i in range(len(self.products)):
            self.products[i].print_info()
            print("-"*10)
        print("="*10)
        return self
