try:
   def remove_contact(all_contacts):
        if all_contacts != []:
           mobile_number = int(input("Enter A Number You Want To Remove: "))
           for contact in (all_contacts):
                    if contact['mobile'] == mobile_number:
                          all_contacts.remove(contact)
                          print(" The Contact Has Been Removed")
        else:
            print("This Number Does Not Exist In The System")
except Exception as f:
      print(f"Error type is: {f}")      
