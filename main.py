import vk_requests
import threading
import messenge.py
import adresant.py
config=open("config.txt","w+")
first_strng=""

print("Привет!/nВы запустили программу VKReminder!/nПриятного пользования;)")
first_string=config.read(8)
if first_string.find("create")!=-1:
	print("Вы не первый раз пользуетесь программой.")
elif first_string.find("non-full")!=-1:
	print("Почему то не все данные были заполнены.Давайте исправим это")
	config.close()
	config=open("config.txt","a")
	
else:
	print("Вы первый раз используете программу.Давайте-ка вы сначала чуть-чуть раскажите о себе!")
	config.close()
	config=open("config.txt","w")
	
