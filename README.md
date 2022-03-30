# Práctica 1: Web scraping

## Presentación

El proyecto "WebScraping" se presenta como la solución de la Práctica 1 de la asignatura Tipología y ciclo de vida de los datos. 

Este proyecto realiza webscraping sobre una web que contiene un calendario de series historico, de manera que pueda generarse un dataset que permita analizar la evolución de esta industria audiovisual, en formato de tipos de contenidos y volumenes a lo largo de los años.

Además sirve como base de datos historica de cada una de las series emitidas en televisión con el paso de los años.

## Equipo

Está practica ha sido desarrollada de manera individual por Daniel González Rodríguez.

## Estructura del código:

La estructura seguida para el proyecto es la siguiente:

```
WebScraping
├── main.py       		- Script para iniciar el proceso de web scraping
├── README.md       		- Este fichero explicativo
├── requirements.txt       	- Librerías necesarias para ejecutar el paquete
│
├── data			- Dataset generados durante el proceso
│
├── files			- Código para trabajar con los ficheros generados
│   ├── __init__.py    		- Indicación de paquete Python
│   └── save.py			- Código para guardar los datos en ficheros
│
└── scraping			- Codigo relacionado con el scraping
    ├── __init__.py    		- Indicación de paquete Python
    ├── connection.py		- Funciones de conexión a la web
    ├── page.py			- Funciones para recuperar el contenido de una página del calendario
    └── summary.py		- Funciones para recuperar los resumenes de las series
```
