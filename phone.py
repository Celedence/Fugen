import re

def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3} \d{4}\b')
    match = phone_regex.search(input)
    if match :
        return match.group()
    raise ValueError("must be formatted")

def extract_all_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3} \d{4}\b')
    return phone_regex.findall(input)
    
    
def is_valid_phone(input):
    phone_regex = re.compile(r'^\b\d{3} \d{3} \d{4}$')
    match = phone_regex.search(input)
    if match:
        return True
    return False


print(is_valid_phone("423 623 6235"))



# print(extract_phone("this is a new 623 623 6235"))
print(extract_all_phone("this is a new 623 623 6235 or 815 234 2345"))