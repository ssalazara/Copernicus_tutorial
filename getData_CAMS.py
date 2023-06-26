import cdsapi

c = cdsapi.Client()

c.retrieve(
    'cams-solar-radiation-timeseries',
    {
        'location': {
            'latitude': -36.60664,
            'longitude': -72.10344,
        },
        'altitude': '-999.',
        'sky_type': 'clear',
        'date': '2015-11-01/2023-03-01',
        'time_step': '1minute',
        'time_reference': 'universal_time',
        'format': 'csv_expert',
    },
    'download.csv_expert')
