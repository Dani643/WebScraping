import csv


def save_dictionary(series, resumen_capitulo):
    """Función que escribe en un fichero las series obtenidas en función de si se ha recuperado el detalle
    del resumen de cada capítulo o no

    Argumentos:
        series: diccionario con las series
        resumen_capitulo: indica si se recuperó el resumen de cada capítulo

    Devuelve:
        None: se crea el fichero de db
    """
    header = ['Serie', 'Canal de emisión', 'Tipo de serie', 'Día de emisión', 'País', 'Duración', 'Estado',
              'Resumen de la serie', 'Número del capitulo', 'Fecha de emisión']
    if resumen_capitulo:
        with open('capitulos_db.csv', 'w', newline='') as f:
            header.append('Resumen del capitulo')
            writer = csv.writer(f, delimiter=';')
            writer.writerow(header)
            for nombre in series.keys():
                for episodio in series[nombre]['Episodios'].keys():
                    row = [nombre, series[nombre]['Datos'][0], series[nombre]['Datos'][1],
                           series[nombre]['Datos'][2], series[nombre]['Datos'][3], series[nombre]['Datos'][4],
                           series[nombre]['Datos'][5], series[nombre]['Datos'][6], episodio,
                           series[nombre]['Episodios'][episodio][0],
                           series[nombre]['Episodios'][episodio][2].replace('\n', ' ')]
                    writer.writerow(row)
    with open('series_db.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(header)
        for nombre in series.keys():
            for episodio in series[nombre]['Episodios'].keys():
                row = [nombre, series[nombre]['Datos'][0], series[nombre]['Datos'][1],
                       series[nombre]['Datos'][2], series[nombre]['Datos'][3], series[nombre]['Datos'][4],
                       series[nombre]['Datos'][5], series[nombre]['Datos'][6], episodio,
                       series[nombre]['Episodios'][episodio][0]]
                writer.writerow(row)
    return 0
