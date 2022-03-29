import scraping
import time
import data


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    # Nombre de las direcciones web necesarias
    url = 'https://www.pogdesign.co.uk/cat/1-1981'
    url_base = 'https://www.pogdesign.co.uk'
    # Se crea un diccionario para los datos
    series = dict()
    # Número de meses a analizar
    meses_analizar = 1

    i = 0
    while i < meses_analizar:
        url = scraping.read_page(url, series)
        print(series)
        if url == '-1':
            break
        else:
            url = url_base + url
            i += 1
    # Se avisa que no se analizaron todos los meses posibles
    if i < meses_analizar:
        print('Se encontraron problemas durante el proceso y se analizó {} meses'.format(i))
    scraping.serie_summary(series, url_base)
    print(series)
    data.save_dictionary(series)
