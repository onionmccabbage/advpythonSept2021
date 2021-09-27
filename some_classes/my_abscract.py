# abc is the abstract base class
from abc import ABCMeta, abstractmethod, abstractproperty

# we can declare an abstract top-level class
class Shape():
    __metaclass__ = ABCMeta
    @abstractmethod
    def display(self):
        pass # we give it NO body
    @abstractproperty
    def name(self):
        pass # again declare NO body