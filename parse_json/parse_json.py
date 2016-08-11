import json

python_object = open('forecast.json').read()
new_python_object = json.loads(python_object)

output_to_file = open('output_json.txt', 'w')
output_to_file.write(str(new_python_object["currently"]["temperature"]))

# currently -> temperature