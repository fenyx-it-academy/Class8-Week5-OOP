#assignment 1   

import random  

class Client : 
    total_balance = 0
    def __init__(self , first_name , last_name ,balance  ,loyalty_point, gendel ="uncertain" ) : 
        self.first_name = first_name 
        self.last_name = last_name 
        self.email = f"{first_name}{last_name}@company.com"
        self.acount_number = (f"ABN{random.randint(1000000000,9999999999)}") 
        self.balacne = balance 
        self.loyalty_point =loyalty_point
        
        

    def increase(self , amount) :  
        self.balacne += amount 
        Client.total_balance += amount 
        return (f"Your balance is updated , {self.balacne}") 

    def decrease(self,amount):
        self.balacne -= amount 
        Client.total_balance -= amount 
        return (f"Your balance is updated , {self.balacne}")



    def send_money(self , receive_account_number ,amount) : 

        if self.balacne < amount :
            return " balance is not enough "
        else : 
            
            client_object = [obj for obj in globals().values() if isinstance(obj,Client) and obj.acount_number == receive_account_number]
            if len(client_object) == 0 : 
                print('client not found')

            else : 

                reciever_object = client_object[0]
                reciever_object.balacne += amount
                self.balacne -= amount



client1 = Client("John" , "wessem" , 1,100)
client2 = Client("Wendy" , "asber" , 2,2000)
client3 = Client("Reacher" , "wels" ,6, 6000)




print(client1.first_name)
print(client1.email)
print(client1.increase(500))
print(client2.decrease(500))
client3.send_money(client1.acount_number , 500)
print(client3.balacne , "\t",client1.balacne)
print(client1.send_money(client2.acount_number,5000))



class premium_client(Client):
    def __init__(self, first_name, last_name, balance, loyalty_point, gendel="uncertain"):
        super().__init__(first_name, last_name, balance, loyalty_point, gendel)


    def add_deposit(self , amount):
        super().increase(amount)
        loyalty_point_earned = amount / 10
        self.loyalty_point = loyalty_point_earned + self.loyalty_point


        if self.loyalty_point > 1000 : 
            VIP_Init = Vip(self.first_name,self.last_name,self.balacne,self.loyalty_point)
            VIP_Init.add_deposit(amount)
           



class Vip(Client) : 
    def __init__(self, first_name, last_name, balance, loyalty_point, gendel="uncertain"):
        super().__init__(first_name, last_name, balance, loyalty_point, gendel)
  



    def add_deposit(self,amount) :
        if self.loyalty_point > 1000 and self.loyalty_point < 1500 : 
            print("you are in bronze level ")
            self.balacne += amount *0.01
            self.loyalty_point -= 50
            print(f"Congratulations! You'r loyalty points become {self.loyalty_point}  and received a bonus of {amount}. New balance: {self.balacne}")
        elif self.loyalty_point > 1500 and self.loyalty_point < 2000 : 
            print("you are in the silver level")
            self.balacne += amount*0.02
            self.loyalty_point -=50
            print(f"Congratulations!You'r loyalty points become {self.loyalty_point} and received a bonus of {amount}. New balance: {self.balacne}")
        elif self.loyalty_point > 2000 :
            print("you are in the gold level")
            self.balacne += amount*0.03
            self.loyalty_point -=50
            print(f"Congratulations! You'r loyalty points become  {self.loyalty_point}  and received a bonus of {amount}. New balance: {self.balacne}")


 

client4 = premium_client("Oliver" , "Declan" , 10000 , 1600)
client5 = premium_client("Aurora" , "Hazel" , 10000 , 1100)
client6 = premium_client("Emma" , "Elijah" , 10000 , 2200)


print(client4.balacne)
print(client5.email ,"\n ******************* \n", client5.acount_number)
client5.send_money(client4.acount_number , 5000)
client6.send_money(client1.acount_number , 1000)
print(client6.balacne , "*******************************\t*********************************" , client1.balacne)
print(client4.balacne , "-----------------------------\t------------------------------ ", client5.balacne )
client4.add_deposit(1000)
client5.add_deposit(500)
client6.add_deposit(500)


