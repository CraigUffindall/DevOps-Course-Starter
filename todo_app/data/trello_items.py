import requests
import os


def get_items():
    json = get_open_cards()
    items = []

    for list in json:
        list_name = list['name']
        for card in list['cards']:
            items.append({ 'id':card['id'], 'status':list_name, 'name':card['name'] })

    return items


def add_item(name):
    json = get_open_cards()

    for list in json:
        if list['name'] == 'To Do':
            list_id = list['id']
            requests.post('https://api.trello.com/1/cards', params={'key':os.getenv('API_KEY'),'token':os.getenv('API_TOKEN'),'idList':list_id,'name':name})


def get_open_cards():
    r = requests.get('https://api.trello.com/1/boards/' + os.getenv('TRELLO_BOARD_ID') + '/lists', params={'key':os.getenv('API_KEY'),'token':os.getenv('API_TOKEN'),'cards':'open'})
    return r.json()