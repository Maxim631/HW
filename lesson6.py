# 1.
s = b'r\xc3\xa9sum\xc3\xa9'
print(s.decode('UTF-8'))
print(s.decode('Latin1'))

# 2.
a = 'first name'
b = 'second name'
c = 'age'
d = 'city'

with open("abcd.txt", "w") as file:
    file.write(a + '\n' + b + '\n')


with open("abcd.txt", "a") as file:
    file.write(c + '\n' + d)

# 3.
import json
import csv
json_dict = {
    123456: ('Paul', 29),
    567893: ('Wayne', 34),
    216489: ('Marcus', 24),
    977827: ('Harry', 26),
    123377: ('Bruno', 28),
    }

with open("venv/write_json.json", "w") as file:
    json.dump(json_dict, file)

# 4.
with open("venv/write_json.json", "r") as file:
    data: list = file.readlines()

    print(data)


# with open('names.csv', 'w', newline='') as csvfile:


