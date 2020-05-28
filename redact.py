import re
text = "Last night Mrs. Daisy and Mr. White killed Ms. Chow"


pattern = re.compile(f'(Mr.|Mrs.|Ms.) [a-z]+', re.I)
print(pattern.findall(text))

