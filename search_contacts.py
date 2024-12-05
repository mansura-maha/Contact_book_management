try:
   def search_contact(all_contacts):
    contact = all_contacts
    results = []
    for contact in all_contacts:
        if results in contact["first_name"] or all_contacts in contact["mobile_number"]:
            results.append(contact)
            print("Search Results: ")
            for contact in all_contacts:
                    print(f"First Name: {contact['first_name']} , Last Name: {contact['last_name']} , Mobile: {contact['mobile']} , E-mail Address: {contact['email_address']} , Home Address: {contact['home_address']} , Group: {contact['group']}")
except Exception as f:
      print(f"Error type is: {f}")