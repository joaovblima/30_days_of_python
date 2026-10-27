def capitalize_list_items(list):
    new_list=[]
    for i in list:
        new_list.append(i.capitalize())
    return new_list

print(capitalize_list_items(['brasil', 'francisco', 'prefeito kil']))