import requests

URL = 'http://google.ru'
BUTTON = 'Поиск в Google'


def open_browser(browser_name):
    name = [item.capitalize() for item in open_browser.__name__.split('_')]
    print(f"{' '.join(name)} -> {browser_name.upper()}")


def go_to_company_name_homepage(page_url):
    open_browser("chrome")
    response = requests.get(page_url)
    print(f"Статус ответа:{response.status_code} \nЗапрашиваемый адрес: {page_url}")
    return response


def find_registration_button_on_login_page(page_url, button_text):
    response = go_to_company_name_homepage(page_url)
    data = response.text
    count = data.count(button_text)
    print(f"Кнопка \"{button_text}\" -  найдена {count} раз")


if __name__ == "__main__":
    find_registration_button_on_login_page(URL, BUTTON)
