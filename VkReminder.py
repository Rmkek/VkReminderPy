import vk_requests
import threading

api = vk_requests.create_api(app_id='Your app id', login='Your vk login', password='Your vk password', scope='Scope (you can determine whether you need this or not at https://vk.com/dev/methods)')
api.messages.send(user_id="User that will receive message", message="Напоминание активировано. PyVKReminder 1.0")

def send_message():
  threading.Timer(3600.0, send_message).start() #Every hour it sends message below.
  api.messages.send(user_id="User that will receive message", message="PyVkReminder 1.0 by Roman Malyshkov.")
  
send_message()