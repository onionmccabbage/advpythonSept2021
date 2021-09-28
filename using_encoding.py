# we need a set of classes to encode our data structures
import json

class Item:
    def __init__(self, name, cost):
        self.name = name # these call the setter methods below
        self.cost = cost
    def __str__(self):
        return 'Name: {} Cost: {}'.format(self.name, self.cost)
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        # we should validate!!
        self.__name = new_name
    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self, new_cost):
        # we should validate!!
        self.__cost = new_cost

class ItemEncoder(json.JSONEncoder):
    def default(self, obj): # override the default encoding method of JSONEncoder
        if isinstance(obj, Item):
            # we know it is an 'Item' instance, so we can encode it
            return obj.__dict__ # return a dict of our object
        else:
            # if type is wrong, pass to parent class, which may then raise an exception
            return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    # we need an item
    laptop = Item('laptop', 850)
    # itemJSON = json.dumps(laptop) # normal JSON encoding (fails in this case)
    itemJSON_i = json.dumps(laptop, cls=ItemEncoder) # use our class to encode (as a dict)

    # print(itemJSON, type(itemJSON))
    print(itemJSON_i, type(itemJSON_i))

    # remember we CAN access name-mangled members
    print(laptop._Item__cost) # 850




