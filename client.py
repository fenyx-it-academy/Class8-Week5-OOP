# the code works....WOOOHOOOO!!!!! 
# you can copy paste it to VSCode and run it there
# everything seems to work 
# you can read at the end on how to test the code
# espically the part about testing if the premium user
# became a VIP or not
# I've also done the UML, see the UML.md file
# ~Ramy
#
#


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
            client_list = [obj for obj in globals().values() if isinstance(obj, Client)]
            for receiver_client in client_list:
                if receiver_client.account_number == receiver_account_number:
                    receiver_client.balance += amount
                    self.balance -= amount
                    print(f"{amount} is transfer to the {receiver_client.name} from {self.name}")


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
    def __init__(self, name, surname, balance, loyalty_point=0, children_number=0, gender='uncertain'):
        super().__init__(name, surname, balance, children_number, gender)
        self.loyalty_point = loyalty_point

        #if self.loyalty_point > 1000 :
        #    VIP_Init =  Vip_Client(self.name, self.surname, self.balance)
        #    return VIP_Init

    def add_deposit(self, amount):
        super().add_deposit(amount)
        loyalty_point_earned = amount / 10

        self.loyalty_point += loyalty_point_earned

        if 50 <= self.loyalty_point <= 1000:
            self.balance += 100
            self.loyalty_point += 50
            return(f"Congratulations! You've earned {loyalty_point_earned} loyalty points and received a bonus of {amount}. New balance: {self.balance}")

        if self.loyalty_point > 1000 :
            
            VIP_Init =  Vip_Client(self.name, self.surname, self.balance)
            VIP_Init.add_deposit(amount)
            # print ("you are now VIP!")
            return Vip_Client(self.name, self.surname, self.balance) #VIP_Init


            #self.make_into_vip()
            #return super(Vip).Vip_Client(self.name, self.surname, self.balance).Vip.add_deposit(99) # init a VIP client?????
            
            

    #def make_into_vip (self):
    #    print ("You are VIP now!!!")
        #vip = Vip_Client(self.name, self.surname, self.balance)
        

    
        

class Vip_Client (Client):
    def __init__(self, name, surname, balance, level="bronze", children_number=0, gender='uncertain'):
        super().__init__(name, surname, balance, children_number, gender)
        self.level = level
        self.bonus_rates = {'gold': 0.03, 'silver': 0.02, 'bronze': 0.01}

    def add_deposit(self, amount):
        super().add_deposit(amount)
        self.balance += amount * self.bonus_rates[self.level]
        return (f'you got {self.bonus_rates[self.level]} bonus because you are {self.level} level, total balance now is {self.balance}')
    
    def send_money(self, receiver_account_number, amount):
    
       return super().send_money(receiver_account_number, amount)


###################################################################################
###################################################################################
############## testing!!
###################################################################################
###################################################################################

# Init normal clients for testing
client1 = Client("Ramy", "Aaron", 1000, 1)
client2 = Client("Abdulrhman", "A", 1000)
client3 = Client("Burhan", "B", 1000)
client4 = Client("Mohammad", "M", 1000)
client5 = Client("Bahadir", "B", 1000)


# Init premium clients for testing
pClient1 = Premium_Client("Ramy", "Aaron", 1000) #lotalty points var is optional, 0 by default
pClient2 = Premium_Client("Abdulrhman", "A", 100)
pClient3 = Premium_Client("Burhan", "B", 100)
pClient4 = Premium_Client("Mohammad", "M", 100)
pClient5 = Premium_Client("Bahadir", "B", 100)



# Test if the premium user is VIP ?

# Adding loyalty points by making a test deposit
# if we add a large enough test deposit, the user will gain enough loyalty_point to become VIP
# you can test this by making a small deposite (smaller than 20000)
pClient1 = pClient1.add_deposit(20000)


# Now, if the user did in fact become VIP, he should have "level" attribute assigned
# and it should print "bronze"
# however, if the print function below gives an error then the user is NOT VIP
print (pClient1.level )


