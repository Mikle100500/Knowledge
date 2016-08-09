from cars.cars_list_conditions import find_car

cars_list = ["BMW M5", "BMW M3", "Porsche 911BMW", "Mercedes G63", "Morgan Aero", "Alpha Romeo Julette"]

assert find_car(cars_list, "BMW"), ["BMW M5", "BMW M3"]
assert find_car(cars_list, "Porsche") == ["Porsche 911BMW"]
assert find_car(cars_list, "Alpha Romeo") == ["Alpha Romeo Julette"]