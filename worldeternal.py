import requests
import time
from threading import Thread 
import threading 
mail = input("перетяните файл с почтами: ")
try:
    mail = mail.split("\"")[1].split("\"")[0]
except:
    pass
#читаем файл в список ауф
with open(mail, 'r', encoding="UTF-8") as file:
    mails = [row.strip() for row in file]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0",
    "Accept": "*/*","Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest"
}
lock = threading.Lock()
#функция типа запросы делает понял да
def print_from_list(): 
    while mails: 
        lock.acquire()
        #ну типа читаем строчку и удаляем из массива
        mail = mails.pop()
        #а тут мы извлекаем саму почту example@.mail.ru и т.д
        acc = mail.split(":")[0]
        lock.release() 
        data = "b_117b2d245865f1381be6fc47e_6f7e087302=&EMAIL="+acc
        req = requests.post("https://warheroesonline.us6.list-manage.com/subscribe/post?u=117b2d245865f1381be6fc47e&id=6f7e087302", headers=headers,data=data)
        if req.status_code == 200:
            print("succesfully registered: "+acc)
        else:
            print("error:"+acc)
#запускаем 10 потоков
for _ in range(10): 
    Thread(target=print_from_list).start()