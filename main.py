import requests # Importa libreria para hacer solicitudes HTTP.
import baseDeDatos  

# Configuración de la base de datos 
config = {
    'user': 'root',  # Tu usuario de MariaDB || Este usuario no tiene contraseña
    'host': 'localhost',  # El host donde se está ejecutando MariaDB, generalmente 'localhost'
    'port': 3308,  # El puerto en el que MariaDB está escuchando, por defecto es 3306
    'database': 'criptomonedas',  # La base de datos que vamos a crear/verificar
}

# Crear/verificar la base de datos
baseDeDatos.crearBaseDeDatos(config)

# URL de la API de CoinGecko
url = 'https://api.coingecko.com/api/v3/coins/markets'

# Parámetros de la solicitud a la API
params = {
    'vs_currency': 'usd',  # Moneda en la que deseas obtener los precios de las criptomonedas
    'order': 'market_cap_desc',  # Ordenar las criptomonedas de mayor a menor capitalización de mercado
    'per_page': 20,  # Solicita 20 criptomonedas 
    'page': 1,  # Página de resultados que deseas obtener (1 para la primera página)
    'sparkline': 'false'  # No incluir datos de sparkline en los resultados
}

response = requests.get(url, params=params)

if response.status_code == 200: 
    # Si la respuesta es exitosa, obtener los datos en formato JSON
    data = response.json()

    # Preparar los datos para la base de datos
    datos_procesados = []
    for criptomoneda in data:
        datos_procesados.append({
            'nombre': criptomoneda['name'],
            'simbolo': criptomoneda['symbol'],
            'precio': criptomoneda['current_price'],
            'mercado': 'CoinGecko',
            'market_cap': criptomoneda['market_cap'],
            'total_volume': criptomoneda['total_volume'],
            'high_24h': criptomoneda['high_24h'],
            'low_24h': criptomoneda['low_24h']
        })

    # Registrar los datos en la base de datos
    baseDeDatos.registrarDatos(datos_procesados, config)
else: 
    print("Error:", response.status_code)
