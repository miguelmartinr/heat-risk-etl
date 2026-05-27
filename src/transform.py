# Transform

def transform_data(data):
    temp_madrid = {
        'ciudad': data['name'],
        'temperatura': data['main']['temp'],
        'humedad': data['main']['humidity'],
        'viento': data['wind']['speed'],
        'sensacion_termica': data['main']['feels_like'],
        'IRC': (data['main']['feels_like'])+((data['main']['humidity'])/10)
    }

    return temp_madrid
