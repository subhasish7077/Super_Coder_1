'''
Service
car_list
__init__(car_list)
get_car_list()
find_cars_by_year(year)
add_cars(new_car_list)
remove_cars_from_karnataka()

Method Description

1. init(car_list)
    - Initialises the instance variable, car_list
2. find_cars_by_year(year)
    - Finds and Returns the List of Models of all cars with the year as the one passed as the argument.
    
3. add_cars(new_car_list)
    - The new_car_list should be added to the instance variable car_list
    - The car_list should be still sorted such that years are in ascending order

4. remove_cars_from_karnaktaka()
    - Finds and removes all cars with the registration number, beginning with "KA" from the car_list

 Consider a Car Class as given in the code. Write a Service Class as given in the class diagram below which performs various activities on a list of cars.

Assume that the car_list is sorted by year in ascending order
'''

class Service:
    __car_list=None
    def __init__(s,car_list) -> None:
        s.__car_list=car_list
    def get_car_list(s):
        return s.__car_list
    def find_cars_by_year(s,year):
        pass
    def add_cars(s,new_car_list):
        pass
    def remove_cars_from_karnataka(s,):
        pass
