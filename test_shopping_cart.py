from shopping_cart import ShoppingCart
from item_database import ItemDatabase
from unittest.mock import Mock
import pytest

@pytest.fixture
def cart():
	#all set up for cart here
	return ShoppingCart(5)

def test_can_add_item_to_cart(cart):
	cart.add("apple")
	assert cart.size() == 1 #asserts 1 item has been added

def test_cart_contains_item_when_item_appended(cart):
	cart.add("apple")
	assert "apple" in cart.get_items() #checks if item "apple" is in cart

def test_add_more_than_max_items_should_fail(cart):
	for _ in range(5):
		cart.add("apple")
	with pytest.raises(OverflowError):
		cart.add("apple")

def test_get_total_price(cart):
	cart.add("apple")
	cart.add("orange")
	item_database = ItemDatabase()

	def mock_get_item(item: str):
		if item == "apple":
			return 1.0
		if item == "orange":
			return 2.0
		
	item_database.get = Mock(side_effect=mock_get_item)
	assert cart.get_total_price(item_database) == 3.0