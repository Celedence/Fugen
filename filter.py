import re

def censor(input):
    pattern = re.compile(r'\bfrack\w*\b', re.I)
    return pattern.sub("CENSOR", input)