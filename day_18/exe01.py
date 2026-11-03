import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
word_in_paragraph = paragraph.split()
list_tuple_word_count = []
palavras_processadas = set()

for word in word_in_paragraph:
    if word not in palavras_processadas:
        palavras_processadas.add(word)
        match = re.findall(re.escape(word), paragraph, re.I)
        tupla = (len(match), match)
        list_tuple_word_count.append(tupla)

print(list_tuple_word_count)