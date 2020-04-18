translit_dict = {
    'а':'a', 'б':'b', 'в':'v', 'г':'g', 'д':'d', 'е':'e', 'ё':'yo',
    'ж':'zh','з':'z', 'и':'i', 'й':'y', 'к':'k', 'л':'l', 'м':'m',
    'н':'n', 'о':'o','п':'p', 'р':'r', 'с':'s', 'т':'t', 'у':'u',
    'ф':'f', 'х':'kh', 'ц':'ts', 'ч':'ch', 'ш':'sh', 'щ':'sch','ъ':'',
    'ъе':'ye', 'ы':'y', 'ый':'iy', 'ь':'', 'э':'e', 'ю':'yu', 'я':'ya'
    }

def Translit(text):
    text = text.replace('/транслит', '')
    result = ''

    if not len(text):
        return 'После команды /транслит напишите сообщение.'

    while len(text) > 1:
        # ый -> iy
        if text[0:2] in translit_dict:                             
            result += translit_dict[text[0:2]]
            text = text[2:len(text)]

        # ыЙ -> iY
        elif text[0] + text[1].lower() in translit_dict:            
            result += translit_dict[text[0:2].lower()][0]
            result += translit_dict[text[0:2].lower()][1].upper()
            text = text[2:len(text)]

        # Ый -> Iy
        elif text[0].lower() + text[1] in translit_dict:            
            result += translit_dict[text[0:2].lower()].title()
            text = text[2:len(text)]

        # ый -> IY
        elif text[0:2].lower() in translit_dict:                    
            result += translit_dict[text[0:2].lower()].upper()
            text = text[2:len(text)]

        # б -> b
        elif text[0] in translit_dict:                                
            result += translit_dict[text[0]]
            text = text[1:len(text)]

        # Я -> YA или Я -> Ya
        elif text[0].lower() in translit_dict:
            # Я -> YA
            if (len(result) > 0 and
                    (text[1].isupper() or result[len(result)-1].isupper())):               
                result += translit_dict[text[0].lower()].upper()
                text = text[1:len(text)]

            # Я -> Ya
            else:                                            
                result += translit_dict[text[0].lower()].title()
                text = text[1:len(text)]

        # 1 -> 1
        else:                                                
            result += text[0]
            text = text[1:len(text)]

    if len(text):
        # б -> b
        if text[0] in translit_dict:
            result += translit_dict[text[0]]

        # Я -> YA
        elif text.lower()[0] in translit_dict:
            result += translit_dict[text[0].lower()].upper()

        # 1 -> 1
        else:
            result += text[0]

    return result