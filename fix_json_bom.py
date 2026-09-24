import json

with open('sentences.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

with open('sentences.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('sentences.json resaved cleanly as utf-8')
