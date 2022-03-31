class Discount:
    # discounts_dict = {
    #     'DIS_10': {'disc': .1, 'points': 10},
    #     'DIS_15': {'disc': .15, 'points': 15},
    #     'DIS_20': {'disc': .2, 'points': 20},
    #     }
        
    def __init__(self, key, value, points):
        self.name = key
        self.value = value
        self.points = points
    
    def __str__(self):
        return " Name: %s \n Price: %s \n Points: %s \n" % (self.name, self.value, self.points)