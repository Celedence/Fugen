import re

titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna (2010)",
    "Further Tales of the City (1982)",
    "Baby Cakes (1984)",
    "More Tales of the City (1980)",
    "Michael Tolliver Lives (2007)",
    "Sure of You (1989)"
]

titles.sort()
fixed_titles = []

pattern = re.compile(r'(^[\w ]+) \((\d{4})\)')
for book in titles:
    result = pattern.sub("\g<2> - \g<1>", book)
    fixed_titles.append(result)
fixed_titles.sort()
print(fixed_titles)