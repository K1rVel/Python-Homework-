import json
import pytjs

my_js={
    "name": 'Kirill',
    "age": 18,
    "country": [{
        "name": "Russia",
        "time": "17",
        "city": "Sochi"
    }]
}

my_jsonchik=json.dumps(my_js)
with open('my.json', 'w') as f:
    f.write(my_jsonchik)