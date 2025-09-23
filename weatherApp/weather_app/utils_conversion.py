from datetime import datetime,timedelta

def kelvin_to_celcious(kelvin):
    return round(kelvin-273.15,2)

def kelvin_to_fahrenheit(kelvin):
    return round((kelvin-273.15)*(9/5)+32,2)

def unix_to_localtime(unix_time,timezone_offset_second):
    dt = datetime.utcfromtimestamp(unix_time) + timedelta(seconds=timezone_offset_second)
    return dt.strftime("%Y-%m-%d %H:%M:%S")
def wind_deg_to_compass(degree):
    directions=['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                  'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    idx = int((degree/22.5)+0.5)%16
    return directions[idx]
def meters_to_km(meters):
    if type(meters) == str:
        return meters
    else:
        return round(meters/1000,2)
def seconds_to_timezone(offset_seconds):
    sign = '+' if offset_seconds >= 0 else '-'
    offset_seconds = abs(offset_seconds)
    hours = offset_seconds // 3600
    minutes = (offset_seconds % 3600) // 60
    return f"{sign}{hours:02}:{minutes:02}GMT"
