from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':

    reference = 'https://www.pogdesign.co.uk/cat/'
    try:
        html = urlopen('https://www.pogdesign.co.uk/cat/9-2001')
    except HTTPError as e:
        print(e)
    except URLError as e:
        print('The server could not be found!')
    else:
        print('It Worked!')

    bs = BeautifulSoup(html.read(), 'html.parser')

    try:
        badContent = bs.nonExistingTag.anotherTag
    except AttributeError as e:
        print('Tag was not found')
    else:
        if badContent is None:
            print('Tag was not found')
        else:
            print(badContent)

    # nameList = bs.findAll('p', {'data-episode': ''})
    # print(soup.find("a", attrs={"class": "tweet-timestamp js-permalink js-nav js-tooltip"})["title"])

    series = dict()

    title = bs.find_all('div', {"class": 'day'})
    for name in title:
        fecha = name['id']
        rutas = name.find_all('a')
        for ruta in rutas:
            print(ruta['href'])
        texto = name.get_text().strip().split('\n')
        i = 0
        while i < len(texto):
            # Se evita el texto de cabecera que indica el día del mes y los espacios en blanco
            if i != 0 and  texto[i] != "":
                # Si la serie existe se añade el capítulo, si no se crea en el diccionario
                if texto[i] in series.keys():
                    series[texto[i]].append(texto[i+1])
                else:
                    series[texto[i]] = [texto[i + 1]]
                i += 2
            i += 1
    print(series)


