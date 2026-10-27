Exercícios: Nível 1
Obtenha a entrada do usuário usando input("Enter your age: "). Se o usuário tiver 18 anos ou mais, dê o retorno: You are old enough to drive. Se for menor de 18, dê o retorno de quanto tempo falta. Saída:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.

Compare os valores de my_age e your_age usando if … else. Quem é mais velho (eu ou você)? Use input("Enter your age: ") para obter a idade como entrada. Você pode usar uma condição aninhada para imprimir 'year' para uma diferença de 1 ano, 'years' para diferenças maiores, e um texto personalizado se my_age = your_age. Saída:

Enter your age: 30
You are 5 years older than me.

Obtenha dois números do usuário usando o prompt input. Se a for maior que b retorne a is greater than b, se a for menor que b retorne a is smaller than b, senão a is equal to b. Saída:

Enter number one: 4
Enter number two: 3
4 is greater than 3

Exercícios: Nível 2
Escreva um código que dê a nota aos estudantes de acordo com suas notas:
```sh
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
```
Obtenha o mês da entrada do usuário e depois verifique se a estação é Outono, Inverno, Primavera ou Verão. 
Se a entrada do usuário for: Setembro, Outubro ou Novembro, a estação é Outono.
Dezembro, Janeiro ou Fevereiro, a estação é Inverno.
Março, Abril ou Maio, a estação é Primavera Junho, Julho ou Agosto, a estação é Verão

A seguinte lista contém algumas frutas:
```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
```

Se uma fruta não existir na lista, adicione a fruta à lista e imprima a lista modificada. Se a fruta existir, imprima print('That fruit already exist in the list')

Exercícios: Nível 3
Aqui temos um dicionário person. Sinta-se livre para modificá-lo!
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
 * Verifique se o dicionário person tem a chave skills; se sim, imprima a habilidade do meio na lista skills.
 * Verifique se o dicionário person tem a chave skills; se sim, verifique se a pessoa tem a habilidade 'Python' e imprima o resultado.
 * Se as habilidades da pessoa forem apenas JavaScript e React, imprima print('He is a front end developer'); se as habilidades da pessoa incluírem Node, Python, MongoDB, imprima print('He is a backend developer'); se as habilidades da pessoa incluírem React, Node e MongoDB, imprima print('He is a fullstack developer'); senão imprima print('unknown title') - para resultados mais precisos, mais condições podem ser aninhadas!
 * Se a pessoa for casada e morar na Finlândia, imprima a informação no seguinte formato:
    Asabeneh Yetayeh lives in Finland. He is married.