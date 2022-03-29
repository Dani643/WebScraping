import csv


def save_dictionary(series):
    header = ['Serie', 'Capitulo', 'Fecha de emisión', 'Resumen']

    with open('series_db.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(header)
        for nombre in series.keys():
            for episodio in series[nombre]['Episodios'].keys():
                row = [nombre, episodio, series[nombre]['Episodios'][episodio][0],
                       series[nombre]['Episodios'][episodio][2].replace('\n', ' ')]
                writer.writerow(row)
    return 0
