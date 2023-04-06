"""The central library at Mysore has a set of very interesting
 books and journals. The books are arranged in the 
alphabetical order of their author names. 
So it is very easy for the readers to search for the book.
The library has got a set of new books. The librarian wants
 to arrange them in order too. As some books are already 
arranged in the order, find a suitable way of arranging the 
new set of books amidst them.

Write a python program to arrange all the books in the 
alphabetical order of the author names.
sort_item_list_by_author(): Accepts the new list of books 
and returns it sorted in the alphabetical order of their 
author names.
add_new_items(): Accepts the new list of books, sorts it and
 merges it with the existing books in the library.
Hint - Use sort_item_list_by_author() method for sorting the 
books.
sort_items_by_published_year(): Sorts the list of books (item_list) based on the increasing order of their published years. If there are multiple items that
are published in the same year, then sort them based on the alphabetical order of their author names.
Note: While sorting the author names in alphabetical order, ignore the special characters including space, if there are any.

Library
- item_list
init(item_list)
+ get_item_list()
+ sort_item_list_by_author(new_item_list)
+ add_new_items(new_item_list)
+ sort_items_by_published_year()


Item
- item_name
- author_name
- published_year
init(item_name,author_name,published_year)
+ get_item_name()
+ get_author_name()
+ get_published_year()
str()"""

class item:
    def __init__(self,item_name,author_name,published_year):
        self.__item_name=item_name
        self.__author_name=author_name
        self.__published_year=published_year
    
    def get_item_name(self):
        return self.__item_name
    
    def get_author_name(self):
        return self.__author_name
    
    def get_published_year(self):
        return self.__published_year
    def __str__(self):
        return f"{self.__item_name} by {self.__author_name} published in {self.__published_year}"

class library:
    def __init__(self,item_list):
        self.__item_list=item_list
    
    def get_item_list(self):
        return self.__item_list
    
    def sort_item_list_by_author(self,new_item_list):
        def theAuthorName(item):
            return item.get_author_name()
        new_item_list=sorted(new_item_list,key=theAuthorName) #lambda x:x.get_author_name()
        return new_item_list
    
    def add_new_item(self,new_item_list):
        self.__item_list=self.__item_list+new_item_list
        self.__item_list=self.sort_item_list_by_author(self.__item_list)
    
    def sort_items_by_published_year(self):
        def sortKey(item):
            return (item.get_published_year(),item.get_author_name())
        self.__item_list=sorted(self.__item_list,key=sortKey)

    

book1=item("book1","aaa",2001)
book2=item("book2","bbb",2002)
book3=item("book3","ddd",2003)
book4=item("book4","ccc",2003)
book5=item("book5","eee",2005)
itemList1=[book5,book3,book4]
itemlist2=[book2,book1]

lib1=library(itemList1)
print("viewing items in list")
temp=lib1.get_item_list()
for i in temp:
    print(i)
#print('\n'.join(map(str, lib.get_item_list())))
print("===========================")

lib1.add_new_item(itemlist2)
print("viewing items after adding new item list")
temp=lib1.get_item_list()
for i in temp:
    print(i)

print("=======================")


#y=lib1.sort_item_list_by_author(itemList1)
#for i in y:
#    print(i)

print("=================================")
lib1.sort_items_by_published_year()

temp=lib1.get_item_list()
for i in temp:
    print(i)


"""
book1=item("The War of the Worlds","H.G. Wells",1898)
book2=item("The Alchemist","Paulo Coelho",1988)
book3=item("Harry Potter and the Philosopher's Stone","J.K. Rowling",1997)
book4=item("The Hunger Games","Suzanne Collins",2008)
book5=item("The Da Vinci Code","Dan Brown",2003)
"""
