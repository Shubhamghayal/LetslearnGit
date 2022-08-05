

class Atm:
    #static/ class variable
    __counter=1
    
    def __init__(self):
        self.__pin=""           
        self.__balance=0
        self.sno=Atm.__counter
        Atm.__counter += 1             #accessing using class name
        
    
        
        #self.menu()
    
    @staticmethod                 
    def get_counter():                 #dont need self for static 
        return Atm.__counter
    
    @staticmethod
    def set_counter(new):
        if type(new)==int:
            Atm.__counter=new
        else:
            print("not allowed")
            
            
        
    
    def get_pin(self):
        return self.__pin
    
    def set_pin(self,new_pin):
        if new_pin == str:
            self.__pin=new_pin
            print("pin changed")
        else:
            print("not allowed") 
    
    def menu(self):
        user_input=input('''
                         Please Select to Proceed:
                         1. Enter 1 to Create Pin
                         2. Enter 2 to Deposite
                         3. Enter 3 to Withdrdraw
                         4. Enter 4 to Check Balance
                         5. Enter 5 to Exit
                         ''')
        
        if user_input==1:
            Atm.create_pin()
        elif user_input==2:
            Atm.deposite()
        elif user_input==3:
            Atm.withdraw()
        elif user_input==4:
            Atm.check_balance() 
        elif user_input==5:
            print("Thank You")     
              
        
    def create_pin(self):
        self.__pin=input("Enter your pin")
        print("pin saved successfully")
        self.menu()
        
    
    def deposite(self):
        temp=input("Plz Enter your PIN")
        if temp==self.__pin:
            amount=int(input("enter amount"))
            self.__balance +=amount
        else:
            print("invalid PIN")
        self.menu()
        
            
    def withdraw(self):
        temp=input("enter PIN")
        if temp==self.__pin:
            amount=input("enter your amount")
            if amount<self.__balance:
                self.__balance=self.__balance - amount
                print("Operation successful")
            else:
                print("insufficent Balance")
        else:
            print("invalin PIN")   
        self.menu()
        
        
            
    def check_balance(self):
        temp=input("enter pin")
        if temp==self.__pin:
            print("Total balace available="+self.__balance)
        else:
            print("enter coreect pin")
        self.menu()
        
            
            
abc=Atm()
# abc.create_pin()
# abc.deposite()
# abc.withdraw()
# abc.check_balance() 
b=Atm() 
c=Atm()
# print(b.sno)
# print(c.sno)
print(Atm.get_counter())
Atm.set_counter(15)
print(Atm.get_counter())




                                   
        
            
    