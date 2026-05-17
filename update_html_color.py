with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('src="assets/logos/', 'src="assets/logos_color/')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html to use logos_color')
