import re

# Read files
with open('C:/Users/Raphael Fernandes/Desktop/PRO RADIOLOGIA PP/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

with open('C:/Users/Raphael Fernandes/Desktop/PRO RADIOLOGIA PP/tomografia.html', 'r', encoding='utf-8') as f:
    tomo_content = f.read()

# Extract CSS from index.html
css_start = index_content.find('<style>') + len('<style>')
css_end = index_content.find('</style>')
css = index_content[css_start:css_end]

# Extract JS from index.html
js_start = index_content.find('<script>') + len('<script>')
js_end = index_content.find('</script>')
js = index_content[js_start:js_end]

print('CSS length:', len(css))
print('JS length:', len(js))

# Build new HTML header
new_html = '<!DOCTYPE html>\n<html lang=\"pt-BR\">\n<head>\n'
new_html += '<meta charset=\"UTF-8\">\n'
new_html += '<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n'
new_html += '<title>Tomografia 3D (CBCT) | PRO Radiologia – Presidente Prudente</title>\n'
new_html += '<meta name=\"description\" content=\"Tomografia Cone Beam 3D em Presidente Prudente. Alta resolução, baixa radiação. Ideal para implantes, cirurgias e endodontia. Entrega digital DICOM em até 1 hora.\">\n'
new_html += '<meta name=\"keywords\" content=\"tomografia cone beam presidente prudente, CBCT odontológico, tomografia 3D dental SP\">\n'
new_html += '<meta property=\"og:title\" content=\"Tomografia 3D (CBCT) | PRO Radiologia\">\n'
new_html += '<meta property=\"og:description\" content=\"Tomografia Cone Beam 3D em Presidente Prudente. Alta resolução, baixa radiação. Ideal para implantes, cirurgias e endodontia. Entrega digital DICOM em até 1 hora.\">\n'
new_html += '<meta property=\"og:type\" content=\"website\">\n'
new_html += '<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n'
new_html += '<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n'
new_html += '<link href=\"https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,400&display=swap\" rel=\"stylesheet\">\n'
new_html += '<style>\n'
new_html += css
new_html += '\n</style>\n</head>\n<body>\n'

# Add nav with role and aria-label from tomografia.html
nav_start = tomo_content.find('<nav')
nav_end = tomo_content.find('</nav>') + len('</nav>')
nav_content = tomo_content[nav_start:nav_end]
nav_content = nav_content.replace('<nav id=\"nav\"', '<nav id=\"nav\" role=\"navigation\" aria-label=\"Main navigation\"')
new_html += nav_content + '\n'

# Add page body content (ph section and page-body)
ph_start = tomo_content.find('<section class=\"ph\"')
# Find the end of page-body div
page_body_end = tomo_content.find('</aside>\n</div>\n<footer>')
if page_body_end == -1:
    page_body_end = tomo_content.find('</aside>\n  </div>\n<footer>')
page_body_content = tomo_content[ph_start:page_body_end]
new_html += page_body_content + '\n'

# Add footer with corrected email (no Cloudflare)
footer_start = tomo_content.find('<footer>')
footer_end = tomo_content.find('</footer>') + len('</footer>')
footer_content = tomo_content[footer_start:footer_end]
# Remove Cloudflare email protection links
footer_content = re.sub(r'<a href=\"/cdn-cgi/l/email-protection#[^"]*\"[^>]*>.*?</a>', '<a href=\"mailto:contato@proradiologia.odo.br\" title=\"E-mail\">✉️</a>', footer_content)
new_html += footer_content + '\n'

# Add WhatsApp float
waf_start = tomo_content.find('<a class=\"waf\"')
waf_end = tomo_content.find('</a>', waf_start) + len('</a>')
waf_content = tomo_content[waf_start:waf_end]
new_html += waf_content + '\n'

# Add modal
movl_start = tomo_content.find('<div class=\"movl\"')
movl_end = tomo_content.find('</div>\n<script>')
if movl_end == -1:
    movl_end = tomo_content.find('</div>\n<script')
movl_content = tomo_content[movl_start:movl_end]
new_html += movl_content + '\n'

# Add JavaScript from index.html
new_html += '<script>\n'
new_html += js
new_html += '\n</script>\n</body>\n</html>'

# Write the new file
with open('C:/Users/Raphael Fernandes/Desktop/PRO RADIOLOGIA PP/tomografia-new.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print('File created successfully: tomografia-new.html')
