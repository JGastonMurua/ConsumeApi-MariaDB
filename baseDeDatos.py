import pymysql  # Importa libreria para conectar y ejecutar comandos en una base de datos MySQL/MariaDB.
from typing import List, Dict # Especifica tipos de datos en las funciones (List y Dict).

def crearBaseDeDatos(config: Dict[str, str]): # Toma un diccionario de configuración como argumento.
    try:
        # Conectar a MariaDB sin especificar una base de datos
        conexion = pymysql.connect(
            user=config['user'], 
            password=config.get('password', ''), 
            host=config['host'], 
            port=config['port']
        )
        cursor = conexion.cursor()
        # Crear la base de datos si no existe
        cursor.execute("CREATE DATABASE IF NOT EXISTS criptomonedas")
        conexion.close()
        print("Base de datos 'criptomonedas' verificada/creada.")
    except pymysql.MySQLError as e:
        print("Error al conectar o al ejecutar la consulta:", e)

def registrarDatos(datos: List[Dict[str, str]], config: Dict[str, str]) -> None:
    try:
        # Conectar a la base de datos especificada
        conexion = pymysql.connect(**config)
        print("Conexión establecida")

        with conexion.cursor() as cursor:
            # Crear la tabla si no existe
            sql_create_table = """
            CREATE TABLE IF NOT EXISTS criptomonedas (
                id INT AUTO_INCREMENT PRIMARY KEY, 
                nombre VARCHAR(50), 
                simbolo VARCHAR(10), 
                precio DECIMAL(15, 8), 
                mercado VARCHAR(50),
                market_cap DECIMAL(20, 2),
                total_volume DECIMAL(20, 2),
                high_24h DECIMAL(15, 8),
                low_24h DECIMAL(15, 8)
            )
            """
            cursor.execute(sql_create_table)

            # Insertar datos en la tabla
            sql_insert_data = """
            INSERT INTO criptomonedas (nombre, simbolo, precio, mercado, market_cap, total_volume, high_24h, low_24h) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            for registro in datos:
                val = (
                    registro.get('nombre'), 
                    registro.get('simbolo'), 
                    registro.get('precio'), 
                    registro.get('mercado'),
                    registro.get('market_cap'),
                    registro.get('total_volume'),
                    registro.get('high_24h'),
                    registro.get('low_24h')
                )
                cursor.execute(sql_insert_data, val)

            # Confirmar la transacción
            conexion.commit()

    except pymysql.MySQLError as e:
        print("Error al conectar o al ejecutar la consulta:", e)
    finally:
        if 'conexion' in locals():
            conexion.close()
