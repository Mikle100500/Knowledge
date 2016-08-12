import json, requests

URL = 'http://uz.gov.ua/passengers/timetable/suggest-station/'

response = requests.get(URL)
object_list = response.json()

# new_python_object = json.loads(object_list)

print
len(object_list)
