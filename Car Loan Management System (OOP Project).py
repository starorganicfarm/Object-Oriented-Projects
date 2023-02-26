#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Car Loan Management System
class Customer:
    def __init__(self,name,address,phone_no):
        self.name=name
        self.address=address
        self.phone_no=phone_no   
    def details(self):
        print(f"Customer Name:{self.name} \nAddress:{self.address} \nPhone Number:{self.phone_no}")
        
class Login(Customer):
    def request(self):
        print("Your Account has been made. Now you can Deal with Vehicles")

class Vehicle(Customer):
    def __init__(self,name,address,phone_no,corolla_price,city_price,civic_price,year1,year2):
        Customer.__init__(self,name,address,phone_no)
        self.corolla_price=corolla_price
        self.city_price=city_price
        self.civic_price=civic_price
        self.year1=year1
        self.year2=year2
        self.new_price=0
        self.new_percent=0
        self.new_year=0
    def Cars(self):
        a=str(input("Enter which brand vehicle do you want(Corolla or City or Civic): "))
        if a=="Corolla" or a=="COROLLA":
                print(f"The Price of COROLLA is Rs {self.corolla_price}")
                self.new_price=self.corolla_price
        elif a=="City" or a=="CITY":
                print(f"The Price of CITY is Rs {self.city_price}")
                self.new_price=self.city_price
        elif a=="Civic" or a=="CIVIC":
                print(f"The Price of CIVIC is Rs {self.civic_price}")
                self.new_price=self.civic_price
    def Minimum(self):
        c=int(input("Enter Minimum Amount: "))
        print(f"You pay minimum Amount Rs {c}")
        self.new_percent=c
    def Years(self):
        b=int(input("Select Tenure(5 or 7)years: "))
        if b==5:
                print(f"You select Tenure for {self.year1} years.")
                self.new_year=b
        elif b==7:
                print(f"You select Tenure for {self.year2} years.")
                self.new_year=b
    def calculate(self):
        res=(self.new_price-(self.new_percent))/(self.new_year*12)
        print(f"Your monthly payment is Rs {int(res)}")

class Approval(Vehicle):
    def result(self):
        print("Your Car Loan has been Approved!!!")

obj2=Login("Bilal Ahmed","R-35 FB Area Block 8 Gulshan-e-Yaseen Karachi","0300-2345674")
obj2.request()
obj=Vehicle("Bilal Ahmed","R-35 FB Area Block 8 Gulshan-e-Yaseen Karachi","0300-2345674",2000000,3000000,3500000,5,7)
print("\n")
obj.details()
print("\n")
obj.Cars()
print("\n")
obj.Minimum()
print("\n")
obj.Years()
print("\n")
obj.calculate()
print("\n")
obj1=Approval("Bilal Ahmed","R-35 FB Area Block 8 Gulshan-e-Yaseen Karachi","0300-2345674",2000000,3000000,3500000,5,7)
obj1.result()

