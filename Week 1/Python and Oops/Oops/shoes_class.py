class shoe:
    def __init__(self,price,material) -> None:
        self.price=price
        self.material=material
s1=shoe(1000,'canvas')
s2=shoe(2000,'canvas')
print(id(s1)) #returns an integer value wichi is unique to this object
print(id(s2))
