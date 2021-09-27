from my_abscract import Shape

class Circle(Shape):
    def __init__(self, name):
        self.name = name # use the setter method
    def display(self):
        print('Circle {}'.format(self.name))
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        # check name is within bounds
        if type(new_name) == str and new_name != '':
            self.__name = new_name
        else:
            self.__name = 'default'

if __name__ == '__main__':
    c = Circle('meridian')
    c.display()