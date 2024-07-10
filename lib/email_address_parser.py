import re

email_addresses = "john@doe.com, person@somewhere.com team@example.com"

class EmailAddressParser:

    def __init__(self, email_addresses):
        self.email_addresses = email_addresses
    
    # return email list in alphabetical order to pass more tests!!
    def parse(self):
        print("Line 8", type(self.email_addresses))
        email_list = re.split(r"\s+|,\s*", self.email_addresses)
        print("Line 13, Email List" , email_list)
        return email_list

parser = EmailAddressParser(email_addresses)
parsed_emails = parser.parse()

print(parsed_emails)
