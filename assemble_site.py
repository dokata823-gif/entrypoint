import json

with open('template.html', 'r', encoding='utf-8') as f:
    template = f.read()

with open('sentences.json', 'r', encoding='utf-8') as f:
    sentences_str = f.read()

with open('mock_tests.json', 'r', encoding='utf-8') as f:
    mock_str = f.read()

final_html = template.replace('__SENTENCES_DATA__', sentences_str).replace('__MOCK_DATA__', mock_str)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

with open('entry_point.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print('Successfully assembled index.html and entry_point.html!')
