'''
Coorg Fruit Farm is a retail chain which sells fruits grown in their orchards in Coorg, 
India. They want to keep track of customers who buy fruits from them and also the 
billing process.
Write a python program to implement the class diagram given below.

RULES TO FOLLOW
=================
Class Description:
Fruit Info class:
fruit_name_list: Static list which contains the list of fruits available
fruit_price_list: Static list which contains the price/kg of fruits
    The above two lists have one-to-one correspondence, initialize it with the
    data given in the table
get_fruit_price(fruit_name): Accept a fruit name and return its price/kg. 
                             If fruit is not available, return -1

Fruit Name	    Apple	Guava	Orange	 Grape	Sweet Lime
Price per Kg	 200	  80	  70	  110	    60

Purchase class:
Initialize static variable counter to 101
calculate_price(): Calculate and return total fruit price based on rules given below
For valid fruit name (hint: invoke get_fruit_price(fruit_name)),
Calculate price based on price/kg and quantity of the fruit purchased by the customer

If price/kg of the fruit is maximum among the fruits in fruit lists and quantity 
    purchased is more than 1kg, apply 2% discount on calculated price
If price/kg of the fruit is minimum among the fruits in fruit lists and quantity 
    purchased is 5kg or more, apply 5% discount on calculated price
If the customer is a "wholesale" customer, provide an additional 10% discount. Apply 
    this discount on already discounted price, if any one of the above two points 
    are applicable. Else apply it on calculated price

Auto-generate purchase id starting from 101 prefixed by “P”. 
    Example -> P101,P102 P103 etc.
Return final fruit price 
Else, return -1.
Note:
Perform case sensitive string comparison 
There will be only one fruit with maximum price and one with minimum price

For testing:
Create objects of Customer and Purchase class
Invoke calculate_price() on Purchase object
Display the details
'''
class Fruit_Info:
    def __init__(s):
        s.__fruit_name_list=['Apple','Guava','Orange','Grape','Sweet Lime']
        s.__fruit_price_list=[200,80,70,110,60]
    def get_fruit_price(s,name):
        try:
            i=s.__fruit_name_list.index(name)
            return s.__fruit_price_list[i]
        except:
            return False
    def get_fruit_list(s):
        return s.__fruit_name_list
    def get_fruit_price_list(s):
        return s.__fruit_price_list
class customer:
    def __init__(s,name,type):
        s.__name=name
        s.__type=type
    def get_name(s):
        return s.__name
    def get_type(s):
        return s.__type
class Purchase(Fruit_Info):
    counter=101
    def __init__(s,fruit_name,quantity,customer):
        super().__init__()
        s.__name=fruit_name
        s.__quantity=quantity
        s.__price=None
        s.__customer=customer
        s.__id=None
    def purchased_id(s):
        s.__id='P'+str(Purchase.counter)
        Purchase.counter+=1
    def get_purchased_id(s):
        return s.__id
    def calculate_price(s):
        # print('s=test_price:',super().get_fruit_price(s.__name))
        if(super().get_fruit_price(s.__name)!=False):
            s.__price=super().get_fruit_price(s.__name)*s.__quantity
            max_price=max(super().get_fruit_price_list())
            min_price=min(super().get_fruit_price_list())
            if(super().get_fruit_price(s.__name)==max_price and s.__quantity>1):
                s.__price-=s.__price*0.02
            elif(super().get_fruit_price(s.__name)==min_price and s.__quantity>=5):
                s.__price-=s.__p*0.05
            if(s.__customer.get_type()=='wholesale'):
                s.__price-=s.__price*0.1
            s.purchased_id()
        else:
            s.__price=-1
    def display(s):
        print()
        print('Name:',s.__customer.get_name())
        print('Fruit:',s.__name)
        print('Quantity',s.__quantity)
        print('Purchased Id:',s.get_purchased_id())
        print('Price:',s.__price)
        print()

c=customer('Sipu','wholesale')
p=Purchase('Apple',2,c)
p.calculate_price()
p.display()

c=customer('Lipu','retailer')
p=Purchase('Apple',2,c)
p.calculate_price()
p.display()

        

