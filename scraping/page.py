from bs4 import BeautifulSoup
import requests


def read_page(url, series):
    """Función que para una página del calendario devuelve un diccionario con las series encontradas
    en cada uno de los días

    Argumentos:
        url: ruta con la pagina a leer
        series: diccionario con las series para rellenar

    Devuelve:
        pagina_previa: diccionario con las series completado con la web
    """
    # Se modifica la cabecera de conexión
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp, */*;q=0.8",
               "Accept-Encoding": "gzip, deflate, sdch, br", "Accept-Language": "en-US,en;q=0.8",
               "Cache-Control": "no-cache", "dnt": "1", "Pragma": "no-cache", "Upgrade-Insecure-Requests": "1",
               "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/5 37.36"
                             " (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
    try:
        html = requests.get(url, headers=headers)
    except requests.exceptions.Timeout:
        print('Maybe set up for a retry, or continue in a retry loop')
    except requests.exceptions.TooManyRedirects:
        print('Tell the user their URL was bad and try a different one')
    except requests.exceptions.ConnectionError:
        print('Web site does not exist')
    else:
        print('It Worked!')

    bs = BeautifulSoup(html.text, 'html.parser')

    previo = bs.find('div', {"class": 'prev-month'})

    # Se procesa cada uno de los días
    days = bs.find_all('div', {"class": 'day'})
    for day in days:
        fecha = day['id']
        # Se procesa cada una de las filas del día
        filas = day.find_all('div', {"class": 'info'})
        for fila in filas:
            # Se recupera el nombre de la serie y el número de capítulo
            texto = fila.get_text().strip().split('\n')
            # Se recupera la ruta con la información del capítulo
            rutas = fila.find_all('a')
            ruta = rutas[-1]['href']
            # Si la serie existe se añade el capítulo, si no se crea en el diccionario
            if texto[0] in series.keys():
                series[texto[0]][texto[1]] = ruta
            else:
                series[texto[0]] = dict()
                series[texto[0]][texto[1]] = ruta
    return previo.a['href']
