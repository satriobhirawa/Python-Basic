from menu_item import MenuItem

class Food(MenuItem):
    def __init__(self, name, price, calorie_count):
        # Using super() call __init__() from the parent class
        super().__init__(name, price)
        
        # Delete the following 2 lines
        
        
        self.calorie_count = calorie_count
    
    def info(self):
        return self.name + ': $' + str(self.price) + ' (' + str(self.calorie_count) + 'kcal)'
    
    def calorie_info(self):
        print('kcal: ' + str(self.calorie_count))
