from class_and_metod import *
import pytest


"""ТЕСТ на МЕТОД GET... Проверяем ответ что он не пустой + статус код"""

def test_get_api_otvet_ok():
    result, result_text, status = get_zapross_brony_booking()
    assert len(result) != 0
    print(f'Длина ответа {len(result)} != 0')
    assert len(result_text) != 0
    print(f'Длина ответа {len(result_text)} != 0')
    assert status == 200
    print(f'status_code == {status}')



"""ТЕСТ на МЕТОД GET...  Cравнение ответа json и pydantic на валидное содержимое"""

def test_get_api_pydantic():
    result, result_text, status = get_zapross_brony_booking()
    pyd = TeloGet.parse_raw(result_text)
    """Если в результатах получим ошибку, значит в значениях json, есть не соответствие типов данных.
     С помощью pydantyc у нас уже типы данных определены"""
    assert result['firstname'] == pyd.firstname
    assert pyd.lastname == result['lastname']
    assert pyd.depositpaid == result['depositpaid']
    assert pyd.bookingdates.checkout == result['bookingdates']['checkout']
    assert pyd.bookingdates.checkin == result['bookingdates']['checkin']
    assert pyd.totalprice == result['totalprice']


"""ТЕСТ на метод POST получение токкена зарегистрированного пользователя"""

def test_post_zapros_na_token():
    result, status, result_text = post_zapross_na_tocen('admin', 'password123')
    assert len(result) != 0
    print(f'длина resalt {len(result)} != 0')
    assert status == 200
    print(f'Status_code {status} == 200')
    assert result_text != 0
    print(f'длина result_text {result_text} != 0')



"""ТЕСТ на метод POST получение токкена  НЕзарегистрированного пользователя с
использованием фикстур pytest на различные значения из техник тест дизайна. Общее колличество 42 теста"""

@pytest.mark.parametrize('username',[""," ","a","abr_a","a/akj.","a a a","a@#$%T"], ids=[""," ","a","abr_a","a/akj.","a a a","a@#$%T"])
@pytest.mark.parametrize('password', ["0", " 0 a", "mOtRi", "5432_7df", "", " "], ids=["0", " 0 a", "mOtRi", "5432_7df", "", " "])
def test_post_zapros_na_token_ficstur(username, password):
    """согласно документации сервер будет отдавать ответ со статусом 200 и
    возвращать тело, мы проверяем на соответсвие тело {"token":"e4058a0ee306978"}"""
    result, status, result_text = post_zapross_na_tocen(username, password)
    assert len(result) != 0
    print(f'длина resalt {len(result)} != 0')
    assert status == 200
    print(f'Status_code {status} == 200')
    assert result['reason'] == 'Bad credentials'
    print(f'result {result["reason"]} == "Bad credentials"')

"""ТЕСТ на метод POST получение токкена  зарегистрированного пользователя.
    Используем PYDANTIC для проверки ответа"""

def test_post_na_token_pydantic():
    result, status, result_text = post_zapross_na_tocen('admin', 'password123')
    pyd = TeloPost.parse_raw(result_text)
    """Если результаты равны то значение в token == str"""
    assert pyd.token == result['token']
    print(f'результат pydantic token {pyd.token} == str')



"""ТЕСТ на метод POST получение токкена  зарегистрированного пользователя.
    Используем PYDANTIC для проверки тела запроса (data) перед отправкой и проверяем ответ на тип."""

def test_post_na_token_data_pydantic():
    username = 'admin'
    password = 'password123'
    pyddata = TeloPostData.username
    pyddata2 = TeloPostData.password
    assert pyddata2 == str
    print(f'username == {pyddata}')
    assert pyddata == str
    print(f'password == {pyddata2}')
    result, status, result_text = post_zapross_na_tocen(username, password)
    pyd = TeloPost.parse_raw(result_text)
    """Если результаты равны то значение в token == str"""
    assert pyd.token == result['token']
    print(f'результат pydantic token {pyd.token} == str')



"""ТЕСТЫ на Meтод GET Мои питомцы. Проверяем документацию Json ответ от сервера на соответствие типов
    с помощью PYDANTIK and json(тест изначально валился пришлось переработать его для наглядности,
    скорей всего тут кроется БАГ)"""

def test_get_k_api_my_pets_pydantic():
    result, status, pet_id, result_text = moi_pets()
    pyd = Pets.parse_raw(result_text)
    age_text = pyd.pets[0].age
    age_json = result['pets'][0]['age']
    assert type(age_text) == int
    print(f'согласно pydantic тип age_text == {type(age_text)}')
    assert type(age_json) == str
    print(f'согласно json тип age_text == {type(age_json)}')
    assert age_text != age_json
    print(f'ответ pydantic {age_text} int != ответ json {age_json} str тип даных не соответстует документации')


def test_get_api_pet_id_pydantic():
    result, status, pet_id, result_text = moi_pets()
    pyd = Pets.parse_raw(result_text)
    assert pet_id == pyd.pets[0].id
    print(f'json ответ {pet_id} == {pyd.pets[0].id} pydantic type')
    assert type(pet_id) == type(pyd.pets[0].id)
    print(f'json ответ type {type(pet_id)} == {type(pyd.pets[0].id)} pydantic type')
    assert status == 200
    print(f'{status} == 200')


def test_get_name_pydantic():
    result, status, pet_id, result_text = moi_pets()
    pyd = Pets.parse_raw(result_text)
    assert type(result['pets'][0]['name']) == str
    print(f'согласно json тип name == {type(result["pets"][0]["name"])}')
    assert type(pyd.pets[0].name) == str
    print(f'согласно pydantic тип name == {type(pyd.pets[0].name)}')
    assert result['pets'][0]['name'] == pyd.pets[0].name
    print(f'результат json {result["pets"][0]["name"]} == {pyd.pets[0].name}  результат pydantic')


def test_get_animal_type_pydantic():
    result, status, pet_id, result_text = moi_pets()
    pyd = Pets.parse_raw(result_text)
    assert type(result['pets'][0]['animal_type']) == str
    print(f'согласно json тип animal_type == {type(result["pets"][0]["animal_type"])}')
    assert type(pyd.pets[0].animal_type) == str
    print(f'согласно pydantic тип name == {type(pyd.pets[0].animal_type)}')
    assert result['pets'][0]['animal_type'] == pyd.pets[0].animal_type
    print(f'результат json {result["pets"][0]["animal_type"]} == {pyd.pets[0].animal_type}  результат pydantic')