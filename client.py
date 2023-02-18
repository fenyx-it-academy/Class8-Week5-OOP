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
                return f'{amount} was sent from {self.account_number} to {receiver_account_number}'

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
        
        # total_points_collexted is an attributes that the total loyalty points collected by the customer since creating the account.
        self.total_points_collected = loyalty_point
        
        if self.total_points_collected >= 1000:
            self.upgrade_to_VIP()
        elif self.loyalty_point >= 50:
            self.claim_100eur_bonus()

    def add_deposit(self, amount):
        super().add_deposit(amount)
        loyalty_point_earned = amount / 10
        self.loyalty_point += loyalty_point_earned
        self.total_points_collected += loyalty_point_earned
        print(f"Congratulations! You've earned {loyalty_point_earned} loyalty points and received a deposit of {amount}. New balance: {self.balance}")
        
        # if total loyalty points collected is more than 1000, upgrade to VIP CLient
        if self.total_points_collected >= 1000:
            self.upgrade_to_VIP()
        # otherwise, if current loyalty points are more than 50, claim 100eur bonus.
        elif self.loyalty_point >= 50:
            self.claim_100eur_bonus()
        
    # a function that keeps claiming 100eur bonus until current loyalty points are less than 50
    def claim_100eur_bonus(self):
        while self.loyalty_point >= 50:
            self.balance += 100
            self.loyalty_point -= 50
            print(f"Congratulations! You've claimed 100 EUR. You now have {self.loyalty_point} loyalty points. Balance: {self.balance}")
        
    def upgrade_to_VIP(self, vip_level = "bronze"):
        if self.total_points_collected >= 1000:
            account_number = self.account_number
            self.__class__ = VipClient      # Change the class to VipClient class
            self.__init__(self.name, self.surname, self.balance, vip_level, self.children_number, self.gender)
            self.account_number = account_number    # keep the account number
            Client.num_client -= 1                  # remove the duplicated client count from the total number of clients
            Client.total_balance -= self.balance    # remove the duplicated balance from the total balance
            self.loyalty_point = None
            self.total_points_collected = None
            print(f"{self.name} {self.surname} is now a VIP client, level {self.vip_level}")
        else:
            print("Not enough loyalty points!")
    
        
class VipClient(Client):
    gold_rate = 0.03
    silver_rate = 0.02
    bronze_rate = 0.01

    def __init__(self, name, surname, balance, vip_level = 'bronze', children_number=0, gender='uncertain'):
        super().__init__(name, surname, balance, children_number, gender)
        if vip_level in ['bronze', 'silver', 'gold']:
            self.vip_level = vip_level
        else:
            self.vip_level = 'bronze' # defailt VIP level is bronze
    
    def add_deposit(self, amount):
        if self.vip_level == 'bronze':
            amount += amount * self.bronze_rate
        elif self.vip_level == 'silver':
            amount += amount * self.silver_rate
        elif self.vip_level == 'gold':
            amount += amount * self.gold_rate
        super().add_deposit(amount)
        


clt1 = Premium_Client('John', 'Smith', 10000, 900)
clt2 = Premium_Client('Jane', 'Doe', 20000, 0)
clt3 = Client('Blake', 'Jack', 30000)

print("-----------------------------------")
print('Adding a deposit to the premium client to trigger the 1000 total royalty points collected:')
clt1.add_deposit(2000)
print(type(clt1))

print("-----------------------------------")
print('Adding a deposit to the VIP bronze client:')
clt1.add_deposit(1200)
print(f'{clt1.name} now has {clt1.balance}')

print("-----------------------------------")
print('Sending money from a VIP client to a normal client')
print(f'{clt1.name} before had {clt1.balance}')
print(f'{clt3.name} before had {clt3.balance}')
print(clt1.send_money(clt3.account_number, 1000))
print(f'{clt1.name} now has {clt1.balance}')
print(f'{clt3.name} now has {clt3.balance}')
