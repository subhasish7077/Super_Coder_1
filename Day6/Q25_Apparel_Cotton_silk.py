# An apparel shop wants to manage the items which it sells.25 min
# Write a python program to implement the class diagram given below.

# RULES TO FOLLOW
# ===============
# Class Description:

# Apparel class:
# Initialize static variable counter to 100
# In the constructor, auto-generate item_id starting from 101 prefixed by "C" for cotton apparels 
# and "S" for silk apparels. Example – C101, S102, S103, C104 etc.
# calculate_price(): Add 5% service tax on the price of the apparel and update attribute, price with the new value


# Cotton class:
# While invoking parent constructor from child constructor, pass "Cotton" as item_type
# calculate_price(): Update attribute, price of Apparel class based on rules given below
# Add service tax on price by invoking appropriate method of Apparel class
# Apply discount on price
# Add 5% VAT on final price

# Silk class:
# While invoking parent constructor from child constructor, pass "Silk" as item_type
# calculate_price(): Update attribute, price of Apparel class based on rules given below
# Add service tax on price by invoking appropriate method of Apparel class
# Identify points earned based on rules given below:
# Silk apparels with price more than Rs. 10000, earn 10 points and anything less than or equal to that earn 3 points
# Initialize attribute, points with the identified points
# Add 10% VAT on price

# Note: Perform case sensitive string comparison 

# For testing:
# Create objects of Cotton class and Silk class
# Invoke calculate_price() on Cotton objects and Silk objects
# Display their details

class Apparel:
    counter = 100
    def __init__(s,item,price) -> None:
        Apparel.counter+=1
        s.__item_id=item[0].upper()+str(Apparel.counter)
        s.__item=item
        s.__price=price
    def calculate_price(s):
        s.__price+=s.__price*0.05
    def get_price(s):
        return s.__price
    def get_item_id(s):
        return s.__item_id
    def get_item(s):
        return s.__item
    def set_price(s,price):
        s.__price=price
    def  display(s):
        print()
        print("Item: ",s.__item)
        print("Item id: ",s.__item_id)
        print("Price: ",s.__price)

class Cotton(Apparel):
    def __init__(s, price,discount) -> None:
        super().__init__("Cotton", price)
        s.__discount=discount
    def calculate_price(s):
        super().calculate_price()
        price=super().get_price()
        price-=price*(s.__discount/100)
        price+=price*0.05
        super().set_price(price)
    def get_discount(s):
        return s.__discount
    def set_discount(s,discount):
        s.__discount=discount
    def display(s):
        super().display()

class Silk(Apparel):
    def __init__(s, price) -> None:
        super().__init__("Silk", price)
        s.__point=0
    def calculate_price(s):
        super().calculate_price()
        if(super().get_price()>10000):
            s.__point+=10
        else:
            s.__point+=3
        price=super().get_price()
        price+=price*0.1
        super().set_price(price)
    def get_points(s):
        return s.__point
    def set_point(s,point):
        s.__point=point
    def display(s):
        super().display()
        print("Silk points: ",s.__point)



c1=Cotton(1000,5)
c1.calculate_price()
c1.display()

s1=Silk(20000)
s1.calculate_price()
s1.display()