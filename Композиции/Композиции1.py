class Profile:
    def __init__(self, name, last_name, age, passport):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.passport = passport

    def print_info(self):
        print(f'Name: {self.name}\n'
              f'Lastname: {self.last_name}\n'
              f'Age: {self.age}\n'
              f'passport: {self.passport}\n')


class Address:
    def __init__(self, city, street, zipcode):
        self.city = city
        self.street = street
        self.zipcode = zipcode


class Role:
    def __init__(self, role, hours_worked):
        self.role = role
        self.hours_worked = hours_worked


class BankAccount:
    def __init__(self, card_number, balance):
        self.card_number = card_number
        self.balance = balance


class Order:

    def __init__(self):
        self.item = None
        self.date = None
        self.delivery = None
        self.price = None

    def set_all(self, item, date, delivery, price):
        self.item = item
        self.date = date
        self.delivery = delivery
        self.price = price

def usr_check():
    user = Order(None, None, None, None, None)
    user.check_info()
    user.create_address()
    user.create_role('Account', 17)
    user.create_bank_account('1717', 100)
    user.create_order('', '10.12.2022', 'kv', 777)