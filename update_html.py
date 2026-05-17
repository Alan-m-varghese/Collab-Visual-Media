import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

r1 = ['0124.png', 'Apex Logo.png', 'DP.jpg.png', 'IMG-20260223-WA0007.jpg.png', 'IMG_20240924_002810-removebg-preview.png']
html1 = ''
for i in range(3):
    html1 += f'                <!-- Set {i+1} -->\n'
    for img in r1:
        html1 += f'                <div class=\"client-logo-item\">\n                    <img src=\"assets/logos/{img}\" alt=\"Client Logo\">\n                </div>\n'

content = re.sub(r'(<!-- Row 1.*?<div class="clients-track">\s*)(<!-- Set 1 -->.*?)(            </div>\s*</div>\s*<!-- Row 2)', r'\1' + html1 + r'\3', content, flags=re.DOTALL)

r2 = ['LOGO ONLY white-01.png', 'Logo.png', 'PSM - Logo PNG-02.png', 'Satmya Logo.png', 'Yuva Logo Final-01.png', 'arya ayurveda hospital_LOGO.png']
html2 = ''
for i in range(3):
    html2 += f'                <!-- Set {chr(65+i)} -->\n'
    for img in r2:
        html2 += f'                <div class=\"client-logo-item\">\n                    <img src=\"assets/logos/{img}\" alt=\"Client Logo\">\n                </div>\n'

content = re.sub(r'(<!-- Row 2.*?<div class="clients-track">\s*)(<!-- Set A -->.*?)(            </div>\s*</div>\s*</section>)', r'\1' + html2 + r'\3', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html')
