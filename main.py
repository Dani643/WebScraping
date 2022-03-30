import scraping
import files


if __name__ == '__main__':
    # Número de meses a analizar. 1200 meses es más del máximo para llegar a la primera serie
    meses_analizar = 1200
    # Se configura si se quiere recuperar el resumen de cada capítulo. El número de conexiones si se omite
    # se reducirá ampliamente
    resumen_capitulo = 0
    # Nombre de las direcciones web necesarias
    url_base = 'https://www.pogdesign.co.uk'
    url = url_base + '/cat/'
    # Se crea un diccionario para los datos
    series = dict()

    # Se itera por todas las páginas del calendario por cuantos meses se quiera obtener
    i = 0
    while i < meses_analizar:
        url = scraping.read_page(url, url_base, series)
        if url == '-1':
            break
        else:
            url = url_base + url
            i += 1
    # Se avisa que no se han podido analizar todos los meses posibles ya que ha existido un problema
    if i < meses_analizar:
        print('Se encontraron problemas durante el proceso y se analizó {} meses'.format(i))
    if resumen_capitulo == 1:
        scraping.episode_summary(series, url_base)
    files.save_dictionary(series, resumen_capitulo)
