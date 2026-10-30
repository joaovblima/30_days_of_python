from datetime import datetime

data = datetime.now()
print(data)

date_format = data.strftime("%m/%d/%Y, %H:%M:%S")
print(date_format)


#date_string = "5 December, 2019"
#print("date_string =", date_string)     # date_string = 5 December, 2019
#date_object = datetime.strptime(date_string, "%d %B, %Y")
#print("date_object =", date_object) 

hoje = "5 December, 2019"
print("date string = ", hoje)
data_obj = datetime.strptime(hoje, "%d %B, %Y")
print("date obj" , data_obj)