import re

email_addresses = "john@doe.com, person@somewhere.com team@example.com"

class EmailAddressParser:

    def __init__(self, email_addresses):
        self.email_addresses = email_addresses
    
    def parse(self):
        print("Line 8", type(self.email_addresses))
        email_list = sorted(re.findall(r"[a-zA-Z0-9]+@+[a-zA-Z0-9]+[.][a-zA-Z0-9]+|[a-zA-Z0-9]+[.-][a-zA-Z0-9]+@+[a-zA-Z0-9]+[.][a-zA-Z0-9]+", self.email_addresses))
    # line 14 passes all but last test, that includes entries that are not email addresses.  Above solution just finds only email addresses in string and pulls them out instead of using split()
        # email_list = sorted(re.split(r"\s+|,\s*", self.email_addresses))
        print("Line 13, Email List" , email_list)
        return email_list

parser = EmailAddressParser(email_addresses)
parsed_emails = parser.parse()

print(parsed_emails)
