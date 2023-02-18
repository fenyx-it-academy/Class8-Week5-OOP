import random


class Client:
    def __init__(self, name, surname, balance, gender, account_number, children_number, loyalty_point=0):
        self.name = name
        self.surname = surname
        self.balance = balance
        self.gender = gender
        self.account_number = account_number
        self.children_number = children_number
        self.loyalty_point = loyalty_point

    def __str__(self):
        return f'{self.name} {self.surname}, {self.balance}, {self.children_number}'

    def add_deposit(self, amount):
        self.balance += amount

    def send_money(self, other, amount):
        if amount <= self.balance:
            self.balance -= amount
            other.balance += amount
            return True
        else:
            return False

class Premium_Client(Client):
    def __init__(self, name, surname, balance, gender, account_number, children_number, loyalty_point=0):
        super().__init__(name, surname, balance, gender, account_number, children_number, loyalty_point)

    def add_loyalty_point(self, amount):
        self.loyalty_point += amount
        if self.loyalty_point >= 1000:
            self.convert_to_vip()

    def convert_to_vip(self):
        vip_client = VipClient(self.name, self.surname, self.balance, self.gender, self.account_number, self.children_number, self.loyalty_point)
        del self.__dict__
        self.__class__ = vip_client.__class__
        self.__dict__ = vip_client.__dict__

class VipClient(Client):
    def __init__(self, name, surname, balance, gender, account_number, children_number, loyalty_point=0):
        super().__init__(name, surname, balance, gender, account_number, children_number, loyalty_point)
        self.level = self.get_level()
    
    def get_level(self):
        if self.loyalty_point >= 10000:
            return 'Gold'
        elif self.loyalty_point >= 5000:
            return 'Silver'
        else:
            return 'Bronze'
    
    def add_deposit(self, amount):
        if self.level == 'Gold':
            amount *= 1.03
        elif self.level == 'Silver':
            amount *= 1.02
        elif self.level == 'Bronze':
            amount *= 1.01
        self.balance += amount

    def __del__(self):
        self.name = None
        self.surname = None
        self.balance = None
        self.gender = None
        self.account_number = None
        self.children_number = None
        self.loyalty_point = None

if __name__ == '__main__':
    # Example usage
    clt = Client('Ali', 'Ahmed', 7500, 'Male', 1001, 1)
    print(clt)

    pclt = Premium_Client('Danial', 'Melmav', 15000, 'Male', 1002, 2)
    print(pclt)

    pclt.add_deposit(1000)
    print(pclt.balance)
    print(pclt.loyalty_point)

    pclt.add_loyalty_point(400)
    print(pclt.loyalty_point)

    pclt.add_loyalty_point(600)
    print(pclt.level)

    vclt = zip
