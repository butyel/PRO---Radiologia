import re

# Read source files
with open('C:/Users/Raphael Fernandes/Desktop/PRO RADIOLOGIA PP/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

with open('C:/Users/Raphael Fernandes/Desktop/PRO RADIOLOGIA PP/tomografia.html', 'r', encoding='utf-8') as f:
    tomo_content = f.read()

# Extract CSS from index.html
css_start = index_content.find('<style>') + len('<style>')
css_end = index_content.find('</style>')
css = index_content[css_start:css_end]

# Extract JavaScript from index.html - get the LAST script tag (not the JSON-LD one)
# Find all script tags
script_positions = []
pos = 0
while True:
    pos = index_content.find('<script', pos)
    if pos == -1:
        break
    # Check if this is a script tag (not script type=application/ld+json)
    next_gt = index_content.find('>', pos)
    tag_content = index_content[pos:next_gt+1]
    if 'application/ld+json' not in tag_content:
        script_positions.append(pos)
    pos = next_gt + 1

# Get the last regular script tag
if script_positions:
    last_script_start = script_positions[-1]
    js_start = index_content.find('>', last_script_start) + 1
    js_end = index_content.find('</script>', js_start)
    js = index_content[js_start:js_end]
else:
    js = ''

print(f'CSS length: {len(css)}')
print(f'JS length: {len(js)}')

# Start building new HTML
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

# Extract nav from tomografia.html and fix it
nav_start = tomo_content.find('<nav')
nav_end = tomo_content.find('</nav>') + len('</nav>')
nav_content = tomo_content[nav_start:nav_end]
# Remove any existing role/aria-label to avoid duplication
nav_content = re.sub(r'role="[^"]*"', '', nav_content)
nav_content = re.sub(r'aria-label="[^"]*"', '', nav_content)
# Add correct role and aria-label
nav_content = nav_content.replace('<nav id="nav"', '<nav id="nav" role="navigation" aria-label="Main navigation"')
new_html += nav_content + '\n'

# Extract main content (from <section class="ph"> to before <footer>)
ph_start = tomo_content.find('<section class="ph"')
footer_start = tomo_content.find('<footer>')
main_content = tomo_content[ph_start:footer_start]
new_html += main_content + '\n'

# Extract and fix footer - remove Cloudflare, fix emails
footer_end = tomo_content.find('</footer>') + len('</footer>')
footer_content = tomo_content[footer_start:footer_end]
# Remove Cloudflare email protection links
footer_content = re.sub(r'<a href="/cdn-cgi/l/email-protection#[^"]*"[^>]*>.*?</a>', '<a href="mailto:contato@proradiologia.odo.br" title="E-mail">EM</a>', footer_content)
new_html += footer_content + '\n'

# Add WhatsApp float
waf_start = tomo_content.find('<a class="waf"')
waf_end = tomo_content.find('</a>', waf_start) + len('</a>')
waf_content = tomo_content[waf_start:waf_end]
new_html += waf_content + '\n'

# Add modal
movl_start = tomo_content.find('<div class="movl"')
# Find the end - before <script>
movl_end = tomo_content.find('<script>', movl_start)
movl_content = tomo_content[movl_start:movl_end]
new_html += movl_content + '\n'

# Add JavaScript
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
print(f'Total length: {len(new_html)}')
