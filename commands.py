import random
from pic import pictures
from strings import errors, commands
from translit import Translit

started_quiz = {}


def RandId():
    return random.randint(-9223372036854775808, 9223372036854775807)


def MainCommands(vk, response, user_id, user_name):
    # привет
    if response.lower().startswith('привет'):
        vk.messages.send(user_id=user_id, message=f'Привет, {user_name}.', random_id=RandId())
        vk.messages.send(user_id=user_id, message=commands, random_id=RandId())
    
    # /помощь
    elif response.lower().startswith('/помощь') or response.lower().startswith('/команды'):
        vk.messages.send(user_id=user_id, message=commands, random_id=RandId())
    
    # /транслит
    elif response.lower().startswith('/транслит'):
        if len(response.split(' ', 1)) > 1:
            arg = response.split(' ', 1)[1]
            vk.messages.send(user_id=user_id, message=Translit(arg), random_id=RandId())
        else:
            vk.messages.send(user_id=user_id, message=errors['/транслит'], random_id=RandId())
            return
    
    # /капс
    elif response.lower().startswith('/капс'):
        if len(response.split(' ', 1)) > 1:
            arg = response.split(' ', 1)[1]
            if arg.isupper():
                vk.messages.send(user_id=user_id, message=errors['/капс уже капс'], random_id=RandId())
            else:
                vk.messages.send(user_id=user_id, message=arg.upper(), random_id=RandId())
        else:
            vk.messages.send(user_id=user_id, message=errors['/капс неверно'], random_id=RandId())
            return
    
    # /пикча
    elif response.lower() == '/пикча':
        attachment = pictures[random.randint(0, 228)]
        vk.messages.send(user_id=user_id, attachment=attachment, random_id=RandId())
    
    # /пикчи
    elif response.lower().startswith('/пикчи'):
        if len(response.split(' ', 1)) > 1 and response.split(' ', 1)[1].isdigit():
            count = int(response.split(' ', 1)[1])
        else:
            vk.messages.send(user_id=user_id, message=errors['/пикчи'], random_id=RandId())
            return
        
        if count > 10:
            count = 10
        
        attachment = ''
        
        for i in range(0, count):
            attachment += pictures[random.randint(0, 228)] + ','
        
        attachment = attachment.strip(',')
        vk.messages.send(user_id=user_id, attachment=attachment, random_id=RandId())


def ChooseCommand(vk, response, user_id, user_name):
    MainCommands(vk, response, user_id, user_name)
    # if user_id in started_quiz:
    #    QuizCommands(vk, user_id)
