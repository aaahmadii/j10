source_file = 'copy.txt'
destination_file = 'paste.txt'

with open(source_file, 'r', encoding='utf-8') as src:
    content = src.read()

with open(destination_file, 'w', encoding='utf-8') as dest:
    dest.write(content)

print(f'محتوای {source_file} به {destination_file} کپی شد.')
