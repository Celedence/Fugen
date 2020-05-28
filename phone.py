import re

def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3} \d{4}\b')
    match = phone_regex.search(input)
    print(match.group())
    raise ValueError("must be formatted")

    

# def is_valid_phone():
extract_phone("this is a new 623 623 6235")
extract_phone("this is a new 623 623 62355")