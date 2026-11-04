def count_lines_and_words(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f'arquivo não encontrado {path}')
        return None
    
    n_words = 0
    for line in lines:
        n_words += len(line.split())
    

    return len(lines), n_words
    
"""
files = [
    'obama_speech.txt',
    'michelle_obama_speech.txt',
    'donald_speech.txt',
    'melina_trump_speech.txt',
]
"""

file = './donald_speech.txt'
n_lines, n_words = count_lines_and_words(file)
print(f'linhas {n_lines}, palavavras {n_words}')
"""
for name in files:
    result = count_lines_and_words(f'data/{name}')
    if result is None:
        continue

    n_lines, n_words = result
    print(f'{name}: {n_lines}, linhas, {n_words} palavras')
"""