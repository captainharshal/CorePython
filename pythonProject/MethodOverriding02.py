# Polymorphism with Inheritance:

class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay

    def get_pay(self):
        return self.base_pay


class SalesEmployee(Employee):
    def __init__(self, name, base_pay, sales_incentive):
        self.name = name
        self.base_pay = base_pay
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return self.base_pay + self.sales_incentive


if __name__ == '__main__':
    john = SalesEmployee('John', 5000, 1500)
    print(john.get_pay())

    jane = Employee('Jane', 5000)
    print(jane.get_pay())





# Polymorphism with Advanced Method Overriding Example:


import re

class Parser:
    def __init__(self, text):
        self.text = text

    def email(self):
        match = re.search(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', self.text)
        if match:
            return match.group(0)
        return None

    def phone(self):
         match = re.search(r'\d{3}-\d{3}-\d{4}', self.text)
         if match:
             return match.group(0)
         return None

    def parse(self):
        return {
          'email': self.email(),
          'phone': self.phone()
        }


class UkParser(Parser):
    def phone(self):
        match = re.search(r'(\+\d{1}-\d{3}-\d{3}-\d{4})', self.text)
        if match:
            return match.group(0)
        return None


if __name__ == '__main__':
    s = 'Contact us via 408-205-5663 or email@test.com'
    parser = Parser(s)
    print(parser.parse())

    s2 = 'Contact me via +1-650-453-3456 or email@test.co.uk'
    parser = UkParser(s2)
    print(parser.parse())





# Polymorphism with Overriding Attributes Example:


import re


class Parser:
    phone_pattern = r'\d{3}-\d{3}-\d{4}'

    def __init__(self, text):
        self.text = text

    def email(self):
        match = re.search(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', self.text)
        if match:
            return match.group(0)
        return None

    def phone(self):
        match = re.search(self.phone_pattern, self.text)
        if match:
            return match.group(0)
        return None

    def parse(self):
        return {
            'email': self.email(),
            'phone': self.phone()
        }


class UkParser(Parser):
    phone_pattern = r'(\+\d{1}-\d{3}-\d{3}-\d{4})'


if __name__ == '__main__':
    s = 'Contact us via 408-205-5663 or email@test.com'
    parser = Parser(s)
    print(parser.parse())

    s2 = 'Contact me via +1-650-453-3456 or email@test.co.uk'
    parser = UkParser(s2)
    print(parser.parse())