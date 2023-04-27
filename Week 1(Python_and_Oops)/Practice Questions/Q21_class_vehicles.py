class vehicles:
    def __init__(self,id,type,cost) -> None:
        self.__id=id
        self.__type=type
        self.__cost=cost
        self.__premium_amount=None
    
    def diaplay(self):
        print()
        print("Id: ",self.__id)
        print("Cost: ",self.__cost)
        print("Type: ",self.__type)
        print("Premium Amount: ",self.__premium_amount)
        print()

    def calculate_premium(self):
        if(self.__type=='two_wheeler'):
            self.__premium_amount=int(self.__cost)*0.02
        elif(self.__type=="four_wheeler"):
            self.__premium_amount=int(self.__cost)*0.06
    
    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id=id

    def get_cost(self):
        return self.__cost
    def set_cost(self,cost):
        self.__cost=cost

    def get_type(self):
        return self.__type
    def set_type(self,type):
        if(type=='two_wheeler'):
            self.__type=type
        elif(type=="four_wheeler"):
            self.__type=type
        else:
            self.__type="Invalid Input"

    def get_premium(self):
        return self.__premium_amount

id,type,cost=input().split()
v1=vehicles(id,type,cost)
v1.calculate_premium()
v1.diaplay()

v1.set_id(105)
print(v1.get_id())
v1.set_type("four_wheeler")
print(v1.get_type())
v1.set_cost(30000)
print(v1.get_cost())
v1.calculate_premium()
print(v1.get_premium())

v1.diaplay()




