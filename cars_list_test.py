from cars_list_conditions import find_car

cars_list = ["BMW M5", "BMW M3", "Porsche 911BMW", "Mercedes G63", "Morgan Aero"]

assert find_car(cars_list, "BMW") == ["BMW M5", "BMW M3"]
assert find_car(cars_list, "Porsche") == ["Porsche 911BMW"]
