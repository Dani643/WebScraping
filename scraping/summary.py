import time
from bs4 import BeautifulSoup
from scraping.connection import data_retrieve


def serie_summary(series, url_base):
    """Función que para un diccionario de series, rellena los resúmenes de los capítulos

    Argumentos:
        series: diccionario con las series

    Devuelve:
        series: diccionario relleno con los resúmenes
    """
    for nombre in series.keys():
        for episodio in series[nombre].keys():
            # Si está vacío o no se pudo recuperar anteriormente se rellena con el resumen
            if series[nombre][episodio][2] == '' or series[nombre][episodio][2] == 'No recuperable':
                # Se construye la url con el sumario del episodio
                url = url_base + '/cat/' + series[nombre][episodio][1]
                html = data_retrieve(url)
                if html != '-1':
                    bs = BeautifulSoup(html.text, 'html.parser')
                    # Se guardan los datos relativos a la página previa del calendario
                    summary = bs.find('p', {"class": 'sumtext'})
                    series[nombre][episodio][2] = summary.get_text()
                else:
                    series[nombre][episodio][2] = 'No recuperable'
