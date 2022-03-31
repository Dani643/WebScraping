import csv
import os
import zipfile as zf


def save_dictionary(series, resumen_capitulo):
    """Función que escribe en un fichero las series obtenidas en función de si se ha recuperado el detalle
    del resumen de cada capítulo o no

    Argumentos:
        series: diccionario con las series
        resumen_capitulo: indica si se recuperó el resumen de cada capítulo

    Devuelve:
        None: se crea el fichero de db
    """
    path = 'data_processed'
    fichero_series = 'series_db.csv'
    fichero_capitulos = 'capitulos_db.csv'
    header = ['Serie', 'Canal de emisión', 'Tipo de serie', 'Día de emisión', 'País', 'Duración', 'Estado',
              'Resumen de la serie', 'Número del capitulo', 'Fecha de emisión']
    # Se crea el fichero con los resumenes de capitulos si se han procesado
    if resumen_capitulo:
        with open(os.path.join(path, fichero_capitulos), 'w', newline='') as f:
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
    # Se crea el fichero con los datos de las series
    with open(os.path.join(path, fichero_series), 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(header)
        for nombre in series.keys():
            for episodio in series[nombre]['Episodios'].keys():
                row = [nombre, series[nombre]['Datos'][0], series[nombre]['Datos'][1],
                       series[nombre]['Datos'][2], series[nombre]['Datos'][3], series[nombre]['Datos'][4],
                       series[nombre]['Datos'][5], series[nombre]['Datos'][6], episodio,
                       series[nombre]['Episodios'][episodio][0]]
                writer.writerow(row)
    # Se obtiene el tamaño del fichero
    tamanyo = os.path.getsize(os.path.join(path, fichero_series))
    # Si es mayor que 10MB se comprime para que pueda subirse en GitHub
    if tamanyo / (1024*1024) > 10:
        zip_file = os.path.join(path, fichero_series) + '.zip'
        # Se crea el zip
        with zf.ZipFile(zip_file, 'w', compression=zf.ZIP_DEFLATED) as zip_f:
            # Añadimos el fichero p_big al zip
            zip_f.write(os.path.join(path, fichero_series), fichero_series)
        # Se borra el fichero original
        os.remove(os.path.join(path, fichero_series))
