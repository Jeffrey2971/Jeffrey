import json

with open('./data.json') as f:
    print(json.loads(f.read()))
