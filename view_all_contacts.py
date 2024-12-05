#f"{contact['first_name']}, {contact['middle_name']}, {contact['last_name']}, {contact['mobile']}, {contact['email_address']}, {contact['home_address']}, {contact['group']}

def view_all_contacts(all_contacts):
        if all_contacts != []:
                for contact in all_contacts:
                    print(f"First Name: {contact['first_name']} , Last Name: {contact['last_name']} , Mobile: {contact['mobile']} , E-mail Address: {contact['email_address']} , Home Address: {contact['home_address']} , Group: {contact['group']}")
        else:
           print("No Contact Found In The System")