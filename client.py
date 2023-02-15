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
        self.total_loyalty_point=loyalty_point
      

    def add_deposit(self, amount):
        super().add_deposit(amount)
        loyalty_point_earned = amount / 10

        self.loyalty_point += loyalty_point_earned
        self.total_loyalty_point += loyalty_point_earned

        while( self.loyalty_point > 50):
            count=self.loyalty_point//50
            self.balance += 100*count
            self.loyalty_point -= 50*count
            print(f"Congratulations! You've earned {loyalty_point_earned} loyalty points and received a bonus of {100*count} , New balance: {self.balance}")
        if self.total_loyalty_point > 1000:

            print("Congratulations! now you are a vip member")
            self.__class__ = VIP
           

      


class VIP(Client):
    def __init__(self, name, surname, balance, loyalty_point, total_loyalty_point,children_number=0, gender='uncertain'):
        
        print("VIP init")
    def add_deposit(self,amount):
     
        loyalty_point_earned = amount / 10

        self.loyalty_point += loyalty_point_earned
        self.total_loyalty_point += loyalty_point_earned
    
        while( self.loyalty_point > 50):
            count=self.loyalty_point//50
            self.balance += 100*count
            self.loyalty_point -= 50*count
            print(f"Congratulations! You've earned {loyalty_point_earned} loyalty points and received a bonus of {100*count} , New balance: {self.balance}")
            

        level="bronz"
        coef=1.01
        if self.total_loyalty_point>2000:
            level="silver"
            coef=1.02
        if self.total_loyalty_point>3000:
            level="gold"
            coef=1.03
        self.balance+=amount*coef
        Client.total_balance+=amount*coef
        return (f'Your balance is updated , {self.balance}. Because of you are a {level} member, you earn extra {amount*(coef-1):.2f} money')


pclt = Premium_Client('Danial', 'Melmav', 1500, 120)
clt= Client("john", "smith",7000,3,"man")

clt2= Client("Jane", "doe", 2000)
pclt2 = Premium_Client('Danial2', 'Melmav2', 15000, 0)
pclt3 = Premium_Client('Danial', 'Melmav', 15000, 0)

print(pclt.add_deposit(500))
print(pclt.balance)
print(pclt.loyalty_point)

print(pclt.total_loyalty_point)







