# Consumir una api y registrar datos en base de datos SQL

Este proyecto tiene como objetivo consumir datos de una API de criptomonedas (CoinGecko) y registrar esos datos en una base de datos MariaDB utilizando scripts en Python.

## Descripción

El proyecto se compone de dos archivos principales:
1. `main.py`: Este script consume la API de CoinGecko para obtener datos sobre criptomonedas y llama a funciones para registrar estos datos en la base de datos.
2. `baseDeDatos.py`: Este script contiene las funciones necesarias para crear la base de datos y la tabla (si no existen) y para insertar los datos en la base de datos.

## Detalles

- **API utilizada**: CoinGecko.
- **Base de datos**: MariaDB.
- **Librería de Python**: PyMySQL para interactuar con la base de datos || Requests para hacer solicitudes http. 

## Requisitos

- Python 3.x
- MariaDB o MySQL
- Librería PyMySQL

## Instalación de Requisitos

**Instalar Python**: Puedes descargar e instalar Python desde [python.org](https://www.python.org/).

**Instalar MariaDB**: Puedes descargar e instalar MariaDB desde [mariadb.org](https://mariadb.org/download/).

**Instalar PyMySQL**: Ejecuta el siguiente comando para instalar la librería PyMySQL, abre la  consola y escribe: `pip install pymysql`

## Ejecutar el Proyecto:

- Abre una terminal o línea de comandos.
- Navega hasta el directorio donde están tus scripts. (Al utilizar MariaDB necesitamos que la carpeta que contenga los scripts este situada dentro de la carpeta de `XAMPP` y dentro de la carpeta `htdocs`).
- Ejecuta el script main.py.
- Verifica los Datos en MariaDB usando phpMyAdmin:

      - Abre el navegador web y ve a http://localhost/phpmyadmin
      - Inicia sesión.
      - Selecciona la base de datos criptomonedas.
      - Verifica los datos en la tabla criptomonedas.
## Autor

[@Gaston Murua](https://github.com/JGastonMurua)

Este es un proyecto creado para la cursada de la materia Programación sobre redes del profesor [Javier Blanco](https://github.com/jjcblanco)