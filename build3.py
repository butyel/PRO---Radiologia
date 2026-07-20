import re

# Read files
with open('C:/Users/Raphael Fernandes/Desktop/PRO RADIOLOGIA PP/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

with open('C:/Users/Raphael Fernandes/Desktop/PRO RADIOLOGIA PP/tomografia.html', 'r', encoding='utf-8') as f:
    tomo_content = f.read()

# Extract CSS from index.html (between <style> and </style>)
css_start = index_content.find('<style>') + len('<style>')
css_end = index_content.find('</style>')
css = index_content[css_start:css_end]

# Extract JavaScript from index.html - get the LAST <script> tag
# Find all occurrences of '<script>' (exact match, not <script type=...>)
pos = 0
last_script_start = -1
while True:
    pos = index_content.find('<script>', pos)
    if pos == -1:
        break
    last_script_start = pos
    pos += 1

if last_script_start != -1:
    js_start = last_script_start + len('<script>')
    js_end = index_content.find('</script>', js_start)
    js = index_content[js_start:js_end]
else:
    js = ''

print(f'CSS length: {len(css)}')
print(f'JS length: {len(js)}')
print(f'JS starts with: {js[:50]}')

# Build new HTML
new_html = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tomografia 3D (CBCT) | PRO Radiologia - Presidente Prudente</title>
<meta name="description" content="Tomografia Cone Beam 3D em Presidente Prudente. Alta resolucao, baixa radiacao. Ideal para implantes, cirurgias e endodontia. Entrega digital DICOM em ate 1 hora.">
<meta name="keywords" content="tomografia cone beam presidente prudente, CBCT odontologico, tomografia 3D dental SP">
<meta property="og:title" content="Tomografia 3D (CBCT) | PRO Radiologia">
<meta property="og:description" content="Tomografia Cone Beam 3D em Presidente Prudente. Alta resolucao, baixa radiacao. Ideal para implantes, cirurgias e endodontia. Entrega digital DICOM em ate 1 hora.">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<style>
'''
new_html += css
new_html += '''
</style>
</head>
<body>
'''

# Extract and fix nav from tomografia.html
nav_start = tomo_content.find('<nav')
nav_end = tomo_content.find('</nav>') + len('</nav>')
nav_content = tomo_content[nav_start:nav_end]
# Add role and aria-label to nav
nav_content = nav_content.replace('<nav id="nav"', '<nav id="nav" role="navigation" aria-label="Main navigation"')
new_html += nav_content + '\n'

# Extract main content (from <section class="ph"> to before <footer>)
ph_start = tomo_content.find('<section class="ph"')
# Find the footer
footer_start = tomo_content.find('<footer>')
# Get content before footer (the page-body section)
main_content = tomo_content[ph_start:footer_start]
new_html += main_content + '\n'

# Extract and fix footer
footer_end = tomo_content.find('</footer>') + len('</footer>')
footer_content = tomo_content[footer_start:footer_end]
# Remove Cloudflare email protection and fix emails
footer_content = re.sub(r'<a href="/cdn-cgi/l/email-protection#[^"]*"[^>]*>.*?</a>', '<a href="mailto:contato@proradiologia.odo.br">contato@proradiologia.odo.br</a>', footer_content)
new_html += footer_content + '\n'

# Add WhatsApp float (before modal)
waf_start = tomo_content.find('<a class="waf"')
waf_end = tomo_content.find('</a>', waf_start) + len('</a>')
waf_content = tomo_content[waf_start:waf_end]
new_html += waf_content + '\n'

# Add modal
movl_start = tomo_content.find('<div class="movl"')
movl_end = tomo_content.find('</div>\n<script>')
if movl_end == -1:
    movl_end = tomo_content.find('</div>\n  <script>')
movl_content = tomo_content[movl_start:movl_end]
new_html += movl_content + '\n'

# Add JavaScript from index.html
new_html += '<script>'
new_html += js
new_html += '''
</script>
</body>
</html>'''

# Write the new file
with open('C:/Users/Raphael Fernandes/Desktop/PRO RADIOLOGIA PP/tomografia-new.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print('File created successfully!')
print(f'Total file length: {len(new_html)}')
