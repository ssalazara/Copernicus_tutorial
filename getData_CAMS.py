import cdsapi

#Instanciamos el cliente para solicitar la información
c = cdsapi.Client()

#Especificamos la fuente a la que consultamos la información
c.retrieve(
    'cams-solar-radiation-timeseries',
    {
        #Especificamos la locación, en este caso de ejemplo Chillán
        'location': {
            'latitude': -36.60664,
            'longitude': -72.10344,
        },
        'altitude': '-999.', #Este dato se deja en -999 para que busque en su fuente la altitud si es que existe
        'sky_type': 'clear',
        'date': '2015-11-01/2023-03-01', #Fecha desde y hasta de la búsqueda de datos
        'time_step': '1minute', 
        'time_reference': 'universal_time',
        'format': 'csv_expert',
    },
    'download.csv_expert') #Descarga del archivo final

#Toda esta inforamción se entrega en la plataforma de consulta
