import scraping
import data


if __name__ == '__main__':
    # Nombre de las direcciones web necesarias
    url = 'https://www.pogdesign.co.uk/cat/'
    url_base = 'https://www.pogdesign.co.uk'
    # Se crea un diccionario para los datos
    series = dict()
    # Número de meses a analizar
    meses_analizar = 1
    # Se configura si se quiere recuperar el resumen de cada capítulo
    resumen_capitulo = 0

    i = 0
    while i < meses_analizar:
        url = scraping.read_page(url, url_base, series)
        if url == '-1':
            break
        else:
            url = url_base + url
            i += 1
    # Se avisa que no se analizaron todos los meses posibles
    if i < meses_analizar:
        print('Se encontraron problemas durante el proceso y se analizó {} meses'.format(i))
    if resumen_capitulo == 1:
        scraping.episode_summary(series, url_base)
    print(series)
    data.save_dictionary(series, resumen_capitulo)
