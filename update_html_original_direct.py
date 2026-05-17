import os

logos_dir = 'logos'
all_files = sorted(os.listdir(logos_dir))

# Split into two rows
row1_files = all_files[:5]
row2_files = all_files[5:]

def build_track(files):
    html = []
    for f in files:
        html.append(f'                <div class="client-logo-item">\n                    <img src="logos/{f}" alt="Client Logo">\n                </div>')
    return '\n'.join(html)

row1_html = build_track(row1_files)
row1_set = f"<!-- Set 1 -->\n{row1_html}\n<!-- Set 2 -->\n{row1_html}\n<!-- Set 3 -->\n{row1_html}"

row2_html = build_track(row2_files)
row2_set = f"<!-- Set A -->\n{row2_html}\n<!-- Set B -->\n{row2_html}\n<!-- Set C -->\n{row2_html}"

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
# Replace Row 1
content = re.sub(
    r'(<div class="clients-track-wrapper">\s*<div class="clients-track">).*?(</div>\s*</div>\s*<!-- Row 2)',
    rf'\1\n{row1_set}\n            \2',
    content,
    flags=re.DOTALL
)

# Replace Row 2
content = re.sub(
    r'(<div class="clients-track-wrapper clients-track-reverse">\s*<div class="clients-track">).*?(</div>\s*</div>\s*</section>)',
    rf'\1\n{row2_set}\n            \2',
    content,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html to use original logos")
