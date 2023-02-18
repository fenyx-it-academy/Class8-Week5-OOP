import random


class Client:
    bonus = 300
    interest_rate = 1.05
    num_client = 0
    total_balance = 0

    def __init__(self, name, surname, balance, children_number=0, gender='uncertain'):
        self.name = name
        self.surname = surname
        self.balance = balance
        self.email = f'{name.lower()}.{surname}@gmail.com'
        self.gender = gender
        self.account_number = (f"ABN{random.randint(1000000000,9999999999)}")
        self.children_number = children_number
        Client.num_client += 1
        Client.total_balance += balance

        if children_number > 0:
            self.add_child_bonus()

    def add_deposit(self, amount):
        self.balance += amount
        Client.total_balance += amount
        return (f'Your balance is updated , {self.balance}')

    def withdraw_deposit(self, amount):
        self.balance -= amount
        Client.total_balance -= amount
        return(f"Your balance is updated,  {self.balance}")

    def payment_rent(self, rent):
        self.balance -= rent
        return(f'Your rent is paid , {self.balance}')

    def send_money(self, receiver_account_number, amount):
        if self.balance < amount:
            return 'balance is not enough'
        else:
            client_object = [obj for obj in globals().values() if isinstance(
                obj, Client) and obj.account_number == receiver_account_number]
            if len(client_object) == 0:
                print('client not found')

            else:
                reciever_object = client_object[0]
                reciever_object.balance += amount
                self.balance -= amount

    def add_child_bonus(self):
        self.add_deposit(self.children_number * Client.bonus)

    def add_interest(self):
        self.balance *= Client.interest_rate

    @classmethod
    def average_balacance(cls):
        if cls.num_client == 0:
            return 0
        else:
            return cls.total_balance / cls.num_client


class Premium_Client(Client):
    def __init__(self, name, surname, balance, loyalty_point, children_number=0, gender='uncertain'):
        super().__init__(name, surname, balance, children_number, gender)
        self.loyalty_point = loyalty_point        

        self.vip_class()     

    def add_child_bonus(self):
        super().add_deposit(self.children_number * Client.bonus)

    def add_deposit(self, amount):
        super().add_deposit(amount)
        loyalty_point_earned = amount / 10

        self.loyalty_point += loyalty_point_earned

        if self.loyalty_point >= 50:
            self.balance += 100
            self.loyalty_point -= 50
            return(f"Congratulations! You've earned {loyalty_point_earned} loyalty points and received a bonus of {amount}. New balance: {self.balance}")

    def vip_class(self):
        if self.loyalty_point >= 1000:
            self.__class__ = VIP         

class VIP(Premium_Client):

    gold = 0.03
    silver = 0.02
    bronz = 0.01

    def __init__(self, name, surname, balance, loyalty_point, type_of_vip = 'null',children_number=0, gender='uncertain'):
        super().__init__(name, surname, balance, loyalty_point, children_number=0, gender='uncertain')
        self.type_of_vip = type_of_vip

    def add_deposit(self, amount):
        if self.loyalty_point >= 3000:
            super().add_deposit(amount)
            self.balance += VIP.gold
            print ('You are VIP/Gold client')

        elif 2000 <= self.loyalty_point < 3000:
            super().add_deposit(amount)
            self.balance += VIP.silver
            print ('You are VIP/Silver client')

        elif 1000 <= self.loyalty_point < 2000:
            super().add_deposit(amount)
            self.balance += VIP.bronz
            print ('You are VIP/Bronz client')   

        return(f"Your balance is updated,  {self.balance}") 


pclt1 = Client('Jane', 'Lutter', 12000, 1000)
pclt2 = Premium_Client('Tom', 'Poli', 15000, 1000)

print(pclt2.add_deposit(700)) 
print(pclt2.loyalty_point)
print(pclt2.add_deposit(10000))
print(pclt2.loyalty_point)
print(pclt2.add_deposit(10000))
print(pclt2.loyalty_point)
print(pclt2.add_deposit(10000))
print(pclt2.loyalty_point)
 

 

 

 
