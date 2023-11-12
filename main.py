#Importing other files.
from AddressBook import AddressBook, ExtPerson


#Functions in main.
#This function prints the menu.
def print_menu():
    print('L. Load the data into the address book from a disk.')
    print('S. Sort the address book by last name.')
    print('3. Search for a person by last name.')
    print('P. Print the address, phone number, and date of birth (if it exists) of a given person.')
    print('5. Print the names of the people whose birthdays are in a given month.')
    print('6. Print the names of all family members, friends, or business associates of a given person.')
    print('A. Add a new entry to the address book.')
    print('D. Delete an entry to the address book.')
    print('9. Save data in the address book.')
    print('10. Print all entries in the address book.')
    print('Q. Quit.')

#This function loads the data into the address book from a text file with the right format.
def menu_L():
    file = open("AddressBook.txt", "r")
    lines = file.readlines()
    for line in lines:
        data = line.strip().split('|')
        name = data[0].split(' ')
        date = data[1].split('/')
        address = data[2].split(', ')
        relationship = data[3]
        phone_number = data[4]
        #This creates a new entry object and adds it to the address book using the data from the text file.
        Entry = ExtPerson()        
        Entry.set_full_name(name[0], name[1])
        Entry.set_date(date[0], date[1], date[2])
        Entry.set_address(address[0], address[1], address[2], address[3])
        Entry.set_phone_number(phone_number)
        Entry.set_relationship(relationship)
        A_book.add_person(Entry)
    print('Done!')
    print()

#This function sorts the address book by last name.  
def menu_S():
    A_book.sort_list()
    print('Done!')
    print()

#This function searches for a person by last name (Redundant function requested by assignment).
def menu_P():
    menu_3()

#This function searches for a person by last name.
def menu_3():
    sans = (input('Enter the last name of the person to be searched. '))
    A_book.search_by_last_name(last_name = sans)
    print()

#This function prints the names of the people whose date of birth is in a given month.
def menu_5():
    A_book.print_name_by_month(month = input('Enter the month number: '))
    print()

#This function prints the names of the people whose relationship is in a given relationship.  
def menu_6():
    A_book.print_relationship(relationship = input('Enter the relationship: '))
    print()

#This function adds a person to the address book.
def menu_A():
    while True:
        #This creates a new entry object and adds it to the address book prompting the user for data.
        Entry = ExtPerson()        
        Entry.set_full_name(first_name = input('Enter first name: '), last_name = input('Enter last name: '))
        Entry.set_date(day = input('Enter birth day: '), month = input('Enter birth month: '), year = input('Enter birth year: '))
        Entry.set_address(street = input('Enter street: '), city = input('Enter city: '), state = input('Enter state: '), zip_code = input('Enter zip code: '))
        Entry.set_phone_number(phone_number = input('Enter phone number: '))
        Entry.set_relationship(relationship = input('Enter relationship: '))
        A_book.add_person(Entry)
        #This prompts the user if they want to add another entry, reloading the loop or breaking out of the loop.
        another = input('Do you want to add another entry? (Y/N): ')
        print()
        if another == 'Y' or another == 'y':
            continue
        else:
            #printing()
            break

#This function deletes a person from the address book.        
def menu_D():
    dans = (input('Enter the last name of the person to be deleted. '))
    A_book.delete_entry(dans)
    print('Done!')
    print()

#This function saves the data in the address book into a text file. It overwrites the old data.   
def menu_9():
    A_book.save()
    print('Done!')
    print()

#This function prints all the entries in the address book.  
def printing():
    A_book.printing()
    print()


#Main code.
#Initializing the address book object.
A_book = AddressBook()
#This while loop repeats the menu until the user chooses to quit.
while True:
    print_menu()
    menu_input = input('Enter your choice: ')
    print()
    #If statements for selection of the menu and data validation.
    if menu_input == 'L' or menu_input == 'l':
        menu_L()
    elif menu_input == 'S' or menu_input == 's':
        menu_S()
    elif menu_input == '3':
        menu_3()
    elif menu_input == 'P' or menu_input == 'p':
        menu_P()  
    elif menu_input == '5':
        menu_5()
    elif menu_input == '6':
        menu_6()
    elif menu_input == 'A' or menu_input == 'a':
        menu_A()
    elif menu_input == 'D' or menu_input == 'd':
        menu_D()
    elif menu_input == 'Q' or menu_input == 'q':
        print('Goodbye!')
        break
    elif menu_input == '9':
        menu_9()
    elif menu_input == '10':
        printing()
    else:
        print('Wrong input. Try again.')
        print()