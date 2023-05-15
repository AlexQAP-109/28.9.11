from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import pytest



def test_petfriends():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get("https://petfriends.skillfactory.ru/")

    """кликаем на кнопку"""
    btn_newuser = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/button')
    btn_newuser.click()

    """Кликаем на ссылку у меня уже есть ак"""
    btn_exist_acc = browser.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    """обращаемся к полю маил чистим его и всавляем маил"""
    field_email = browser.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("kotik@kotik.ru")

    """обращаемся к полю pass чистим его и всавляем pass"""
    """Используем WebDriverWait для явного ожидания"""
    field_pass = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "pass")))
    field_pass.clear()
    field_pass.send_keys("12345")

    """Обращаемся к кнопке и кликаем ее"""
    btn_submit = browser.find_element(By.XPATH, "/html/body/div[1]/div/form/div[3]/button")
    btn_submit.click()

    """Обращаемчя к полю мои питомцы и кликаем его"""
    my_pets = browser.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a')
    my_pets.click()

    """Обращаемся к карточкам  пользователя и проверяем что там находится 8 питомцев"""

    vse_tr = browser.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    dlina = len(vse_tr)
    print(f'количество my_pets c тегоm tr  =  {dlina}')
    assert dlina == 8


    vse_img_th = browser.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/th/img')
    print(f'количество тегов th  соответствует  == {len(vse_img_th)}')
    assert len(vse_img_th) == 8

    """Обращаемчя к полю мои питомцы и кликаем его"""
    my_pets = browser.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a')
    my_pets.click()

    """Используем явное ожидание просто для примера"""
    time.sleep(5)

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    """Открываем скачанный фаил с html и закрываем браузер """

    browser.quit()
    with open('index_selenium_html', encoding='utf8') as file:
        img_ = file.read()
    soup = BeautifulSoup(img_, 'lxml')
    a = soup.find_all('tr')
    img_s_photo = []
    img_bez_poto = []

    for i in a:
        if len(str(i.img)) > 58:
            b = i.img
            img_s_photo.append(b)
        else:
            img_bez_poto.append(i.img)

    polovina = len(a)//2
    if polovina > len(img_s_photo):
        print(f'к сожaлению из {len(a)} img всего {len(img_s_photo)} c фото ')
    else:
        print(f'из всех  {len(a)} img у {len(img_s_photo)} есть фото')

    td_pars = soup.find_all('td')
    name_poroda_age = []
    musor = []
    for i in td_pars:
        if i.text.split() == ['×']:
            musor.append(i.text.split())
        else:
            name_poroda_age.append(i.text.split())

    if len(name_poroda_age)// len(musor) == 3:
        print(f'длина списка со значениями имя, порода, возраст {len(name_poroda_age)} и количество разделителей '
              f'между карточками {len(musor)} каждому питомцу соответсвует 3 параметра')


    """Выбираем на  проверку имена питомцев из карточек"""
    name_my_pets = []
    poroda_age =[]
    for i in name_poroda_age:
        if i == name_poroda_age[0]:
            name_my_pets.append(i)
        elif i == name_poroda_age[3]:
            name_my_pets.append(i)
        elif i ==  name_poroda_age[6]:
            name_my_pets.append(i)
        elif i == name_poroda_age[9]:
            name_my_pets.append(i)
        elif i == name_poroda_age[12]:
            name_my_pets.append(i)
        elif i == name_poroda_age[15]:
            name_my_pets.append(i)
        elif i == name_poroda_age[18]:
            name_my_pets.append(i)
        elif i == name_poroda_age[21]:
            name_my_pets.append(i)
        else:
            poroda_age.append(i)

    """Проверем имена на уникальность"""

    povtor_name = []
    for i in name_my_pets[1:8]:
        if i == name_my_pets[0]:
            povtor_name.append(name_my_pets[0])

    for i in name_my_pets[2:8]:
        if i == name_my_pets[1]:
            povtor_name.append(name_my_pets[1])

    for i in name_my_pets[3:8]:
        if i == name_my_pets[2]:
            povtor_name.append(name_my_pets[2])

    for i in name_my_pets[4:8]:
        if i == name_my_pets[3]:
            povtor_name.append(name_my_pets[3])

    for i in name_my_pets[5:8]:
        if i == name_my_pets[4]:
            povtor_name.append(name_my_pets[4])

    for i in name_my_pets[6:8]:
        if i == name_my_pets[5]:
            povtor_name.append(name_my_pets[5])

    for i in name_my_pets[7:8]:
        if i == name_my_pets[6]:
            povtor_name.append(name_my_pets[6])

    print(f'К сожалению имена питомцев не все уникальные .'
          f'Список повторяющихся имен {povtor_name}')