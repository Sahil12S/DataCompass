import store
import product

s = store.Store("test store")

p1 = product.Product("T-shirt", 2.5, "Appraisal")
p2 = product.Product("Jeans", 5.6, "Appraisal")
p3 = product.Product("Bread", 0.95, "Food")

s.add_product(p1).add_product(p2).add_product(p3)

s.sell_product(p1.get_id())
s.inflation(.2)
s.set_clearance("Appraisal", .3)
