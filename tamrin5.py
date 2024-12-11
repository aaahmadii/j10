import requests
import json
from datetime import datetime
from persiantools.jdatetime import JalaliDate

def get_air_quality(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        aqi = data['data']['aqi']
        return aqi
    else:
        print("خطا در دریافت داده‌ها")
        return None

def save_to_file(date, aqi):
    filename = 'air_quality_data.txt'
    with open(filename, 'a') as file:
        file.write(f"{date} - AQI: {aqi}\n")

api_url = 'https://waqi.info/fa/#/c/3.683/8.444/2z'

aqi = get_air_quality(api_url)

if aqi is not None:
    jalali_date = JalaliDate.today()
    formatted_date = jalali_date.strftime('%Y/%m/%d')
    
    save_to_file(formatted_date, aqi)
    print(f"داده‌ها با موفقیت ذخیره شدند: {formatted_date} - AQI: {aqi}")
