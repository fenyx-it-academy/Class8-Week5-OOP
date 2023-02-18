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
                print(f"You sent {amount} to {reciever_object.name} {reciever_object.surname}, new balance: {self.balance}")

    def add_child_bonus(self):
        self.add_deposit(self.children_number * Client.bonus)

    def add_interest(self):
        self.balance *= Client.interest_rate
        
    def print(self):
        print(self.account_number, self.__class__.__name__, self.balance, sep='\t')

    @classmethod
    def average_balance(cls):
        if cls.num_client == 0:
            return 0
        else:
            return cls.total_balance / cls.num_client


class Premium_Client(Client):
    def __init__(self, name, surname, balance, loyalty_point, children_number=0, gender='uncertain'):
        super().__init__(name, surname, balance, children_number, gender)
        self.loyalty_point = loyalty_point
        self.spent_loyalty_point = 0            

    def add_deposit(self, amount):
        super().add_deposit(amount)
        loyalty_point_earned = amount / 10
        self.loyalty_point += loyalty_point_earned
        if self.loyalty_point + self.spent_loyalty_point >= 1000:
            self.upgradeTo_Vip()

        if self.loyalty_point > 50:
            self.balance += 100
            self.loyalty_point -= 50
            print(f"Congratulations! You've earned {loyalty_point_earned} loyalty points and received a bonus of {amount}. New balance: {self.balance}")
            self.spent_loyalty_point += 50         
        
    def upgradeTo_Vip(self):
        self._vip_level = "Bronz"
        self.__class__ = Vip_Client
        
class Vip_Client(Premium_Client):                  
    def add_deposit(self, amount):
        bonus_ratio = {
            "Bronz": 0.01,
            "Silver": 0.02,
            "Gold": 0.03
        }
        amount += amount * bonus_ratio[self.vip_level]
        super().add_deposit(amount)
      
pclt = Premium_Client('Danial', 'Melmav', 1500,0)
clt = Client('Ahmed', 'Aslan', 3000, 1)

pclt.add_deposit(8000)
pclt.print()
pclt.add_deposit(4000)
pclt.print()
pclt.send_money(clt.account_number, 3000)