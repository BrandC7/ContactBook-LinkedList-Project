#Linked List class to create indefinite entries to the address book.
class LinkedList:
  
  def __init__(self):
    self.head = None
    self.tail = None

  #Add a new node to the list.
  def append(self, new_node):
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node

  def prepend(self, new_node):
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
      
  def insert_after(self, current_node, new_node):
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    elif current_node is self.tail:
      self.tail.next = new_node
      self.tail = new_node
    else:
      new_node.next = current_node.next
      current_node.next = new_node

  def remove_after(self, current_node):
    #Special case, remove head
    if (current_node == None) and (self.head != None):
      succeeding_node = self.head.next
      self.head = succeeding_node
      if succeeding_node == None: #Removed last item
        self.tail = None
    elif current_node.next != None:
      succeeding_node = current_node.next.next
      current_node.next = succeeding_node
      if succeeding_node == None: #Removed tail
        self.tail = current_node
  
  #Insertion sort function to sort the linkedlist by last name.
  def insertion_sort_singly_linked(self):
    before_current = self.head
    current_node = self.head.next
    while current_node != None:
      next_node = current_node.next
      position = self.find_insertion_position(current_node.data.get_last_name())
      if position == before_current:
        before_current = current_node
      else:
        self.remove_after(before_current)
        if position == None:
          self.prepend(current_node)
        else:
          self.insert_after(position, current_node)
      current_node = next_node

  def find_insertion_position(self, data_value):
    position_a = None
    position_b = self.head
    while (position_b != None) and (data_value > position_b.data.get_last_name()):
      position_a = position_b
      position_b = position_b.next
    return position_a

  #Search by last name in the linkedlist function.
  def search_by_last_name(self, last_name):
    current = self.head
    counter = 1 #Counter for the person number (same case for other functions).
    while current:
      if current.data.get_last_name() == last_name:
        print('Person #' + str(counter))
        print('Name: ', current.data.get_full_name())
        print('Date of Birth: ', current.data.get_date())
        print('Address: ', current.data.get_address())
        print('Relationship: ', current.data.get_relationship())
        print('Phone Number: ', current.data.get_phone_number())
        print()
      counter += 1
      current = current.next

  #Search by month of birth in the linkedlist addressbook function.
  def print_name_by_month(self, month):
    current = self.head
    counter = 1 
    while current != None:
      if current.data.get_month() == month:
        print('Person #' + str(counter))
        print(current.data.get_full_name())
        print()
      counter += 1
      current = current.next

  #Search by relationship in the linkedlist addressbook function.
  def print_relationship(self, relationship):
    current = self.head
    counter = 1 
    while current:
      if current.data.get_relationship() == relationship:
        print('Person #' + str(counter))
        print(current.data.get_full_name())
        print()
      counter += 1
      current = current.next
  
  #Delete entry from the linkedlist addressbookfunction.
  def delete_entry(self, last_name):
    current = self.head
    if current and current.data.get_last_name() == last_name:
      self.head = current.next
      return
    prev = None
    while current and current.data.get_last_name() != last_name:
      prev = current
      current = current.next
    if current is None:
      print(f"Entry with last name {last_name} not found.")
      print()
      return
    prev.next = current.next

  #Save all entries in the linkedlist to a textfile function (it overwrites the old file).
  def save(self):
    file = open("AddressBook.txt", "w")
    current = self.head
    while current:
        file.write(current.data.get_full_name() + "|")
        file.write(current.data.get_date() + "|")
        file.write(current.data.get_address() + "|")
        file.write(current.data.get_relationship() + "|")
        file.write(current.data.get_phone_number()+ "|")
        file.write("\n")
        current = current.next
    file.close()
    
  #Print all entries in the linkedlist.
  def print_all_entries(self):
    current = self.head
    counter = 1 
    while current:
      print('Person #' + str(counter))
      print('Name: ', current.data.get_full_name())
      print('Date of Birth: ', current.data.get_date())
      print('Address: ', current.data.get_address())
      print('Relationship: ', current.data.get_relationship())
      print('Phone Number: ', current.data.get_phone_number())
      print()
      counter += 1
      current = current.next