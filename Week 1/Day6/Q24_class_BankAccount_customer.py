# A bank has many customers and each customer has a bank account
# There are also privileged customers 
# who can earn bonus points for each of their transaction. 
# This scenario is depicted through the below class diagram.
# 30 min

# Customer
# - customer_id
# - customer_name
# - age
# - account
# __init__(customer_id, customer_name, age, account)
# + withdraw(amount)
# + take_card()
# + get_customer_id()
# + get_customer_name()
# + get_age()
# + get_account()
# Account
# - account_type
# - balance
# - min_balance
# __init__(account_type,balance,min_balance)
# + get_account_type()
# + get_balance()
# + get_min_balance()
# + set_balance(balance)
# PrivilegedCustomer
# - bonus_points
# __init__ (customer_id, customer_name, age, account, 
# bonus_points)
# + withdraw(amount)
# + get_bonus_points()
# - increase_bonus()
# OverdrawException
# LimitReachedException

# RULES TO FOLLOW
# ================
# Customer:
# withdraw(amount): This method should reduce the account balance based on the amount withdrawn. 
# Raise the following exceptions based on the given conditions.
# OverdrawException - If the amount to be withdrawn is greater than account balance.
# LimitReachedException - If the balance amount is less than minimum account balance.
# take_card(): Displays the message "Take card out from the ATM".
# PrivilegedCustomer:
# increase_bonus(): If the account balance is greater than 1000, increase the bonus points by 10, else increase it by 2.
# withdraw(amount): Invoke the parent class withdraw() method and increase the bonus points by calling increase_bonus() method, if no exceptions occured.
# If exceptions occur, display relevant messages. Ensure that the card is taken out from the ATM under any situation.

# Write a Python program to create a new PrivilegedCustomer with below details:
# Customer Id: 100
# Customer Name: Gopal
# Age: 43
# Bonus Points: 100
# Account Type: Savings
# Account Balance: 1000
# Account minimum: 500

# The customer should be able to withdraw money and also display the bonus points of the customer after the withdraw.






class OverdrawException(Exception):
    pass
class LimitReachedException(Exception):
    pass

class Customer:
    __customer_id=None
    __customer_name=None
    __age=None
    __account=None
    __balance=None
    def __init__(s,id,name,age,account) -> None:
        s.__customer_id=id
        s.__customer_name=name
        s.__age=age
        s.__account=account
        s.__balance=account.get_balance()
    def withdraw(s,amount):
        if s.__balance<amount:
            raise OverdrawException
        else:
            s.__balance=s.__balance-amount
            s.__account.set_balance(s.__balance)
            print("\n-----------------------")
            print("Withdrawn sucessfully")
            print("------------------------\n")
            if(s.__balance<s.__account.get_min_balance()):
                raise LimitReachedException
    def take_card(s):
        print("Take card out from the ATM")
    def get_customer_id(s):
        return s.__customer_id
    def get_customer_name(s):
        return s.__customer_name
    def get_age(s):
        return s.__age
    def get_account(s):
        return s.__account
    def display(s):
        print()
        print("Customer Id:",s.__customer_id)
        print("Customer Name:",s.__customer_name)
        print("Age:",s.__age)
        print("Account Type:",s.__account.get_account_type())
        print("Account Balance:",s.__balance)
        print("Account minimum:",s.__account.get_min_balance())

class Account:
    __account_type=None
    __balance=None
    __min_balance=None
    def __init__(s,type,balance,min_bal) -> None:
        s.__account_type=type
        s.__balance=balance
        s.__min_balance=min_bal
    def get_account_type(s):
        return s.__account_type
    def get_balance(s):
        return s.__balance
    def get_min_balance(s):
        return s.__min_balance
    def set_balance(s,balance):
        s.__balance=balance

class PrivilegedCustomer(Customer):
    __bonous_point=None
    def __init__(s,id,name,age,account,point) -> None:
        super().__init__(id,name,age,account)
        s.__bonous_point=point

    def get_bonus_points(s):
        return s.__bonous_point
    def increase_bonus(s):
        if(super().get_account().get_balance()>1000):
            s.__bonous_point+=10
        else:
            s.__bonous_point+=2
    def withdraw(s, amount):
        try:
            super().withdraw(amount)
            s.increase_bonus()
        except OverdrawException:
            print("Not enoufgh balance")
        except LimitReachedException:
            print("Balance is less than minimum balance")
    def display(s):
        print()
        print("Customer Id:",super().get_customer_id())
        print("Customer Name:",super().get_customer_name())
        print("Age:",super().get_age())
        print("Bonous Point:",s.__bonous_point)
        print("Account Type:",super().get_account().get_account_type())
        print("Account Balance:",super().get_account().get_balance())
        print("Account minimum:",super().get_account().get_min_balance())

a1=Account("Svings",1000,500)
pc1=PrivilegedCustomer(100,"Gopal",43,a1,100)
pc1.display()
pc1.withdraw(100)
pc1.display()

a2=Account("Current",2000,500)
c1=Customer(200,"Sipu",22,a2,)
c1.display()
c1.withdraw(230)
c1.display()