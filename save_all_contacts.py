def save_all_contacts(all_contacts):
    with open("all_contacts.csv", "w") as gap:
        for contact in all_contacts:
            line = f"{contact['first_name']}, {contact['last_name']}, {contact['mobile']}, {contact['email_address']}, {contact['home_address']}, {contact['group']}\n"
            gap.write(line)

