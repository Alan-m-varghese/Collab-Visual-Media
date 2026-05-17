with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('src="logos/', 'src="assets/logos_cropped/')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated image paths.")
