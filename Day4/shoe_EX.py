class shoe:
    def __init__(self,price,material) -> None:
        self.price=price
        self.material=material
    def __str__(self):
        return "shoe with price: "+str(self.price)+"\nand material: "+self.material
    def __int__(self):
        return self.price * 2

s1=shoe(1000,'canvas')
print(s1)
print(int(s1))
