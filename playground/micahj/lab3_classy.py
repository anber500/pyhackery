from typing import Dict
import json


class SomeCalculatorWithStateAndBehavior(object):
    """
    Im inheriting from object which might be an old way of doing this
    Dont think its necessary. can just go class SomeObject:


    Python lets you do multi inheritance - but it can get gnarly.
    So you could define a class like
    class SomeClass(SomeOtherClassA, SomeOtherClassB, etc):
    These are known as Mixins but inheritance can get pretty hairy when you are
    trying to work out which base class is at play. (MRO - method resolution
    order).
    Just think of tricky c# oo scenarios where you are trying to work
    out which implementation of an interface is doing the work under
    Dependency Injection * (think DI and Strategy Pattern)
    """

    def __init__(self, name: str, thing: Dict, arg3: str):
        """
        This is your constructor
        """
        self.__name = name  # double underscore makes the field private
        self.thing = thing  # this is a public field
        self._arg3 = arg3  # this is a 'protected field' but is publically visible
        # probably useful in sub-classing stuff

    # The little @property thing is called a decoratpr
    # Decorators are functions that wrap another function which means it can
    #
    @property
    def name(self):
        """
        This is a getter for the name property
        This shows you that a 'property' getter is just a function
        Here's a bit of background: https://www.programiz.com/python-programming/property
        :return:
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        You can get and set sorts of weird and wonderful things
        here OR just set the private field value
        :param value:
        :return:
        """
        self.__name == value

    def __gnarly_complex_calculation_in_here(self):
        """
        double underscores say private
        :return:
        """
        return 3  # coz its the magic numer

    def calculate_something(self):
        return self.__gnarly_complex_calculation_in_here()

    def dumpster(self):
        """
        print yourself man
        :return:
        """
        print("dumpster says: ", self.calculate_something())

    def __str__(self):
        """
        This is a built in that lets you
        customise what prints out when you call print(the_instance)
        :return:
        """

        # if you have long lines you can use a tuple like this
        # without the commas and and string operations will join them
        # eg print(tuple_of_strings)
        return ("this is me as a string"
                " normally I will return a thing"
                " that looks like a type name. "
                " comment out __str__ and see what happens."
                " Personally I like to return the class state as json eg"
                " json.dumps(self.__dict__)"
                " hint: if you dont implement this method the result will"
                " look more like this\n"
                " <__main__.SomeCalculatorWithStateAndBehavior object at 0x7fc0305903c8>")


# -----------------------------
# sample usages - dont forget your
# virtual environment if you are running this from
# a command line
# -----------------------------

# use the constructor
calculator = SomeCalculatorWithStateAndBehavior(name="mr-calculator",
                                                thing={"some_key": 7},
                                                arg3="pyhackery is quite fun")
# access the public property - youll get nice intellisense here coz hes a property
print("a:\t", f"My name is {calculator.name}")

# note you can see the protected property but in general the idea is to
# not meddle with the private fields - although I can and I do occasionally
print("b:\t", calculator._arg3)
# a good old function
print("c:\t", calculator.calculate_something())
# use the method we made to print yourself
calculator.dumpster()

print("e:\t", calculator)


# run me
# python -m playground.micahj.lab3_classy