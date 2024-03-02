product_name = "beef"
unit_price = 25.92
quantity = 6.0
 
title = f"{'name':^7}:{product_name:^10}"
print("#", title)
#  name  :   beef   
 
qty = f"{'qty':>7}:{quantity:<08.3f}kg"
print("#", qty)
#     qty:6.000000kg
 
price = f"{'price':>7}:${unit_price:9.2f}"
print("#", price)
#   price:$    25.92
 
total = f"{'total':=<7}:${quantity*unit_price:09.2f}"
print("#", total)
# total==:$000155.52
