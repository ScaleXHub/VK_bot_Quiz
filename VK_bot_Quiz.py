import datetime
import time
import socket
import urllib3
import requests
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import commands
import os

TOKEN = str(os.environ.get('token'))

session = vk_api.VkApi(token=TOKEN)
vk = session.get_api()
longpoll = VkBotLongPoll(session, 149178033)

# Загрузка фото в сообщение:

# upload = vk_api.VkUpload(vk)
# photo = upload.photo_messages(путь)
# owner_id = photo[0]['owner_id']
# photo_id = photo[0]['id']
# access_key = photo[0]['access_key']
# attachment = f'photo{owner_id}_{photo_id}_{access_key}'

print('Initialization completed')

while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                response = str(event.message.text)
                user_id = str(event.message.from_id)
                user = vk.users.get(user_ids=user_id)
                user_name = user[0]['first_name'] + ' ' + user[0]['last_name']
                message_time = str(datetime.datetime.utcfromtimestamp(event.message.date) +
                                   datetime.timedelta(hours=3))
                
                print('–' * 120)
                print(f'Время получения сообщения: {message_time}\n' +
                      f'Текст сообщения: {response}\n' +
                      f'Отправитель: {user_name}\n' +
                      f'id отправителя: {user_id}\n')
                
                commands.ChooseCommand(vk, response, user_id, user_name)
        
        time.sleep(1)
    
    except(socket.timeout, urllib3.exceptions.ReadTimeoutError,
           requests.exceptions.ReadTimeout):
        print('–' * 120)
        print("Произошла ошибка.\nВремя:" + str(datetime.datetime.utcnow()))
