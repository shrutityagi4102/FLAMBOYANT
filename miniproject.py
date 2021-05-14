from tkinter import *

def Customer_Sec():
    def menu():
        print("\f")
        print("\t\t\t\t\t MENU")
        print("\t\t\t\t\t~~~~~~")
        print("")
        print("\t\t-------------------------------------------------------")
        print("\t\t|Sr.no.\t\t|Item\t\t\t\t|Cost|")
        for i in range(len(b_sr)):
            if(b_sr[i]!=0):
                print("\t\t|",b_sr[i],"\t\t|",b_type[i],"\t\t\t|",b_cost[i],"|")
                print("\t\t-------------------------------------------------------")    
    def bill():
        menu()
        x=1
        global k
        k=1
        global bwts
        bwts=0
        global lid
        lid=[]
        global kid
        kid=[]
        global quanta
        quanta=[]
        while(x==1):
            k+=1
            global z
            z = int(input("\nENTER THE SERIAL NUMBER OF ITEM WHICH YOU WISH TO ORDER "))
            global y
            y = int(input("ENTER THE QUANTITY YOU NEED FOR THE FOLLOWING FOOD ITEM "))
            for i in range(len(b_sr)):
                if z==b_sr[i]:
                    quanta.append(y)
                    bwts=bwts+y*b_cost[i]
                    lid.append(b_type[i])
                    kid.append(b_cost[i]*y)
            x=int(input("IF YOU WANT TO ORDER AGAIN PRESS 1, OR ELSE PRESS ANYOTHER KEY "))
    def charger(): 
        print("\t\t\t\t\t\t\t FLAMBOYANT")
        print("\t\t\t\t\t\t\t~~~~~~~~~~~~")
        print("\n1. DINE-IN AT OUR RESTAURANT")
        print("2. DELIVERY")
        print("3. TAKE-AWAY ")
        x=int(input("\nENTER YOUR CHOICE NUMBER "))
        global charges
        charges=0
        if(x==1):
            charges=0
        elif(x==2):
            charges=50
        elif(x==3):
            charges=25  
        bill()
        global bt
        bt=bwts+(0.05*bwts)
        global bf
        bf=bt+charges
    
    def loader():
        print("")
        print("\t\t\t\t\t\t LOADING")
        m=1
        for i in range(1,10000001):
            if(m==10000000):
               m=1
               print("\t\t\t\t\t\t .......")
            m+=1
        print("")
        
    def last():
        charger()
        loader()
        print("\f")
        print("\t\t\t\t\t FLAMBOYANT RESTAURANT")
        print("\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("")
        print("\t\t\t\t\t\t TOTAL BILL")
        print("")
        print("")
        print("\t\t-------------------------------------------------------------------------------")
        print("\t\t|Sr.no.\t\t|Item\t\t\t\t|Quantity|\t\t|Cost|")
        for i in range(1,k):
                print("\t\t|",i,"\t\t|",lid[i-1],"\t\t\t|",quanta[i-1],"\t\t\t|",kid[i-1],"|")
                print("\t\t--------------------------------------------------------------------------------")
        print("")
        print("")
        print("\t\tTOTAL OF ITEMS : ",bwts)
        print("\t\tTAX            : ",(0.05*bwts))
        print("\t\tBILL WITH TAX  : ",bt)
        print("\t\tEXTRA CHARGES  : ",charges)
        print("\t\tFINAL BILL     : ",bf)
        print("\t\tTHANK YOU FOR COMING!")
        print("\t\tPLEASE VISIT US SOON")
        print("\tDON'T FORGET SHARE YOUR VALUABLE FEEDBACK WITH US")
    
    b_sr=[1,2,3,4,5,6,7,8,9,10]
    b_type=["FRIES    ","NACHOS   ","WRAP     ","TACOS    ","BURGER   ","PIZZA    ","PASTA    ","NOODLES  ","SHAKE ","ICE CREAM"]
    b_cost=[100,150,200,200,200,300,350,350,50,50]
    last()

def Staff_Sec():
    class Staff:
        def set_name(self,name):
            self.name=name
        def set_designation(self,post):
            self.post=post
        def set_phone(self,number):
            self.number=number
        def set_id(self,member):
            self.member=member
        def set_salary(self,salary):
            self.salary=salary
        def set_pay(self,pay):
            self.pay=pay
        def get_name(self):
            return self.name
        def get_designation(self):
            return self.post
        def get_phone(self):
            return self.number
        def get_id(self):
            return self.member
        def get_salary(self):
            return self.salary
        def get_pay(self):
            return self.pay
    members = ['Rajat Kumar','Kevin Mehta','Zara Shroff','Manoj Kumar','Ketan Parekh','Sangeta Pandey','Vinod Shah','Hira Singh']  
    cost = [225,200,190,160,160,150,150,150]           
    print("| Sr. No  |\tPay(per hour)   |\t  Names\t\t|")
    print("-"*57)
    for i in range(8):
        print("|   {}\t  |\t   {}\t\t|\t{}\t|".format(i+1,cost[i],members[i]))
        print("-"*57)
    
    hour = 0  #Total no of hours present in a month
    print()
    name = input("Enter staff member's name:")
    uname=name.upper()
    s1=Staff()
    if uname=='RAJAT KUMAR':
        s1.set_name(uname)
        s1.set_designation(post='Manager')
        s1.set_phone(9892267193)
        s1.set_id(27)
        s1.set_pay(pay=225)#pay for per hour    
        lst=[[8,0],[8,2],[7,0],[6,0],[8,1],[8,0],[8,3],[7,0],[0,0],[8,1],[0,0],[8,2],[7,0],[8,3],[6,0],
             [8,0],[7,0],[8,3],[7,0],[8,1],[6,0],[0,0],[6,0],[8,1],[8,0],[8,0],[0,0],[8,0],[7,0],[8,0]]
        
        for i in range(30):
            for j in range(2):
                hour = hour + lst[i][j]
        salary = hour*225
        s1.set_salary(salary)
        print(f"Name: {s1.get_name()}")
        print(f"Designation: {s1.get_designation()}")
        print(f"Phone Number: {s1.get_phone()}")
        print(f"ID: {s1.get_id()}")
        print()
        x = input("Do you want to see the salary:")
        if x.upper()=='YES':
            print(f"Salary for this month: {s1.get_salary()}")
            print()
            print("|Date for month\t|  Total Hours\t|\tPay(per day)\t|")
            print("-"*57)
            for i in range(30):
                y = lst[i][0]+lst[i][1] 
                print("|\t{}\t|\t{}\t|\t {}\t\t|".format(i+1,y,y*225))
                print("-"*57)
            print("|\tTotal\t|\t{}\t|\t{}\t\t|".format(hour,salary))
            print("-"*57)
        else:
            pass
    elif uname=='KEVIN MEHTA':
        s1.set_name(uname)
        s1.set_designation(post='Head Chef')
        s1.set_phone(8818263827)
        s1.set_id(25)
        s1.set_pay(pay=200)    
        lst=[[8,0],[8,0],[7,0],[6,0],[8,2],[0,0],[8,3],[7,0],[8,0],[8,1],[7,0],[8,2],[8,0],[8,3],[8,0],
             [8,1],[7,0],[8,3],[8,0],[8,1],[7,0],[0,0],[6,0],[8,1],[8,0],[8,0],[8,3],[8,0],[0,0],[8,0]]
        
        for i in range(30):
            for j in range(2):
                hour = hour + lst[i][j]
        salary = hour*200
        s1.set_salary(salary)
        print(f"Name: {s1.get_name()}")
        print(f"Designation: {s1.get_designation()}")
        print(f"Phone Number: {s1.get_phone()}")
        print(f"ID: {s1.get_id()}")
        print()
        x = input("Do you want to see the salary:")
        if x.upper()=='YES':
            print(f"Salary for this month: {s1.get_salary()}")
            print()
            print("|Date for month\t|  Total Hours\t|\tPay(per day)\t|")
            print("-"*57)
            for i in range(30):
                y = lst[i][0]+lst[i][1] 
                print("|\t{}\t|\t{}\t|\t {}\t\t|".format(i+1,y,y*200))
                print("-"*57)
            print("|\tTotal\t|\t{}\t|\t{}\t\t|".format(hour,salary))
            print("-"*57)
        else:
            pass
        
        
    elif uname=='ZARA SHROFF':
        s1.set_name(uname)
        s1.set_designation(post='Souz Chef')
        s1.set_phone(7732216543)
        s1.set_id(24)
        s1.set_pay(pay=190)    
        lst=[[8,0],[8,1],[8,0],[7,0],[8,1],[8,0],[8,3],[7,0],[0,0],[8,1],[0,0],[8,0],[7,0],[8,1],[7,0],
             [0,0],[7,0],[8,0],[7,0],[8,1],[6,0],[8,2],[6,0],[8,1],[8,2],[8,0],[0,0],[8,0],[7,0],[8,0]]
        
        for i in range(30):
            for j in range(2):
                hour = hour + lst[i][j]
        salary = hour*190
        s1.set_salary(salary)
        print(f"Name: {s1.get_name()}")
        print(f"Designation: {s1.get_designation()}")
        print(f"Phone Number: {s1.get_phone()}")
        print(f"ID: {s1.get_id()}")
        print()
        x = input("Do you want to see the salary:")
        if x.upper()=='YES':
            print(f"Salary for this month: {s1.get_salary()}")
            print()
            print("|Date for month\t|  Total Hours\t|\tPay(per day)\t|")
            print("-"*57)
            for i in range(30):
                y = lst[i][0]+lst[i][1] 
                print("|\t{}\t|\t{}\t|\t {}\t\t|".format(i+1,y,y*190))
                print("-"*57)
            print("|\tTotal\t|\t{}\t|\t{}\t\t|".format(hour,salary))
            print("-"*57)
        else:
            pass
        
    
    elif uname=='MANOJ KUMAR':
        s1.set_name(uname)
        s1.set_designation(post='Waiter')
        s1.set_phone(9819404456)
        s1.set_id(23)
        s1.set_pay(pay=160)    
        lst=[[7,0],[8,1],[7,0],[6,0],[8,1],[8,0],[8,3],[7,0],[8,0],[8,1],[0,0],[8,2],[7,0],[8,0],[0,0],
             [8,0],[7,0],[8,3],[8,0],[8,1],[7,0],[0,0],[6,0],[8,0],[8,3],[8,0],[8,0],[8,0],[7,0],[8,2]]
        
        for i in range(30):
            for j in range(2):
                hour = hour + lst[i][j]
        salary = hour*160
        s1.set_salary(salary)
        print(f"Name: {s1.get_name()}")
        print(f"Designation: {s1.get_designation()}")
        print(f"Phone Number: {s1.get_phone()}")
        print(f"ID: {s1.get_id()}")
        print()
        x = input("Do you want to see the salary:")
        if x.upper()=='YES':
            print(f"Salary for this month: {s1.get_salary()}")
            print()
            print("|Date for month\t|  Total Hours\t|\tPay(per day)\t|")
            print("-"*57)
            for i in range(30):
                y = lst[i][0]+lst[i][1] 
                print("|\t{}\t|\t{}\t|\t {}\t\t|".format(i+1,y,y*160))
                print("-"*57)
            print("|\tTotal\t|\t{}\t|\t{}\t\t|".format(hour,salary))
            print("-"*57)    
        else:
            pass
        
    
    elif uname=='KETAN PAREKH':
        s1.set_name(uname)
        s1.set_designation(post='Waiter')
        s1.set_phone(8187545796)
        s1.set_id(22)
        s1.set_pay(pay=160)    
        lst=[[6,0],[8,1],[8,0],[8,0],[8,3],[0,0],[8,1],[7,0],[0,0],[8,2],[8,0],[0,0],[8,0],[8,0],[8,0],
             [0,0],[8,0],[8,1],[8,0],[8,0],[6,0],[8,2],[7,0],[8,1],[8,1],[8,0],[0,0],[8,0],[7,0],[8,0]]
        
        for i in range(30):
            for j in range(2):
                hour = hour + lst[i][j]
        salary = hour*160
        s1.set_salary(salary)
        print(f"Name: {s1.get_name()}")
        print(f"Designation: {s1.get_designation()}")
        print(f"Phone Number: {s1.get_phone()}")
        print(f"ID: {s1.get_id()}")
        print()
        x = input("Do you want to see the salary:")
        if x.upper()=='YES':
            print(f"Salary for this month: {s1.get_salary()}")
            print()
            print("|Date for month\t|  Total Hours\t|\tPay(per day)\t|")
            print("-"*57)
            for i in range(30):
                y = lst[i][0]+lst[i][1] 
                print("|\t{}\t|\t{}\t|\t {}\t\t|".format(i+1,y,y*160))
                print("-"*57)
            print("|\tTotal\t|\t{}\t|\t{}\t\t|".format(hour,salary))
            print("-"*57)    
            
        else:
            pass
        
    elif uname=='SANGITA PANDEY':
        s1.set_name(uname)
        s1.set_designation(post='Housekeeper')
        s1.set_phone(8838456284)
        s1.set_id(20)
        s1.set_pay(pay=150)    
        lst=[[8,0],[8,1],[0,0],[8,0],[8,1],[8,2],[8,0],[7,0],[8,0],[8,1],[7,0],[8,2],[0,0],[8,1],[7,0],
             [8,0],[6,0],[8,3],[5,0],[8,1],[8,0],[8,0],[6,0],[8,1],[8,2],[8,0],[0,0],[8,0],[8,0],[8,0]]
        
        for i in range(30):
            for j in range(2):
                hour = hour + lst[i][j]
        salary = hour*150
        s1.set_salary(salary)
        print(f"Name: {s1.get_name()}")
        print(f"Designation: {s1.get_designation()}")
        print(f"Phone Number: {s1.get_phone()}")
        print(f"ID: {s1.get_id()}")
        print()
        x = input("Do you want to see the salary:")
        if x.upper()=='YES':
            print(f"Salary for this month: {s1.get_salary()}")
            print()
            print("|Date for month\t|  Total Hours\t|\tPay(per day)\t|")
            print("-"*57)
            for i in range(30):
                y = lst[i][0]+lst[i][1] 
                print("|\t{}\t|\t{}\t|\t {}\t\t|".format(i+1,y,y*150))
                print("-"*57)
            print("|\tTotal\t|\t{}\t|\t{}\t\t|".format(hour,salary))
            print("-"*57)    
        else:
            pass
       
    
    elif uname=='VINOD SHAH':
        s1.set_name(uname)
        s1.set_designation(post='Housekeeper')
        s1.set_phone(9920147923)
        s1.set_id(21)
        s1.set_pay(pay=150)    
        lst=[[7,0],[0,0],[8,0],[6,0],[8,1],[8,0],[8,1],[7,0],[8,0],[8,1],[7,0],[8,2],[8,0],[8,3],[6,0],
             [8,0],[7,0],[8,2],[7,0],[8,1],[6,0],[0,0],[6,0],[8,1],[8,0],[6,0],[8,0],[8,0],[7,0],[7,0]]
        
        for i in range(30):
            for j in range(2):
                hour = hour + lst[i][j]
        salary = hour*150
        s1.set_salary(salary)
        print(f"Name: {s1.get_name()}")
        print(f"Designation: {s1.get_designation()}")
        print(f"Phone Number: {s1.get_phone()}")
        print(f"ID: {s1.get_id()}")
        print()
        x = input("Do you want to see the salary:")
        if x.upper()=='YES':
            print(f"Salary for this month: {s1.get_salary()}")
            print()
            print("|Date for month\t|  Total Hours\t|\tPay(per day)\t|")
            print("-"*57)
            for i in range(30):
                y = lst[i][0]+lst[i][1] 
                print("|\t{}\t|\t{}\t|\t {}\t\t|".format(i+1,y,y*150))
                print("-"*57)
            print("|\tTotal\t|\t{}\t|\t{}\t\t|".format(hour,salary))
            print("-"*57)    
        else:
            pass
       
    elif uname=='HIRA SINGH':
        s1.set_name(uname)
        s1.set_designation(post='Guard')
        s1.set_phone(7776665551)
        s1.set_id(30)
        s1.set_pay(pay=150)    
        lst=[[8,0],[8,2],[7,0],[0,0],[8,0],[8,1],[8,3],[7,0],[0,0],[8,1],[0,0],[8,2],[7,0],[8,3],[6,0],
             [8,0],[7,0],[8,3],[7,0],[8,1],[6,0],[0,0],[6,0],[8,1],[8,1],[8,0],[0,0],[8,2],[7,0],[8,0]]
        
        for i in range(30):
            for j in range(2):
                hour = hour + lst[i][j]
        salary = hour*150
        s1.set_salary(salary)
        print(f"Name: {s1.get_name()}")
        print(f"Designation: {s1.get_designation()}")
        print(f"Phone Number: {s1.get_phone()}")
        print(f"ID: {s1.get_id()}")
        print()
        x = input("Do you want to see the salary:")
        if x.upper()=='YES':
            print(f"Salary for this month: {s1.get_salary()}")
            print()
            print("|Date for month\t|  Total Hours\t|\tPay(per day)\t|")
            print("-"*57)
            for i in range(30):
                y = lst[i][0]+lst[i][1] 
                print("|\t{}\t|\t{}\t|\t {}\t\t|".format(i+1,y,y*150))
                print("-"*57)
            print("|\tTotal\t|\t{}\t|\t{}\t\t|".format(hour,salary))
            print("-"*57)    
        else:
            pass
       
    else:
        print("Entered incorrect name or Plz check the spelling! ")    

def Covid_Test():
    print("\t\t\t\t\t       'COVID - 19'  ")
    print("\t\t\t\t\t 'THE DANGEROUS PANDEMIC!'")
    print("")
    print("\t\t\t We have reached the second wave of corona virus and hence extra precautions are necessary!")
    print("\t\t\t Please cooperate with us for the safety of you and our fellow citizens")
    print("\t\t\t Kindly answer the following questions with YES or NO!")
    print("")
    q1=input("1.Are you suffering from any cold or cough? ")
    q2=input("2.Are you struggling with any breathing issues? ")
    q3=input("3.Have you travelled anywhere recently? ")
    q4=input("4.Have you been in close proximity with any covid patient recently? ")
    
    q1 =q1.upper()
    q2 =q2.upper()
    q3 =q3.upper()
    q4 =q4.upper()
    
    if (q1 == "YES" or q2 == "YES" and q3 == "YES" or q4 == "YES"):
        #AFTER SORRY ENTER CUSTOMERS NAME
        print("\t\t\t\t\t             SORRY!")
        print("\t\t\t\t\tYou might be suffering from COVID-19!")
        print("")
        print("\t\t\t\tPlease do visit the doctor!!!")
        print("\t\t\t\tOR TAKE A RAPID COVID-19 TEST AT FLAMBOYANT COVID CARE NOW!")
        print("\t\t\t\tIf tested negative do visit again!")
        
    else:
        print("\t\t\t\t\t            HURRAY!")
        print("\t\t\t\t\tAs you are not showing any symptoms for covid-19")
        print("")
        print(" \t\t\t\t\t           WELCOME!")
        print("\t\t\t\t\t**STAY SAFE AND ENJOY YOUR VISIT**")

def getvalue():
    print(f"Feedback:{Feedvalue.get()}")    
    with open("projectrecord.txt","a") as f:
        f.write(f"{Feedvalue.get()}\n")

root = Tk()
root.geometry("650x550")
root.title("Flamboyant")

photo = PhotoImage(file ="1.png")
x_label = Label(image = photo)
x_label.pack(side=TOP,anchor="n")

photo1 = PhotoImage(file ="2.png")
x1_label = Label(image = photo1)
x1_label.pack(side=BOTTOM,anchor="n")

f1 = Frame(root,borderwidth=6, bg="grey", relief=SUNKEN)
f1.pack(side=TOP,anchor="n",pady=25)

b1= Button(f1,fg="black",text="Customer",font="arial 12 bold",command=Customer_Sec)
b1.pack(side=TOP,anchor="n")

b2= Button(f1,fg="black",text="Staff",font="arial 12 bold",command=Staff_Sec)
b2.pack(side=TOP,anchor="n")

b3= Button(f1,fg="black",text="Covid Tester",font="arial 12 bold",command=Covid_Test)
b3.pack(side=TOP,anchor="n")

f2 = Frame(root,borderwidth=6, bg="grey", relief=SUNKEN)
f2.pack(side=TOP,anchor="n")

Feedback=Label(f2,fg="black",text="Feedback",font="arial 12 bold").pack(side=TOP,anchor="n")
Feedvalue=StringVar()
feedentry = Entry(f2,textvariable=Feedvalue)
feedentry.pack(side=TOP,anchor="n")

Button(f2,fg="black",text="Submit",font="arial 12 bold",command=getvalue).pack(side=TOP,anchor="n")

root.mainloop()
