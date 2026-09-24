import json
import re

with open('parse_data.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace("encoding=\"utf-8\"", "encoding=\"utf-8-sig\"")

with open('parse_data.py', 'w', encoding='utf-8') as f:
    f.write(code)
