#Import Node and LinkedList from other files.
from Node import Node
from LinkedList import LinkedList


#Create a Person class with first_name and last_name.
class Person:
    
    def __init__(self, firts_name, last_name):
        self.first_name = firts_name
        self.last_name = last_name

    def set_full_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
 
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def get_last_name(self):
        return self.last_name


#Create a Date class with day, month, and year.
class Date:
    
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def set_date(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_date(self):
        return str(self.day) + '/' + str(self.month) + '/' + str(self.year)

    def get_month(self):
        return self.month

    #This function checks for leap years. (Not in used.)
    def leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


#Create an Address class with street, city, state, and zip_code.
class Address:
    
    def __init__(self, street = str, city = str, state = str, zip_code = int):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def set_address(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def get_address(self):
        return self.street + ', ' + self.city + ', ' + self.state + ', ' + self.zip_code


#Create an ExtPerson child class with relationship and phone_number, and inherits all the traits from the parent classes Person, Date, and Address.
class ExtPerson(Person, Date, Address):
    
    def __init__(self, firts_name = str, last_name  = str, day = str, month = str, year = str, street  = str, city  = str, state  = str, zip_code = str, relationship = str, phone_number = str):
        Person.__init__(self, firts_name, last_name)
        Date.__init__(self, day, month, year)
        Address.__init__(self, street, city, state, zip_code)
        self.relationship = relationship
        self.phone_number = phone_number

    def set_relationship(self, relationship):
        self.relationship = relationship

    def get_relationship(self):
        return self.relationship

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_phone_number(self):
        return self.phone_number


#Create an AddressBook class to call functions from the LinkedList object.
class AddressBook():
    
    #Functions here are to call the functions from the LinkedList object.
    def sort_list(self):
        A_list.insertion_sort_singly_linked()

    def search_by_last_name(self, last_name):
        A_list.search_by_last_name(last_name)

    def print_name_by_month(self, month):
        A_list.print_name_by_month(month)
        
    def print_relationship(self, relationship):
        A_list.print_relationship(relationship) 

    def add_person(self, person):
        node = Node(person)
        A_list.append(node)

    def delete_entry(self, last_name):
        A_list.delete_entry(last_name)  

    def save(self):
        A_list.save()

    def printing(self):
       A_list.print_all_entries()


#Create an object of the LinkedList class.     
A_list = LinkedList()