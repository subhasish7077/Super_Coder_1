class Example:
    def _init_(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
obj=Example()
obj.num=10
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())

