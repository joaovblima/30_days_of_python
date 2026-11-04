import json
pessoa = {
    "nome": 'joao lima',
    'idade' : 29, 
    'time do caracao' : 'são paulo', 
    'santo preferido': 'santo agostinho'
}

with open('./json_ex.json','w', encoding='utf-8') as f:
    json.dump(pessoa, f, ensure_ascii=False, indent=4)