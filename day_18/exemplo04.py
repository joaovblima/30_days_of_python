import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('language', txt, re.I)
print(matches)

matches_2 = re.findall('Python', txt, re.I)
print(matches_2)

matches_3 = re.findall('Python|python', txt)
print('match_3', matches_3)

matches_4 = re.findall('[Pp]ython', txt)
print('matches_4 -> ', matches_4)
