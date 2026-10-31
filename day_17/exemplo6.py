fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_vege = []
for f, v in zip(fruits, vegetables):
    fruits_vege.append({'fruta': f, 'vegetal': v})

print(fruits_vege)