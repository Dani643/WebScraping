from bs4 import BeautifulSoup
from scraping.connection import data_retrieve


def episode_summary(series, url_base):
    """Función que para un diccionario de series, rellena los resúmenes de los capítulos

    Argumentos:
        series: diccionario con las series

    Devuelve:
        series: diccionario relleno con los resúmenes
    """
    for nombre in series.keys():
        for episodio in series[nombre]['Episodios'].keys():
            # Si está vacío se rellena con el resumen
            if series[nombre]['Episodios'][episodio][2] == '':
                # Se construye la url con el sumario del episodio
                url = url_base + '/cat/' + series[nombre]['Episodios'][episodio][1]
                html = data_retrieve(url)
                if html != '-1':
                    bs = BeautifulSoup(html.text, 'html.parser')
                    # Se guardan los datos relativos a la página previa del calendario
                    summary = bs.find('p', {"class": 'sumtext'})
                    series[nombre]['Episodios'][episodio][2] = summary.get_text()
                else:
                    series[nombre]['Episodios'][episodio][2] = 'No recuperable'


def serie_summary(url):
    """Función que recupera el resumen de una serie

    Argumentos:
        url: url donde se encuentra el resumen de la serie

    Devuelve:
        datos: lista con los datos de la serie
    """
    datos = list()
    html = data_retrieve(url)
    if html != '-1':
        bs = BeautifulSoup(html.text, 'html.parser')
        # Se guardan las características de la serie, tipo, duración, temporadas, etc...
        caracteristicas = bs.find('ul', {"class": 'furtherinfo'}).get_text().split('\n')
        for i in caracteristicas:
            if i != "":
                caracteristica = i.split(":", 1)
                datos.append(caracteristica[1].strip())
        # Se guardan el resumen de la serie
        summary = bs.find('p', {"class": 'sumtext'})
        datos.append(summary.get_text())
    else:
        for i in range(7):
            datos.append('NA')
    return datos
