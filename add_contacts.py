from save_all_contacts import save_all_contacts

def add_contacts(all_contacts):
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    mobile = input("Enter Mobile Number: ")
    email_address = input("Enter E-mail Address: ")
    home_address = input("Enter Home Address: ")
    group = input("Add To A Group : ")

    contact = {
        "first_name": first_name,
        "last_name": last_name,
        "mobile": mobile,
        "email_address": email_address,
        "home_address": home_address,
        "group": group,
    }
    all_contacts.append(contact)
    save_all_contacts(all_contacts)

    print("Contact Added Successfully")

    return all_contacts


    
    
