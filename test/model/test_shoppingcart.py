import unittest
# import pytest

from src.model.customer import Customer
from src.model.product import Product
from src.model.shoppingcart import ShoppingCart

CUSTOMER = Customer("test")
PRICE = 100
PRODUCT = "T"

CODPROD10 = 'DIS_10'
CODPROD15 = 'DIS_15'
CODPROD20 = 'DIS_20'


# class TestShoppingCartTest():
class ShoppingCartTest(unittest.TestCase):
    def test_should_calculate_price_with_no_discount(self):
        products = [Product(PRICE, "", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(100.00, order.total)
        # assert 100.00 == order.total

    def test_should_calculate_loyalty_points_with_no_discount(self):
        products = [Product(PRICE, "", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(20, order.loyalty_points)
        # assert 20 == order.loyalty_points

    def test_should_calculate_price_with_10_percent_discount(self):
        products = [Product(PRICE, CODPROD10, PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(90.00, order.total)
        # assert 90.00 == order.total

    def test_should_calculate_loyalty_points_with_10_percent_discount(self):
        products = [Product(PRICE, CODPROD10, PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(10, order.loyalty_points)
        # assert 10 == order.loyalty_points

    def test_should_calculate_price_with_15_percent_discount(self):
        products = [Product(PRICE, CODPROD15, PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(85.00, order.total)
        # assert 85.00 == order.total

    def test_should_calculate_loyalty_points_with_15_percent_discount(self):
        products = [Product(PRICE, CODPROD15, PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(6, order.loyalty_points)
        # assert 6 == order.loyalty_points
        
    def test_should_calculate_price_with_20_percent_discount(self):
        products = [Product(PRICE, CODPROD20, PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()
        
        self.assertEqual(80.00, order.total)
        # assert 80.00 == order.total
        self.assertEqual(5, order.loyalty_points)
        # assert 5 == order.loyalty_points
        
    def test_should_calculate_price_bulk_one(self):
        # BULK_BUY_2_GET_1_aoisdu
        products = [Product(PRICE, "BULK_BUY_2_GET_1_aoisdu", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()
        
        self.assertEqual(100, order.total)
        # assert 100 == order.total
        
    def test_should_calculate_price_bulk_more(self):
        # BULK_BUY_2_GET_1_aoisdu
        products = [Product(PRICE, "BULK_BUY_2_GET_1_aoisdu", 'A'), 
                    Product(PRICE, "BULK_BUY_2_GET_1_aoisdu", 'A'),
                    Product(PRICE, "BULK_BUY_2_GET_1_aoisdu", 'B'),
                    Product(PRICE, "BULK_BUY_2_GET_1_aoisdu", 'C')]
        
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()
        
        self.assertEqual(300, order.total)
        # assert 300 == order.total

    def test_should_calculate_price_with_5_percent_discount_total_under_500(self):
        products = [Product(PRICE, "DIS_5_TOTAL_12pek_12pek", PRODUCT), 
                    Product(PRICE, "DIS_5_TOTAL_12pek", PRODUCT),
                    Product(PRICE, "DIS_5_TOTAL_12pek", PRODUCT),
                    Product(PRICE, "DIS_5_TOTAL_12pek", PRODUCT),
                    Product(PRICE, "DIS_5_TOTAL_12pek", PRODUCT)]
        
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()
        
        self.assertEqual(500, order.total)
        # assert 500 == order.total
    
    def test_should_calculate_price_with_5_percent_discount_total_over_500(self):
        products = [Product(PRICE, "DIS_5_TOTAL_12pek", PRODUCT), 
                    Product(PRICE, "DIS_5_TOTAL_12pek", PRODUCT),
                    Product(PRICE, "DIS_5_TOTAL_12pek", PRODUCT),
                    Product(PRICE, "DIS_5_TOTAL_12pek", PRODUCT),
                    Product(PRICE, "DIS_5_TOTAL_12pek", PRODUCT),
                    Product(PRICE, "DIS_5_TOTAL_12pek", PRODUCT)]
        
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()
        
        self.assertEqual(600*0.95, order.total)
        # assert 600*0.95 == order.total