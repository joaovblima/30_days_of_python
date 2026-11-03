import re

txt = 'i love to teach python and javascript'
match = re.match("i like to teach", txt, re.I)
print(match)