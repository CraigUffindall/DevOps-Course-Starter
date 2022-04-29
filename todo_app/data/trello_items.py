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
    list_id = get_list_id('To Do')
    requests.post('https://api.trello.com/1/cards', params={'key':os.getenv('API_KEY'),'token':os.getenv('API_TOKEN'),'idList':list_id,'name':name})


def get_open_cards():
    r = requests.get('https://api.trello.com/1/boards/' + os.getenv('TRELLO_BOARD_ID') + '/lists', params={'key':os.getenv('API_KEY'),'token':os.getenv('API_TOKEN'),'cards':'open'})
    return r.json()


def move_to_do(id):
    list_id = get_list_id('To Do')
    requests.put('https://api.trello.com/1/cards/' + id, params={'key':os.getenv('API_KEY'),'token':os.getenv('API_TOKEN'),'idList':list_id})


def move_doing(id):
    list_id = get_list_id('Doing')
    requests.put('https://api.trello.com/1/cards/' + id, params={'key':os.getenv('API_KEY'),'token':os.getenv('API_TOKEN'),'idList':list_id})


def move_done(id):
    list_id = get_list_id('Done')
    requests.put('https://api.trello.com/1/cards/' + id, params={'key':os.getenv('API_KEY'),'token':os.getenv('API_TOKEN'),'idList':list_id})


def get_list_id(name):
    r = requests.get('https://api.trello.com/1/boards/' + os.getenv('TRELLO_BOARD_ID') + '/lists', params={'key':os.getenv('API_KEY'),'token':os.getenv('API_TOKEN')})
    json = r.json()

    for list in json:
        if list['name'] == name:
            return list['id']