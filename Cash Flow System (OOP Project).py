#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import tkinter 
from tkinter import messagebox

class Hypermart:
    def __init__(self,window):
        self.window=window
        self.window.title("Hypermart Cash Flow System")
        self.window.geometry("1370x570")
        
        self.title=Label(window,text=" HYPERMART CASH FLOW SYSTEM ",bg="orange",fg="white",font=("Arial",40, "bold","italic"))
        self.title.pack(side=TOP,fill=X)

    #==================================================================================================================#        
        
class Initial_Balance(Hypermart):
    def __init__(self,window):
        self.window=window
        self.lst=[]
        self.frame=Frame(window,bd=4,relief=RIDGE,bg="Crimson")
        self.frame.place(x=30,y=100,width=400,height=390) 
        
        self.title1 = Label(self.frame,text="INITIAL BALANCE ",bg="Crimson",fg="white",font=("Arial",15, "bold","italic"))
        self.title1.grid(row=0,columnspan=2,padx=100,pady=10)
        
        self.label1 = Label(self.frame,text="Beginning Cash  ",bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
        self.label1.grid(row=1,column=0,pady=5,padx=15)     
        self.entry1=Entry(self.frame,font=("Arial",10,"italic"))
        self.entry1.grid(row=1,column=1)
            
        self.label2 = Label(self.frame,text="Cash Sales  ",bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
        self.label2.grid(row=2,column=0,pady=5)
        self.entry2=Entry(self.frame,font=("Arial",10,"italic"))
        self.entry2.grid(row=2,column=1)
        
        self.label3 = Label(self.frame,text="Collections ",bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
        self.label3.grid(row=3,column=0,pady=5) 
        self.entry3=Entry(self.frame,font=("Arial",10,"italic"))
        self.entry3.grid(row=3,column=1)
        
        self.label4 = Label(self.frame,text="Loans ",bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
        self.label4.grid(row=4,column=0,pady=5)
        self.entry4=Entry(self.frame,font=("Arial",10,"italic"))
        self.entry4.grid(row=4,column=1)
        
        self.B1 = tkinter.Button(self.frame,text="TOTAL",bg="Crimson",fg="white",font=("Arial",15, "bold","italic"),command=self.Sub_total1)
        self.B1.grid(row=6,column=1,pady=10)
        
    def Sub_total1(self):
        if self.entry1.get() is '' or self.entry2.get() is '' or self.entry3.get() is '' or self.entry4.get() is '':
            messagebox.showinfo('Warning', 'Empty')
        else:
            try:
                s_total=int(self.entry1.get())
                s_total1=int(self.entry2.get())
                s_total2=int(self.entry3.get())
                s_total3=int(self.entry4.get())

                S1=s_total+s_total1+s_total2+s_total3

                self.lst.append(s_total)
                self.lst.append(s_total1)
                self.lst.append(s_total2)
                self.lst.append(s_total3)
                self.lst.append(S1)

                self.label = Label(self.frame,text="INITIAL BALANCE",bg="Crimson",fg="white",font=("Arial",15, "bold","italic"))
                self.label.grid(row=7,columnspan=2,pady=5)
                self.label = Label(self.frame,text=("Begining Cash :","$",s_total,"/-"),bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
                self.label.grid(row=8,column=0,pady=5)
                self.label = Label(self.frame,text=("Cash Sales :","$",s_total1,"/-"),bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
                self.label.grid(row=8,column=1,pady=5)
                self.label = Label(self.frame,text=("Collections :","$",s_total2,"/-"),bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
                self.label.grid(row=9,column=0  ,pady=5)
                self.label = Label(self.frame,text=("Loans :","$",s_total3,"/-"),bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
                self.label.grid(row=9,column=1,pady=5)
                self.label = Label(self.frame,text=("Sub Total:","$",S1,"/-"),bg="Crimson",fg="white",font=("Arial",13, "bold","italic"))
                self.label.grid(row=10,columnspan=2,pady=5) 
            except ValueError:
                messagebox.showinfo('Warning', 'Wrong Data Input')
 
    #==================================================================================================================#      

class Expenses(Hypermart):
    def __init__(self,window):
        self.window=window
        
        self.lst1=[]
        self.frame1=Frame(window,bd=4,relief=RIDGE,bg="Crimson")
        self.frame1.place(x=475,y=100,width=400,height=390) 
        
        self.title1 = Label(self.frame1,text="EXPENSES ",bg="Crimson",fg="white",font=("Arial",15, "bold","italic"))
        self.title1.grid(row=0,columnspan=2,padx=130,pady=10)
        
        self.label1 = Label(self.frame1,text=" Equipments ",bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
        self.label1.grid(row=1,column=0,pady=5,padx=15)
        self.entry1=Entry(self.frame1,font=("Arial",10,"italic"))
        self.entry1.grid(row=1,column=1)
      
        self.label2 = Label(self.frame1,text=" Shipping Cost ",bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
        self.label2.grid(row=2,column=0,pady=5)
        self.entry2=Entry(self.frame1,font=("Arial",10,"italic"))
        self.entry2.grid(row=2,column=1)
        
        self.label3 = Label(self.frame1,text="Utilities",bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
        self.label3.grid(row=3,column=0,pady=5) 
        self.entry3=Entry(self.frame1,font=("Arial",10,"italic"))
        self.entry3.grid(row=3,column=1)
        
        self.label4 = Label(self.frame1,text="Payroll ",bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
        self.label4.grid(row=4,column=0,pady=5)
        self.entry4=Entry(self.frame1,font=("Arial",10,"italic"))
        self.entry4.grid(row=4,column=1)
        
        self.B1 = tkinter.Button(self.frame1,text="TOTAL",bg="Crimson",fg="white",font=("Arial",15, "bold","italic"),command=self.Sub_total2)
        self.B1.grid(row=6,column=1,pady=10)
        
    def Sub_total2(self):
        if self.entry1.get() is '' or self.entry2.get() is '' or self.entry3.get() is '' or self.entry4.get() is '':
            messagebox.showinfo('Warning', 'Empty')
        else:
            try:
                s_total4=int(self.entry1.get())
                s_total5=int(self.entry2.get())
                s_total6=int(self.entry3.get())
                s_total7=int(self.entry4.get())

                S2=s_total4+s_total5+s_total6+s_total7

                self.lst1.append(s_total4)
                self.lst1.append(s_total5)
                self.lst1.append(s_total6)
                self.lst1.append(s_total7)
                self.lst1.append(S2)

                self.label = Label(self.frame1,text="EXPENSES",bg="Crimson",fg="white",font=("Arial",15, "bold","italic"))
                self.label.grid(row=7,columnspan=2,pady=5)
                self.label = Label(self.frame1,text=("Equipments :","$",s_total4,"/-"),bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
                self.label.grid(row=8,column=0,pady=5)
                self.label = Label(self.frame1,text=("Shipping Cost :","$",s_total5,"/-"),bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
                self.label.grid(row=8,column=1,pady=5)
                self.label = Label(self.frame1,text=("Utilities :","$",s_total6,"/-"),bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
                self.label.grid(row=9,column=0,pady=5)
                self.label = Label(self.frame1,text=("Payroll :","$",s_total7,"/-"),bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
                self.label.grid(row=9,column=1,pady=5)
                self.label = Label(self.frame1,text=("Sub Total:","$",S2,"/-"),bg="Crimson",fg="white",font=("Arial",13, "bold","italic"))
                self.label.grid(row=10,columnspan=2,pady=5)
            except ValueError:
                messagebox.showinfo('Warning', 'Wrong Data Input')
                

     #==================================================================================================================#      


class Taxes(Hypermart):
    def __init__(self,window):
        self.window=window
        
        self.lst2=[]
        self.frame2=Frame(window,bd=4,relief=RIDGE,bg="Crimson")
        self.frame2.place(x=920,y=100,width=400,height=390) 
        
        self.title1 = Label(self.frame2,text="TAXES ",bg="Crimson",fg="white",font=("Arial",15, "bold","italic"))
        self.title1.grid(row=0,columnspan=2,padx=150,pady=10)
        
        self.label1 = Label(self.frame2,text="Federal Income Tax  ",bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
        self.label1.grid(row=1,column=0,pady=5,padx=15)
        self.entry1=Entry(self.frame2,font=("Arial",10,"italic"))
        self.entry1.grid(row=1,column=1)
      
        self.label2 = Label(self.frame2,text="State Income Tax  ",bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
        self.label2.grid(row=2,column=0,pady=5)
        self.entry2=Entry(self.frame2,font=("Arial",10,"italic"))
        self.entry2.grid(row=2,column=1)
        
        self.label3 = Label(self.frame2,text="Interest Expense ",bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
        self.label3.grid(row=3,column=0,pady=5) 
        self.entry3=Entry(self.frame2,font=("Arial",10,"italic"))
        self.entry3.grid(row=3,column=1)
        
        self.label4 = Label(self.frame2,text="Depreciation Expense ",bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
        self.label4.grid(row=4,column=0,pady=5)
        self.entry4=Entry(self.frame2,font=("Arial",10,"italic"))
        self.entry4.grid(row=4,column=1)
        
        self.B1 = tkinter.Button(self.frame2,text="TOTAL",bg="Crimson",fg="white",font=("Arial",15, "bold","italic"),command=self.Sub_total3)
        self.B1.grid(row=6,column=1,pady=10)
        
    def Sub_total3(self):
        if self.entry1.get() is '' or self.entry2.get() is '' or self.entry3.get() is '' or self.entry4.get() is '':
            messagebox.showinfo('Warning', 'Empty')
        else:
            try:
                s_total8=int(self.entry1.get())
                s_total9=int(self.entry2.get())
                s_total10=int(self.entry3.get())
                s_total11=int(self.entry4.get())

                S3=s_total8+s_total9+s_total10+s_total11

                self.lst2.append(s_total8)
                self.lst2.append(s_total9)
                self.lst2.append(s_total10)
                self.lst2.append(s_total11)
                self.lst2.append(S3)

                self.label = Label(self.frame2,text="TAXES",bg="Crimson",fg="white",font=("Arial",15, "bold","italic"))
                self.label.grid(row=7,columnspan=2,pady=5)
                self.label = Label(self.frame2,text=("Federal Income Tax:","$",s_total8,"/-"),bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
                self.label.grid(row=8,column=0,pady=5)
                self.label = Label(self.frame2,text=("State Income Tax  :","$",s_total9,"/-"),bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
                self.label.grid(row=8,column=1,pady=5)
                self.label = Label(self.frame2,text=("Interest Expense :","$",s_total10,"/-"),bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
                self.label.grid(row=9,column=0,pady=5)
                self.label = Label(self.frame2,text=("Depreciation Expense :","$",s_total11,"/-"),bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
                self.label.grid(row=9,column=1,pady=5)
                self.label = Label(self.frame2,text=("Sub Total:","$",S3,"/-"),bg="Crimson",fg="white",font=("Arial",13, "bold","italic"))
                self.label.grid(row=10,columnspan=2,pady=5)
            except ValueError:
                messagebox.showinfo('Warning', 'Wrong Data Input')
        
   #==================================================================================================================# 
 
class Generate_Receipt():
    def __init__(self,window,init_bal,expen,tax):
        
        self.window=window
        self.init_bal = init_bal
        self.expen = expen
        self.tax = tax
        self.lst = self.init_bal.lst
        self.lst1 = self.expen.lst1
        self.lst2 = self.tax.lst2
        
        self.B1 = tkinter.Button(window,text="REPORT",bg="Crimson",fg="white",font=("Arial",15, "bold","italic"),command=self.show)
        self.B1.pack(side=BOTTOM,pady=20)
        
    def show(self):
        w = Tk()
        w.title('Report')
        w.geometry('1000x450')
        
        self.frame3=Frame(w,bd=4,relief=RIDGE,bg="Crimson")
        self.frame3.place(x=30,y=80,width=940,height=350) 
        
        self.label = Label(w,text="REPORT OF CASH FLOW SYSTEM",bg="Orange",fg="white",font=("Arial",20, "bold","italic"))
        self.label.pack(side=TOP,fill=X)
        self.label1 = Label(w,text="YEARLY REPORT",bg="Orange",fg="white",font=("Arial",15, "bold","italic"))
        self.label1.pack(side=TOP,fill=X)
        
        self.label = Label(self.frame3,text="INITIAL BALANCE",bg="Crimson",fg="white",font=("Arial",15, "bold","italic"))
        self.label.grid(row=0,column=0,pady=5,padx=10) 
        self.label2 = Label(self.frame3,text=("Begining Cash :","$",self.lst[0]),bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
        self.label2.grid(row=1,column=0,pady=5,padx=10)  
        self.label3= Label(self.frame3,text=("Cash Sales :","$",self.lst[1]),bg="Crimson",fg="white",font=("Arial",10,"bold","italic"))
        self.label3.grid(row=2,column=0,pady=5)
        self.label4 = Label(self.frame3,text=("Collections :","$",self.lst[2]),bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
        self.label4.grid(row=3,column=0,pady=5)  
        self.label5= Label(self.frame3,text=("Loans :","$",self.lst[3]),bg="Crimson",fg="white",font=("Arial",10,"bold","italic"))
        self.label5.grid(row=4,column=0,pady=5)
        self.label5= Label(self.frame3,text=("Sub Total:","$",self.lst[4],"/-"),bg="Crimson",fg="white",font=("Arial",15,"bold","italic"))
        self.label5.grid(row=5,column=0,pady=5)
        
        self.label = Label(self.frame3,text="EXPENSES",bg="Crimson",fg="white",font=("Arial",15, "bold","italic"))
        self.label.grid(row=0,column=3,pady=5,padx=150)
        self.label6 = Label(self.frame3,text=("Equipments :","$",self.lst1[0]),bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
        self.label6.grid(row=1,column=3,pady=5,padx=150)  
        self.label7= Label(self.frame3,text=("Shipping Cost :","$",self.lst1[1]),bg="Crimson",fg="white",font=("Arial",10,"bold","italic"))
        self.label7.grid(row=2,column=3,pady=5,padx=150)
        self.label8 = Label(self.frame3,text=("Utilities :","$",self.lst1[2]),bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
        self.label8.grid(row=3,column=3,pady=5,padx=150)  
        self.label9= Label(self.frame3,text=("Payrolls :","$",self.lst1[3]),bg="Crimson",fg="white",font=("Arial",10,"bold","italic"))
        self.label9.grid(row=4,column=3,pady=5,padx=150)
        self.label5= Label(self.frame3,text=("Sub Total:","$",self.lst1[4],"/-"),bg="Crimson",fg="white",font=("Arial",15,"bold","italic"))
        self.label5.grid(row=5,column=3,pady=5,padx=150)

        self.label = Label(self.frame3,text="TAXES",bg="Crimson",fg="white",font=("Arial",15, "bold","italic"))
        self.label.grid(row=0,column=6,pady=5)
        self.label6 = Label(self.frame3,text=("Federal Tax :","$",self.lst2[0]),bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
        self.label6.grid(row=1,column=6,pady=5)  
        self.label7= Label(self.frame3,text=("State Tax :","$",self.lst2[1]),bg="Crimson",fg="white",font=("Arial",10,"bold","italic"))
        self.label7.grid(row=2,column=6,pady=5)
        self.label8 = Label(self.frame3,text=("Interest Expense :","$",self.lst2[2]),bg="Crimson",fg="white",font=("Arial",10, "bold","italic"))
        self.label8.grid(row=3,column=6,pady=5)  
        self.label9= Label(self.frame3,text=("Depreciation Expense :","$",self.lst2[3]),bg="Crimson",fg="white",font=("Arial",10,"bold","italic"))
        self.label9.grid(row=4,column=6,pady=5)
        self.label5= Label(self.frame3,text=("Sub Total:","$",self.lst2[4],"/-"),bg="Crimson",fg="white",font=("Arial",15,"bold","italic"))
        self.label5.grid(row=5,column=6,pady=5)
        
        self.label5= Label(self.frame3,text=("Remaining Balance","$",self.lst[4]-self.lst1[4]-self.lst2[4],"/-"),bg="Crimson",fg="white",font=("Arial",25,"bold","italic"))
        self.label5.grid(row=8,column=3,pady=20)
        
        if (self.lst[4]-self.lst1[4]-self.lst2[4])>=0:
            self.label12= Label(self.frame3,text="You got some Profit ",bg="Crimson",fg="white",font=("Arial",25,"bold","italic"))
            self.label12.grid(row=9,column=3)
        else:
            self.label12= Label(self.frame3,text="You got some Loss ",bg="Crimson",fg="white",font=("Arial",25,"bold","italic"))
            self.label12.grid(row=9,column=3)


window = Tk()
Hyp=Hypermart(window)
IB=Initial_Balance(window)
E=Expenses(window)
T=Taxes(window)
R=Generate_Receipt(window,IB,E,T)
window.mainloop()


# In[ ]:





# In[ ]:




