'''
The central library at Mysore has a set of very interesting books and journals.
The books are arranged in the alphabetical order of their author names. So it is 
very easy for the readers to search for the book.
The library has got a set of new books. The librarian wants to arrange them in order too.
As some books are already arranged in the order, find a suitable way of arranging the 
new set of books in middle of them them.

Write a python program to arrange all the books in the alphabetical order 
of the author names.

sort_item_list_by_author(): 
    Accepts the new list of books and returns it sorted in the alphabetical 
    order of their author names.
add_new_items(): Accepts the new list of books, sorts it and merges it with the 
existing books in the library.
Hint - Use sort_item_list_by_author() method for sorting the books.
sort_items_by_published_year(): Sorts the list of books (item_list) based on the increasing order of their published years. 
If there are multiple items that are published in the same year, then sort them based on the alphabetical order of their author names.
Note: While sorting the author names in alphabetical order, ignore the special characters including space, if there are any.

Library
- item_list
_init_(item_list)
+ get_item_list()
+ sort_item_list_by_author(new_item_list)
+ add_new_items(new_item_list)
+ sort_items_by_published_year()


Item
- item_name
- author_name
- published_year
_init_(item_name,author_name,published_year)
+ get_item_name()
+ get_author_name()
+ get_published_year()
_str_()

'''
class Library:
    def __init__(s,item_list):
        s.item_list=item_list
    def get_item_list(s):
        return s.item_list
    def sort_item_list_by_author(s,new_item_list):
        new_item_list.sort(key=lambda x: x.get_author_name())
        return new_item_list
    def add_new_items(s,new_item_list):
        new_item_list=s.sort_item_list_by_author(new_item_list)
        s.item_list=s.item_list+new_item_list
        s.item_list.sort(key=lambda x: x.get_author_name())   
    def sort_items_by_published_year(s):
        s.item_list=s.sort_item_list_by_author(s.item_list)
        s.item_list.sort(key=lambda x: x.get_published_year())
    def display(s):
        for i in s.item_list:
            print(i)

class Item:
    __item_name=None
    __author_name=None
    __published_year=None
    def __init__(s,item_name,author_name,published_year):
        s.__item_name=item_name
        s.__author_name=author_name
        s.__published_year=published_year
        # s.next=None
    def get_item_name(s):
        return s.__item_name
    def get_author_name(s):
        return s.__author_name
    def get_published_year(s):
        return s.__published_year
    def __str__(s):
        return (str(s.__item_name)+"-->"+str(s.__author_name)+'-->'+str(s.__published_year))
    
item1=Item("A Better India: A Better World","Narayana Murthy",1998)
item2=Item("A Passage to India","E.M. Foster",1890)
item3=Item("A Revenue Stamp","Amrita Pritam",2000)
item4=Item("Death of a City","Amrita Pritam",1985)
item5=Item("Pinjar","Amrita Pritam",2001)


item_list=[item1,item2,item3,item4,item5]
library=Library(item_list)


item6=Item("chemistry","Puri sharma",2010 )
item7=Item("physics","S.L.Arora",1880 )
item8=Item("math","R.D Sharma",2000 )

item_list=[item6,item7,item8]
print("sorted items by author name:")
for i in library.sort_item_list_by_author(item_list):
    print(i)  
print("----------------------------------------------------------------")
print("after adding item6,7,8")
library.add_new_items(item_list)
library.display()
library.sort_items_by_published_year()
print("sorted items by published Year:")
print("---------------------------------------------------------------------\n")
library.display()
