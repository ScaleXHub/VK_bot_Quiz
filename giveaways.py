from bs4 import BeautifulSoup
import requests
import json

link = 'https://new.isthereanydeal.com/giveaways/?data=&offset=0&type=lazy'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.33'
}


def CheckTitle(title):
    for substring in ('free on steam', 'free on gog', 'free on epic games', '(gog), (steam), (epic games)'):
        if title.find(substring) != -1:
            return True


def UpdateGiveaways():
    response = requests.get(link, headers=headers)
    html = json.loads(response.text)['html']
    soup = BeautifulSoup(html, 'lxml')
    giveaways_list = []
    giveaways = soup.findAll(class_='sgi')
    
    for giveaway in giveaways:
        giveaway_data = {}
        giveaway_data['title'] = giveaway.find(class_='sgi__title').text
        
        if CheckTitle(giveaway_data['title'].lower()):
            giveaway_data['link'] = giveaway.find(class_='sgi__btn').get('href')
            giveaway_data['add_date'] = giveaway.findAll(class_='sl-expiry')[-1].text
            giveaway_games_count = giveaway.find(class_='sl-tag__num').text
            giveaway_data['games'] = []
            
            if int(giveaway_games_count) > 1:
                giveaway_link = giveaway.find(class_='sgi__cnt').get('href')
                response = requests.get('https://new.isthereanydeal.com' + giveaway_link, headers=headers).text
                soup = BeautifulSoup(response, 'lxml')
                games = []
                
                for game in soup.findAll(class_='pt__primary'):
                    games.append(game.text)
                
                giveaway_data['games'] = games
            
            giveaways_list.append(giveaway_data)
    
    return giveaways_list


if __name__ == '__main__':
    print(*UpdateGiveaways(), sep='\n')
