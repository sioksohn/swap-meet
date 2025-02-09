from swap_meet.item import Item

class Electronics(Item):    
    def __init__(self, id=None, type="Unknown", condition=0):
        super().__init__(id, condition)
        self.type = type

    def get_category(self):
        return f'{self.__class__.__name__}'

    def __str__(self):
        return super().__str__() + f'. This is a {self.type} device.'

