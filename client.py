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

    def add_deposit_cl(self, amount):
        self.balance += amount
        Client.total_balance += amount
        return (f'Dear {self.name}. Your balance is updated , {self.balance}')

    def withdraw_deposit(self, amount):
        self.balance -= amount
        Client.total_balance -= amount
        return(f"Dear {self.name}. Your balance is updated,  {self.balance}")

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
        self.add_deposit_cl(self.children_number * Client.bonus)

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
        self.total_point = loyalty_point
        self.level = None

    def add_deposit(self, amount):
        super().add_deposit_cl(amount)
        loyalty_point_earned = amount / 10

        self.loyalty_point += loyalty_point_earned
        self.total_point += loyalty_point_earned

        summa = 0
        while self.loyalty_point >= 50:
            self.balance += 100
            summa += 100
            self.loyalty_point -= 50
        print(f"Congratulations! You've earned {loyalty_point_earned} loyalty points and received a bonus of {summa}. New balance: {self.balance}")

        if self.total_point > 1000 and self.level == None:
            self.level = 'bronze'
            self.__class__ = Vip_Client     # transfer between classes
            print(f'{self.name} are a VIP client now.')



class Vip_Client(Premium_Client):
    def __init__(self, name, surname, balance, loyalty_point, total_point, children_number=0, gender='uncertain'):
        super().__init__(name, surname, balance, loyalty_point, total_point, children_number, gender, )
        self.level = "bronze"


    def add_deposit(self, amount):

        super().add_deposit(amount)
        
        # VIP bonus.
        # set levels of rate:
        coefficient = {
        'bronze': 0.01,
        'silver': 0.02,
        'gold': 0.03
        }

        # bonus payment:
        super().add_deposit_cl(amount * coefficient[self.level])
        print(f'Bonus payment is {amount * coefficient[self.level]}')
        if 2000 < self.total_point < 3000:
            self.level = 'silver'
            print(f'{self.name} have a Silver VIP level.')
        elif self.total_point > 3000:
            self.level = 'gold'
            print(f'{self.name} have a Gold VIP levet.')
        

pclt = Premium_Client('Daniel', 'Melmav', 15000, 0)
pclt1 = Premium_Client('Mary', 'Smith', 3000, 900)
pclt1.add_deposit(2000)
pclt1.add_deposit(10000)
print(pclt1.account_number)
print(pclt1.withdraw_deposit(2000))
pclt.send_money(pclt1.account_number, 5000)
