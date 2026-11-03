import re

txt = 'i love to teach python and javascript'
match = re.match('i love to teach', txt, re.I)
print(match)
span = match.span()
print(span)
start, end = span
print(start, end)
substring = txt[start:end]
print(substring)