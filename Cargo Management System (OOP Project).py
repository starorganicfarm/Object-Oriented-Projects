#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Cargo Management System
class Customer:
    def __init__(self,name,address,phone_no):
        self.name=name
        self.address=address
        self.phone_no=phone_no
        
    def details(self):
        print(f"Customer Name:{self.name} \nAddress:{self.address} \nPhone Number:{self.phone_no}")
        
class Login(Customer):
    def request(self):
        print("Your Account has been made. Now you can Deal with Cargo")
        
class Cargo(Customer):
    def __init__(self,name,address,phone_no):
        Customer.__init__(self,name,address,phone_no)
    def Mode(self):
        a=str(input("Select your mode of Cargo(Plane or Ship or Locally): "))
        if a=="Locally" or a=="LOCALLY":
            print("You have selected this Shipment.")
        elif a=="Plane" or a=="PLANE":
            print("You have selected this Shipment.")
        elif a=="Ship" or a=="SHIP":
            print("You have selected this Shipment.")
        else:
            print("WRONG SPELLING OF MODE OF CARGO")
    def Destination(self):
        b=str(input("Select Destination(Dubai or Canada or Pakistan): "))
        if b=="Dubai" or b=="DUBAI":
            print(f"You select your destination.")
        elif b=="Canada" or b=="CANADA":
            print(f"You select your destination.")
        elif b=="Pakistan" or b=="PAKISTAN":
            print(f"You select your destination.")

class Payment(Customer):
    def __init__(self,name,address,phone_no):
        Customer.__init__(self,name,address,phone_no)
        self.weight=0
    def Weightage(self):
        b=int(input("Select Weight: "))
        print(f"You select Weight {b} kg")
        self.weight=b
    def calculate(self):
        res=(self.weight*4000)
        print(f"Your Total Bill is Rs {res}")

print("THANK YOU FOR COMING HERE!!!\n")
obj2=Login("Bilal Ahmed","R-35 FB Area Block 8 Gulshan-e-Yaseen Karachi","0300-2345674")
obj2.request()
obj=Cargo("Bilal Ahmed","R-35 FB Area Block 8 Gulshan-e-Yaseen Karachi","0300-2345674")
print("\n")
obj.details()
print("\n")
obj.Mode()
print("\n")
obj.Destination()  
print("\n")
obj1=Payment("Bilal Ahmed","R-35 FB Area Block 8 Gulshan-e-Yaseen Karachi","0300-2345674")
obj1.Weightage()
print("\n")
obj1.calculate()

