import json
numbers = [1, 5, 34, 56, 1, 5, 76]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
