class Point():
    '''
    Class representing a point in x-y space
    '''
    points = 0 # property of the class (and every instance)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.points += 1 # count how many instances we have
        # self.points = 'another entity entirely'
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x):
        if type(new_x) == int:
            self.__x = new_x
        else:
            raise TypeError
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, new_y):
        if type(new_y) == int:
            self.__y = new_y
        else:
            raise TypeError
    def hypot(self):
        '''
        Derive the hypotenuse from x and y
        '''
        h = (self.x**2 + self.y**2)**0.5
        return h
    def moveBy(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
    def display(self):
        return (self.x, self.y)

if __name__ == '__main__':
    p1 = Point(3,4)
    print(p1.hypot())
    p2 = Point(-3,-4)
    p2.moveBy(4,7)
    print(p2.display())
    # print(Point.points) # 2