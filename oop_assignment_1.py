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

    def payment_rent(self):
        self.balance -= self.rent
        return(f'Your rent is paid , {self.balance}')

    def send_money(self, receiver_account_number, amount):
        if self.balance < amount:
            return 'balance is not enough'
        else:
            client_object = [obj for obj in globals().values() if isinstance(
                obj, (Client,Premium_Client,Vip)) and obj.account_number == receiver_account_number]
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
    def __init__(self, name, surname, balance, loyalty_point,children_number=0, gender='uncertain'):
        super().__init__(name, surname, balance, children_number, gender)
        self.loyalty_point = loyalty_point
        self.total_loyalty_point = 0
    def add_deposit(self, amount):
        super().add_deposit(amount)
        loyalty_point_earned = amount / 10 
        self.loyalty_point += loyalty_point_earned
        self.total_loyalty_point += self.loyalty_point
        if self.total_loyalty_point >= 1000:
            self.vip_client = Vip(self.name, self.surname, self.balance,self.total_loyalty_point)
            self.__class__ = Vip
            return self.vip_client
        else: 
            if self.loyalty_point > 50:
              self.balance += 100
              self.loyalty_point -= 50
            return(f"Congratulations! You've earned {loyalty_point_earned} loyalty points and received a bonus of {amount}. New balance: {self.balance}")
    
class Vip(Client):

    def __init__(self, name, surname, balance,total_loyalty_point, vip_level ="Bronz",children_number=0, gender='uncertain'):
        super().__init__(name, surname, balance,children_number, gender)
        self.vip_level = vip_level
        self.total_loyalty_point = total_loyalty_point
        if self.total_loyalty_point >=2500:
           self.vip_level = "Gold"
        elif self.total_loyalty_point >=2000:
            self.vip_level = "Silver"

    def add_deposit(self, amount):
        super().add_deposit(amount)
        if self.vip_level == "Bronz":
            self.balance += .01*amount
        elif self.vip_level == "Silver":
            self.balance += .02*amount
        elif self.vip_level == "Gold":
            self.balance += .03*amount

# testing the classes
pclt = Premium_Client('Danial', 'Melmav', 5000, 0)
clt = Client("haftom","lemlem",200,0)
vip_clt=pclt.add_deposit(100000)
print(vip_clt.balance)
vip_clt.add_deposit(100)
print(vip_clt.balance)
vip_clt.send_money(clt.account_number, 300)
print(vip_clt.balance)
print(clt.balance)
print(isinstance(vip_clt, Vip))
print(isinstance(vip_clt, Premium_Client))
print(vip_clt.vip_level)

