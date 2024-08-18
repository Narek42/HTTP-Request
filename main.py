import requests
import sys
from colorama import Fore  # Style

from colorama import init

init(autoreset=True)

# vars start

# data = {}
methodList = ['GET', 'POST', 'PUT', 'DELETE']


# vars end


# def start


def validate(method, url):
    method = method.upper()
    if method == '':
        print(Fore.YELLOW + 'Необходимо выбрать метод HTTP запроса')
        sys.exit()

    else:
        if method not in methodList:
            print(Fore.RED + 'Метод HTTP запроса не найден')
            print(Fore.BLUE + 'Список HTTP запросов: GET, POST, PUT, DELETE')
            sys.exit()

    url = url.strip()
    if url == '':
        print('Необходимо указать URL адрес')
        sys.exit()

    if method == 'GET':
        send_http_get(url)
    elif method == 'POST':
        params = input('Тело запроса (key=value;), если нужно отправить POST запрос без тело нажимайте ENTER:  ')
        send_http_post(url, params)


def send_http_get(url):
    response = requests.get(url)
    print(Fore.YELLOW + 'Код HTTP запроса: ' + str(response.status_code) + '\n')
    print(Fore.YELLOW + 'HTTP Header')
    for key, value in response.headers.items():
        print(str(key) + ' ' + value)

    print(Fore.YELLOW + 'Ответ сервера')
    print(response.text)


def send_http_post(url, params):
    data = {}
    if params:
        params = params.split(';')

        for index, item in enumerate(params):
            elm = item.strip().replace('=', ':')
            key = elm.split(':')[0]
            value = elm.split(':')[1]
            data[key] = value

        for key, value in data.items():
            if not key or not value:
                print(Fore.RED + "Возникла ошибка при сортировке тело POST запроса. \nПредполагается пустое значение "
                                 "'key' или 'value'.")
                sys.exit()

    response = requests.post(url, json=data)
    print(Fore.YELLOW + 'Код HTTP запроса: ' + str(response.status_code) + '\n')
    print(Fore.YELLOW + 'HTTP Header')
    for key, value in response.headers.items():
        print(str(key) + ' ' + value)

    print(Fore.YELLOW + 'Ответ сервера')
    print(response.text)


# def end


method_ = input("Выберите метод HTTP запроса: ")
url_ = input("Напишите URL адрес: ")
validate(method_, url_)
