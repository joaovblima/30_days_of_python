from unittest.case import skip


person= {
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_married': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
 'street': 'Space street',
 'zipcode': '02210'
},
 }
"""
* Verifique se o dicionário person tem a chave skills; se sim, imprima a habilidade do meio na lista skills.
* Verifique se o dicionário person tem a chave skills; se sim, verifique se a pessoa tem a habilidade 'Python' e imprima o resultado.
* Se as habilidades da pessoa forem apenas JavaScript e React, imprima print('He is a front end developer'); 
se as habilidades da pessoa incluírem Node, Python, MongoDB, imprima print('He is a backend developer');
se as habilidades da pessoa incluírem React, Node e MongoDB, imprima print('He is a fullstack developer'); 
senão imprima print('unknown title') - para resultados mais precisos, mais condições podem ser aninhadas!
* Se a pessoa for casada e morar na Finlândia, imprima a informação no seguinte formato:
   Asabeneh Yetayeh lives in Finland. He is married.
"""

if person['skills']:
    print(person['skills'][-3])
else:
    print('no skills present')

if person['is_married'] and person['country'] == 'Finland':
    print('Asabeneh Yetayeh lives in Finland. He is married.')
else:
    print('fudido ')