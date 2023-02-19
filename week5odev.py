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
    def __init__(self, name, surname, balance, loyalty_point, children_number=0,total_loyality=0, gender='uncertain'):
        super().__init__(name, surname, balance, children_number, gender)
        self.loyalty_point = loyalty_point
        self.total_loyality = total_loyality
    
    

    def add_deposit(self, amount):
        super().add_deposit(amount)
        

        
        loyalty_point_earned = amount / 10
        self.loyalty_point += loyalty_point_earned
        self.total_loyality += loyalty_point_earned
        if self.total_loyality >=1000:
            print(f'you have been upgraded into bronze vip level')
            self.balance += amount*0.01
            print('your balance is now', self.balance)
        elif self.total_loyality >=2000:
            print(f'you have been upgraded into silver vip level')
            self.balance += amount*0.02
            print('your balance is now', self.balance)
        elif self.total_loyality >=3000:
            print(f'you have been upgraded into golden vip level')
            self.balance += amount*0.03
            print('your balance is now', self.balance)
        
        if self.loyalty_point > 50:
            self.balance += 100
            self.loyalty_point -= 50
            return(f"Congratulations! You've earned {loyalty_point_earned} loyalty points and received a bonus of {amount}. New balance: {self.balance}")
            
    def send_money(self, recive_account_number, amount):
        return super().send_money(recive_account_number, amount)
            
            
            
pclt_1 = Premium_Client("Abdulrhman" ,'tabali', 15000,0)
pclt_2 = Premium_Client("Ali" ,'Mohsin', 1000,0)

print(pclt_1.add_deposit(25000))
print(pclt_1.send_money(pclt_2.account_number,250))    
print(f'your final balance is {pclt_1.balance}') 
print(f'your final balance is {pclt_2.balance}')






""" pclt = Premium_Client('Danial', 'Melmav', 15000, 0)

print(pclt.add_deposit(400))
print(pclt.balance)
print(pclt.loyalty_point)
 """
