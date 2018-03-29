#!usr/env/bin python

class ShoppingCart(object):


	items_inCart={} #global dictionary
	def __init__(self,customer_name):
		self.customer_name =customer_name
	#add items in cart
	
	def add_items(self,product,price):
		if product in self.items_inCart:
			print "Item already in Cart."
		else:
			self.items_inCart[product] = price
			print "Item added to the Cart."
			
	def remove_items(self,product):
		if product in self.items_inCart:
			del self.items_inCart[product]
			print "Item:"+ product + "is removed."
		else:
			print "Item:"+ product + "is not in the cart."

my_cart = ShoppingCart("Smriti")
my_cart.add_items("Toothpaste", 2)
my_cart.add_items("Towel",4)
my_cart.add_items("Pajamas",10)
print my_cart.items_inCart