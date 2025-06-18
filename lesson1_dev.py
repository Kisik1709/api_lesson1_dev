import requests

URL_WEATHER = "https://wttr.in/{}"
PARAMS = {
    "m": "",
    "M": "",
    "n": "",
    "q": "",
    "T": "",
    "lang": "ru"
}


def show_weather(city):
    url = URL_WEATHER.format(city)
    responce = requests.get(url, params=PARAMS)
    responce.raise_for_status()
    return responce.text


def main():
    locations = ["Лондон", "svo", "Череповец"]
    try:
        for city in locations:
            print(show_weather(city))
    except requests.exceptions.RequestException as e:
        print("Ошибка при запросе:", e)


if __name__ == "__main__":
    main()
