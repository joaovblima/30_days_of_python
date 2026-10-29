Exercícios: Dia 14
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Exercícios: Nível 1

Explique a diferença entre map, filter e reduce.
map -> é uma função que aplica outra função em uma lista ou um número que você passsa
filter -> filtra e retorna um valor booleano em cima de um valor ou lista que você passa
reduce -> reduz dois numeros ou vários parametros a um só numero, pode ser uma soma, subtração ou multiplicação, a ideia é passar o parametro e reduzir a um. 

Explique a diferença entre função de ordem superior, closure e decorador. 
funcao de ordem superior -> é uma função que faz o uso de outras funções. 
closures -> permite uma função aninhada executar em uma função externa
decorador -> é um padrão de projeto 

Defina uma função de chamada antes de map, filter ou reduce, veja os exemplos.

Use for para imprimir cada país na lista countries.

Use for para imprimir cada nome na lista names.

Use for para imprimir cada número na lista numbers.

Exercícios: Nível 2

Use map para criar uma nova lista transformando cada país em maiúsculas na lista countries

Use map para criar uma nova lista transformando cada número em seu quadrado na lista numbers

Use map para transformar cada nome em maiúsculas na lista names

Use filter para filtrar países que contenham 'land'.

Use filter para filtrar países que tenham exatamente seis caracteres.

Use filter para filtrar países que contenham seis letras ou mais na lista de países.

Use filter para filtrar países que comecem com 'E'

Encadeie dois ou mais iteradores de lista (ex.: arr.map(callback).filter(callback).reduce(callback))

Declare uma função chamada get_string_lists que recebe uma lista como parâmetro e retorna uma lista contendo apenas os itens do tipo string.

Use reduce para somar todos os números na lista numbers.

Use reduce para concatenar todos os países e produzir esta frase: Estonia, Finland, Sweden, Denmark, 
Norway, and Iceland are north European countries

Declare uma função chamada categorize_countries que retorna uma lista de países com algum padrão em comum (você pode encontrar a lista de países neste repositório como countries.js (ex: 'land', 'ia', 'island', 'stan')).

Crie uma função que retorne um dicionário, onde as chaves representam as letras iniciais dos países e os valores são o número de nomes de países que começam com aquela letra.

Declare uma função get_first_ten_countries - ela retorna uma lista dos primeiros dez países da lista countries.js na pasta data.

Declare uma função get_last_ten_countries que retorna os últimos dez países na lista countries.

Exercícios: Nível 3
Use o arquivo countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) e siga as tarefas abaixo:
Ordene os países por nome, por capital, por população
Filtre as dez línguas mais faladas por localização.
Filtre os dez países mais populosos.
🎉 PARABÉNS ! 🎉