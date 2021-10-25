# this code is in the calculator.py file

class Calculator:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        """ Addition """
        return self.first + self.second

    def subtract(self):
        """ Subtraction """
        return self.first - self.second