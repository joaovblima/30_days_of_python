import re 

regex_pattern = r'[Aa]pple | [Bb]anana'
txt = """ Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. """
matches = re.findall(regex_pattern, txt)
print(matches)

"""
regex_pattern_2 = r'\d'  # d é um caractere especial que significa dígitos
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches_2= re.findall(regex_pattern_2, txt)
print(matches_2)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], isso não é o que queremos
"""

regex_pattern = r'[a].'  # o colchete significa a e o . significa qualquer caractere, exceto nova linha
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . qualquer caractere, + qualquer caractere uma ou mais vezes
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

regex_pattern = r'[a].*'  # . qualquer caractere, * qualquer caractere zero ou mais vezes
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? significa aqui que o '-' é opcional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']