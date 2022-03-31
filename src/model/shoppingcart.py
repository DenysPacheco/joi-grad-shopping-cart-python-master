from src.model.product import Product
from src.model.customer import Customer
from src.model.order import Order


class ShoppingCart:
    def __init__(self, customer=Customer, products=[]):
        self.products = products
        self.customer = customer

    def add_product(self, product):
        self.products.append(product)

    def checkout(self):
        total_price = 0.00
        loyalty_points_earned = 0.00
        flag_products_bulk = False
        list_products_bulk = []
        
        discounts_dict = {
            'DIS_10': {'disc': .1, 'points': 10},
            'DIS_15': {'disc': .15, 'points': 15},
            'DIS_20': {'disc': .2, 'points': 20},
        }
        
        for product in self.products:
            discount = 0.00
            if product.product_code in tuple(discounts_dict.keys()):
                loyalty_points_earned += (product.price / discounts_dict[product.product_code]['points'])
                discount = product.price * discounts_dict[product.product_code]['disc']
            # if product.product_code.startswith("DIS_10"):
            #     loyalty_points_earned += (product.price / 10)
            #     discount = product.price * 0.1
            # elif product.product_code.startswith("DIS_15"):
            #     loyalty_points_earned += (product.price / 15)
            #     discount = product.price * 0.15
            # elif product.product_code.startswith("DIS_20"):
            #     loyalty_points_earned += (product.price / 20)
            #     discount = product.price * 0.20
            elif product.product_code.startswith("BULK_BUY_2_GET_1"):
                if(flag_products_bulk and product.name in list_products_bulk):
                    product.price = 0
                    flag_products_bulk = False
                    list_products_bulk.remove(product.name)
                else:
                    flag_products_bulk = True
                    list_products_bulk.append(product.name)
            else:
                loyalty_points_earned += (product.price / 5)
                discount = 0.00
            
            total_price += product.price - discount
            
        
        if total_price > 500 and product.product_code.startswith('DIS_5_TOTAL'):
            total_price *= .95
            
        return Order(int(loyalty_points_earned), total_price)

    def __str__(self):
        product_list = "".join('%s' % product for product in self.products)
        return "Customer: %s \nBought: \n%s" % (self.customer, product_list)
