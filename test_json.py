import json

with open('sentences.json', 'r', encoding='utf-8') as f:
    sentence_list = json.load(f)

print(f"Loaded {len(sentence_list)} sentences.")
