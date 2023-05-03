from pydantic import BaseModel, ValidationError, Field, validator
from setting import valid_email, valid_password
import json
import requests
import pytest



class VlojennuyObjekt(BaseModel):
    checkin: str
    checkout: str


class TeloGet(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: VlojennuyObjekt

class TeloPost(BaseModel):
    token: str
    pass

class TeloPostData(BaseModel):
    username = str
    password = str
"""Класы PETS"""
class GetMyPets(BaseModel):
    age: int
    animal_type: str
    created_at: float
    id: str
    name: str
    pet_photo: str


class Pets(BaseModel):
    pets: list[GetMyPets]

"""Mетод POST на получение токена"""
def post_zapross_na_tocen(username="", password=""):
    URL = 'https://restful-booker.herokuapp.com/auth'
    data = {
    "username" : username,
    "password" : password}
    res = requests.post(URL, data=data)
    result = res.json()
    status = res.status_code
    result_text = res.text
    return result, status, result_text

# a = post_zapross_na_tocen('admin','password123')
# print(a)


"""Метод GET возвращает результаты json, text, status_code"""
def get_zapross_brony_booking():
    URL = 'https://restful-booker.herokuapp.com/booking/'
    res = requests.get(URL+"1")
    result = res.json()
    result_text = res.text
    status = res.status_code

    return result, result_text, status

# d = get_zapross_brony_booking()
# print(d[1])


"""Метод выдает auth_key"""

def get_api_key():
    base_url = "https://petfriends.skillfactory.ru/"

    headers = {
                'email': valid_email,
                'password': valid_password,
            }
    res = requests.get(base_url + 'api/key', headers=headers)
    result = res.json()
    status = res.status_code
    auth_key = result['key']

    return auth_key

"""Мои питомцы GET запрос выводит всех питомцев, статус, последний id"""
def moi_pets():
    base_url = "https://petfriends.skillfactory.ru/"
    auth_key = get_api_key()
    headers = {'auth_key': auth_key}

    filter = {'filter': 'my_pets'}# Фильтр на своих питомцев my pets
    res = requests.get(base_url + 'api/pets', headers=headers, params=filter)
    result = res.json()
    status = res.status_code
    pet_id = result['pets'][0]['id']
    result_text = res.text
    return result, status, pet_id, result_text