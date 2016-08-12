import requests

URL = 'http://uz.gov.ua/passengers/timetable/suggest-station/'
result_data = requests.get(URL)
json_data = result_data.json()
# to_write = open('stations_uz_gov.txt', 'w', encoding='utf-8')
# to_write.write(str(json_data))
# to_write.close()

print(json_data)