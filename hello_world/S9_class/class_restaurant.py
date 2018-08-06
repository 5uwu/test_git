class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(self.name.title() + " " + self.cuisine_type.title())
    
    def open_restaurant(self):
        print(self.name.title() + " is open.")

kfc = Restaurant('kfc', 'snack')
libai = Restaurant('libai', 'chinese')
grandma = Restaurant('grandma', 'hangzhou')

kfc.describe_restaurant()
libai.describe_restaurant()
grandma.describe_restaurant()