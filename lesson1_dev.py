import requests

WEATHER_URL = "https://wttr.in/{}"
PARAMS = {
    "m": "",
    "M": "",
    "n": "",
    "q": "",
    "T": "",
    "lang": "ru"
}


def fetch_weather(city):
    url = WEATHER_URL.format(city)
    responce = requests.get(url, params=PARAMS)
    responce.raise_for_status()
    return responce.text


def main():
    locations = ["Лондон", "svo", "Череповец"]
    try:
        for city in locations:
            print(fetch_weather(city))
    except requests.exceptions.RequestException as e:
        print("Ошибка при запросе:", e)


if __name__ == "__main__":
    main()
