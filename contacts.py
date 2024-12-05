import add_contacts, view_all_contacts, remove_contacts, search_contacts

all_contacts = []
while True:
    print("Welcome to Contact Book Management System")
    print("0. Exit")
    print("1. Add Contacts")
    print("2. View All Contacts")
    print("3. Remove Contacts")
    print("4. Search Contact: ")

    menu = input("Select an option: ")

    if menu == "0":
        print("Thanks For Using Contact Management System ") 
        break 
    elif menu == "1":
        all_contacts = add_contacts.add_contacts(all_contacts)
    elif menu == "2":
        all_contacts = view_all_contacts.view_all_contacts(all_contacts)
    elif menu == "3":
        all_contacts = remove_contacts.remove_contact(all_contacts)
    elif menu == "4":
         all_contacts = search_contacts.search_contact(all_contacts)
        
    else:
        print("Invalid Choice. Please Enter A Valid Number")
