weight =4.8
price = 0.0
#Ground Shipping
if weight <= 2.0:
  price = 20.00 + (1.50 * weight)
elif (weight > 2.0) and (weight <= 6.0):
  price = 20.00 + (3.00 * weight)
elif (weight > 6.0) and (weight <= 10.0 ):
  price = (4.00 * weight) + 20.00
elif weight > 10:
  price = 20.00 + (4.75 * weight)

print (price)
premium_price = 125.00
print(premium_price)
# Drone Shipping
if weight <= 2.0:
  price = (4.5 * weight)
elif (weight > 2.0) and (weight <= 6.0):
  price =  (9 * weight)
elif (weight > 6.0) and (weight <= 10.0 ):
  price = (12 * weight) 
elif weight > 10:
  price =  (14.25 * weight)
print(price)
