import requests
import json


BASE_URL = 'http://127.0.0.1:8000'


##### Create User #####
def create_user(telegram_id: int, data: dict) -> dict:
    endpoint = f"{BASE_URL}/api/botusers/"
    data['telegram_id'] = telegram_id
    response = requests.post(endpoint, json=data)
    if response.status_code != 201:
        return None
    response_data = json.loads(response.text)
    return response_data


###### User Actions ######
########### Change Language ############
def change_language(telegram_id, language:str):
    response = requests.post(f"{BASE_URL}/uz/api/change-language/", data={
        'telegram_id': telegram_id,
        'language': language,
    })
    return response.status_code


#################### Change Phone Number ##################
def change_phone(telegram_id, phone:str):
    response = requests.post(f"{BASE_URL}/uz/api/phone/", data={
        'telegram_id': telegram_id,
        'phone': phone
    })
    return response.status_code


###### GET LANGUAGE of User ######
def language_info(telegram_id: int) -> str:
    endpoint: str = f"{BASE_URL}/uz/api/language-info/?telegram_id={telegram_id}"
    response = requests.get(url=endpoint, timeout=5)
    if response.status_code != 200:
        return None
    response_data = json.loads(response.text)
    return response_data['language']


###### GET CATEGORIES ######
def get_categories() -> list:
    endpoint: str = f"{BASE_URL}/api/categories/"
    response = requests.get(endpoint)
    if response.status_code != 200:
        return None
    response_data = json.loads(response.text)
    return response_data


###### ~~~~ Get All russian english and uzbek Categories ~~~~ ######
def get_all_categories() -> list:
    response = requests.get(f"{BASE_URL}/api/categories/")
    data = json.loads(response.text)
    category_uz = [i['name_uz'] for i in data]
    category_ru = [i['name_ru'] for i in data]
    category_en = [i['name_en'] for i in data]
    return category_uz + category_ru + category_en



