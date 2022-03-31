from bs4 import BeautifulSoup
from scraping.connection import data_retrieve
from scraping.summary import serie_summary


def read_page(url, url_base, series):
    """Función que para una página del calendario devuelve un diccionario con las series encontradas
    en cada uno de los días

    Argumentos:
        url: ruta con la página a leer
        series: diccionario con las series para rellenar

    Devuelve:
        pagina_previa: página del mes anterior del calendario
    """
    # Se lee la url
    html = data_retrieve(url)
    if html != '-1':
        bs = BeautifulSoup(html.text, 'html.parser')

        # Se guardan los datos relativos a la página previa del calendario
        previo = bs.find('div', {"class": 'prev-month'})

        # Se procesa cada uno de los días
        days = bs.find_all('div', {"class": 'day'})
        for day in days:
            # Se guarda el día del calendario que se analiza
            fecha = day['id'][2:].replace("_", "-")
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
                    series[texto[0]]['Episodios'][texto[1]] = [fecha, ruta, ""]
                else:
                    series[texto[0]] = dict()
                    # Si no se conocía la serie se recuperan sus datos
                    series[texto[0]]['Datos'] = serie_summary(url_base + '/cat/' + rutas[0]['href'])
                    series[texto[0]]['Episodios'] = dict()
                    series[texto[0]]['Episodios'][texto[1]] = [fecha, ruta, ""]
        return previo.a['href']
    else:
        return '-1'
