import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match = re.search("first", txt, re.I)
print(match)
span = match.span()
start, end = span
print(start, end)
substring = txt[start:end]
print(substring)