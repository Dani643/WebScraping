import scraping
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':

    # Se crea un diccionario para los datos
    series = dict()
    url = 'https://www.pogdesign.co.uk/cat/1-2001'
    reference = 'https://www.pogdesign.co.uk'
    url2 = scraping.read_page(url, series)
    print(series)
    time.sleep(1)
    url3 = scraping.read_page(reference + url2, series)
    print(url3)
    print(series)
