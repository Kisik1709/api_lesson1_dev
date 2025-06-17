import requests


def main():

    url = ["https://wttr.in/Лондон",
           "https://wttr.in/svo", "https://wttr.in/Череповец"]
    params = {
        "m": "",
        "M": "",
        "n": "",
        "q": "",
        "T": "",
        "lang": "ru"
    }

    try:
        for link in url:
            responce = requests.get(link, params=params)
            responce.raise_for_status()
            print(responce.text)
    except requests.exceptions.RequestException as e:
        print("Ошибка при запросе:", e)


if __name__ == "__main__":
    main()
