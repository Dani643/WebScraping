import requests


def data_retrieve(url):
    # Se modifica la cabecera de conexión
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp, */*;q=0.8",
               "Accept-Encoding": "gzip, deflate, sdch, br", "Accept-Language": "en-US,en;q=0.8",
               "Cache-Control": "no-cache", "dnt": "1", "Pragma": "no-cache", "Upgrade-Insecure-Requests": "1",
               "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/5 37.36"
                             " (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
    try:
        html = requests.get(url, headers=headers)
    except requests.exceptions.Timeout:
        return '-1'
    except requests.exceptions.HTTPError:
        return '-1'
    except requests.exceptions.TooManyRedirects:
        return '-1'
    except requests.exceptions.ConnectionError:
        return '-1'
    else:
        if html.status_code == 200:
            return html
