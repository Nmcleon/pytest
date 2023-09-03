from shopping_cart import ShoppingCart

def test_can_add_item_to_cart():
	cart = ShoppingCart()
	cart.add("apple")
	assert cart.size() == 1 #asserts 1 item has been added

def test_cart_contains_item_when_item_appended():
	cart = ShoppingCart()
	cart.add("apple")
	assert "apple" in cart.get_items() #checks if item "apple" is in cart