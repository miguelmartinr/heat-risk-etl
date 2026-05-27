import requests
import json

def extract_data():
    url = "https://api.openweathermap.org/data/2.5/weather"
    params={
        'q': 'Madrid',
        "appid": 'cfd268431d027c3ce8a8520557211d60',
        'units': 'metric'
    }

    response = requests.get(url, params)
    
    if response.status_code == 200:
        data= response.json()

        with open(r'C:\Users\MIguel\Documents\etl-git\heat-risk-etl\madrid_raw.json', mode='w', encoding='utf-8') as save_file:
            json.dump(data, save_file, indent=4)

        return data

    elif response.status_code == 401:

        print('Error: Authentication Problem')

    else:
        print('Unexpected error')
    