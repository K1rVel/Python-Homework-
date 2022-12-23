import json

my_js={
    "name": "Kirill",
    "age": "18",
    "country": "Russia"
}

my_jsonchik=json.dumps(my_js)
with open('my.json', 'w') as write_file:
    write_file.write(my_jsonchik)