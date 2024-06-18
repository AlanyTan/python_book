product_name = "beef"
unit_price = 25.92
quantity = 6.0
 
title = f"{'name':^7} :{product_name:^10}"
print("#", title)
 
qty = f"{'qty':>7} :{quantity:>8.3f}kg"
print("#", qty)
 
price = f"{'price':>7} :${unit_price:9.2f}"
print("#", price)
 
total = f"{'total':=<7} :${quantity*unit_price:09.2f}"
print("#", total)
#  name   :   beef   
#     qty :   6.000kg
#   price :$    25.92
# total== :$000155.52
