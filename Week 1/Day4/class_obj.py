class customer:
    def __init__(self):
        self.id=100
c1=customer()
print(c1.id)

class table:
    def __init__(self) -> None:
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None

dining_table=table()
back_table=table()
front_table=back_table
back_table=dining_table
print(dining_table," ",back_table," ",front_table)