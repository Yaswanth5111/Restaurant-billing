from datetime import date #to get today date
import time # to get time
import os #to print new screen(terminal)

today_date = date.today()
food={"STATERS":"","Tomato soups":89,"corn soups":89,"Chilli chicken":159,"Chilli paneer":129,"chicken tandoori(half)":269,"Chicken tandoori(full)":499,"BIRYANIS":"","Veg biryani":"154","Egg biryani":170,"Chicken briyani":210,"Mutton biryani":269,"Prawns biryani":399,"Andhra meals":119,"BEVERAGES":"","soft drink":20,"Lassi":40}
food_items={"Tomato soups":89,"corn soups":89,"Chilli chicken":159,"Chilli paneer":129,"chicken tandoori(half)":269,"Chicken tandoori(full)":499,"Veg biryani":"154","Egg biryani":170,"Chicken briyani":210,"Mutton biryani":269,"Prawns biryani":399,"Andhra meals":119,"soft drink":20,"Lassi":40}
class Food_items:
    def _init_(self):
        self.total_orders={}
        self.today_date=today_date
    def update(self,order):
        for i in order:
            if i in self.total_orders:
                self.total_orders[i]+=order[i]
            else:
                self.total_orders[i]=order[i]
    def collection(self):
        items=list(food_items.keys())
        prices=list(food_items.values())
        total=0
        print("Date:",self.today_date,"\n")
        print("ITEM\t\t\tQUANTITY\tPrices\n")
        for i in self.total_orders:
            total+=prices[i]*self.total_orders[i]
            d=23-len(items[i])
            print(items[i]," "*d,self.total_orders[i],"\t\t",prices[i]*self.total_orders[i])
            print()
        print("GST 2%:\t\t\t\t\t",0.02*total)
        print("Total:\t\t\t",sum(self.total_orders.values()),"\t\t",total+0.02*total)
        input("Press Enter to continue...")
        print("\n")
    def records(self):
        items=list(food_items.keys())
        prices=list(food_items.values())
        total=0
        file1=open("D:\python"+str(self.today_date)+".txt","w")
        file1.write("Date:"+str(self.today_date)+"\n")
        file1.write("ITEM\t\t\tQUANTITY\tPrices\n")
        for i in self.total_orders:
            total+=prices[i]*self.total_orders[i]
            d=23-len(items[i])
            file1.write(items[i]+" "*d+str(self.total_orders[i])+"\t\t"+str(prices[i]*self.total_orders[i])+"\n")
        file1.write("GST 2%:\t\t\t\t\t"+str(0.02*total)+"\n")
        file1.write("total:\t\t\t"+str(sum(self.total_orders.values()))+"\t\t"+str(total+(0.02*total)))
        file1.close()

restuarent=Food_items()
def display_menue():
    print("id\t","item\t\t\t\t","price")
    items=list(food_items.keys())
    prices=list(food_items.values())
    order={}
    j=1
    for i in food:
        if food[i]=="":
            print(i)
            print()
        else:
            d=30
            p=30-len(i)
            print(j,"\t",i," "*p,food[i])
            j+=1
            print()
    
    print("Enter 0 to print bill")
    while 1:
        print("Enter item number")
        c=int(input())
        if c==0:
            break
        print("enter quantity")
        quant=int(input())
        if quant==0:
            continue
        if c-1 in order:
            order[c-1]+=quant
        else:
            order[c-1]=quant 
    total=0
    curr_time = time.localtime()
    ind_time= time.strftime("%H:%M:%S", curr_time)
    print("\n\n")
    os.system("cls")
    print("Date:",today_date,"\tTime:",ind_time)
    print("\n")
    print("ITEM\t\t\tQUANTITY\tPrices\n")
    for i in order:
        total+=int(prices[i])*order[i]
        d=23-len(items[i])
        print(items[i]," "*d,order[i],"\t\t",prices[i]*order[i])
        print()
    print("GST 2%:\t\t\t\t\t",0.02*total)
    print("total:\t\t\t",sum(order.values()),"\t\t",total+0.02*total)
    input("Press Enter to continue...")
    print("\n\n")
    restuarent.update(order)
    

def add_item():
    print("Enter the dish name: ")
    item=input()
    print("Enter the price of the dish")
    price=int(input())
    food_items[item]=price
    food[item]=price
    input("Press Enter to continue...")
    print("\n")
    

def previous_records():
    n=input("Enter the date you want to the see the billing records of that day format(yyyy-mm-dd): ")
    os.system("cls")
    if os.path.exists("D:\python"+n+".txt"):
        file1=open("D:\python"+n+".txt","r")
        text=file1.read()
        print(text)
        input("Press Enter to continue...")
        print("\n")
        file1.close()
    else:
        print("sorry, records of this date is not found")

def menue():
    choice=0
    while choice!=5:
        print("1:Take new order\n")
        print("2:Add a new item to restuarent\n")
        print("3:Items served today\n")
        print("4:Search for records of a date\n")
        print("5:Exit\n")
        choice=int(input())
        if(choice==1):
            os.system("cls") #new terminal
            display_menue()
        elif choice==2:
            os.system("cls")
            add_item()
        elif choice==3:
            os.system("cls")
            restuarent.collection()
        elif choice==4:
            os.system("cls")
            previous_records()
        elif choice==5:
            restuarent.records()
        else:
            print("Enter a valid option from 1-4")

menue()