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

    def add_deposit(self, amount):
        super().add_deposit(amount)
        loyalty_point_earned = amount / 10

        self.loyalty_point += loyalty_point_earned

        if self.loyalty_point > 50:
            self.balance += 100
            self.loyalty_point -= 50
            return(f"Congratulations! You've earned {loyalty_point_earned} loyalty points and received a bonus of {amount}. New balance: {self.balance}")

# Vip_Client = type('Vip_Client',(Premium_Client,),{'__init__': }) #I would like to do that way, but i couldn't ((
class Vip_Client(Premium_Client):
    def __init__(self, name, surname, balance, loyalty_point, loyalty_level = 'VIP_bronz', children_number=0, gender='uncertain'):
        super().__init__(name, surname, balance, loyalty_point, children_number, gender)
        self.loyalty_level = loyalty_level
        
        
        if self.loyalty_point > 1000:
            self.add_VIP()  
        else:
            self._del_()
        
    def _del_(self):
        self.name = None
        self.surname = None
        self.balance = None
        self.gender = None
        self.account_number = None
        self.children_number = None
        self.loyalty_point = None
    
    def add_VIP(self):
        self.loyalty_level = 'VIP_bronz'
        if self.loyalty_point > 2000:
            self.loyalty_level = 'VIP_silver'
        if self.loyalty_point > 3000:
            self.loyalty_level = 'VIP_gold'
        return(f"Congratulations! You've {self.loyalty_level} client now!")

    def add_deposit(self, amount):
        super().add_deposit(amount)
        if self.loyalty_level == 'VIP_bronz':
            bonus_vip=amount*0.01
            
        elif self.loyalty_level == 'VIP_silver':
            bonus_vip=amount*0.02
            
        elif self.loyalty_level == 'VIP_gold':
            bonus_vip=amount*0.03
            
        self.balance += bonus_vip
        return(f"Congratulations! You've resived {bonus_vip} as a VIP client!")

vclt1= Vip_Client('Maria','Rich', 200000, 3500)
clt = Client('Elen','Ko',3000)
vclt= Vip_Client('Omar','Gugo', 200000, 5000)
pclt = Premium_Client('Danial', 'Melmav', 15000, 0)

# print(pclt.add_deposit(400))
# print(pclt.balance)
# print(pclt.loyalty_point)
# print(vclt1.loyalty_level)
# print (vclt1.add_deposit(5000))
# print(clt.balance)
# print(vclt.balance)
# vclt.send_money(clt.account_number,300)
# print(clt.balance)
# print(vclt.balance)