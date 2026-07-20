# Script para corrigir todos os HTML files
$files = Get-ChildItem "C:\Users\Raphael Fernandes\Desktop\PRO RADIOLOGIA PP\*.html"

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    
    # 1. Corrigir charset UTF-8
    $content = $content -replace 'charset="UTF-8"', 'charset="UTF-8"'
    
    # 2. Corrigir viewport
    $content = $content -replace 'content="width=device-width,initial-scale=1.0"', 'content="width=device-width, initial-scale=1.0"'
    
    # 3. Adicionar preconnect para Google Fonts (se não existir)
    if ($content -notmatch 'rel="preconnect"') {
        $content = $content -replace '(?m)(<link href="https://fonts.googleapis.com/)', '<link rel="preconnect" href="https://fonts.googleapis.com">' + "`n" + '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' + "`n" + '$1'
    }
    
    # 4. Corrigir backdrop-filter no nav (aplicar apenas quando scrolled)
    $content = $content -replace 'nav\{position:fixed;top:0;left:0;right:0;z-index:200;background:rgba\(255,255,255,\.96\);backdrop-filter:blur\(18px\);border-bottom:1px solid var\(--g2\);padding:0 5%;height:72px;display:flex;align-items:center;justify-content:space-between;transition:box-shadow \.3s\}', 'nav{position:fixed;top:0;left:0;right:0;z-index:200;background:rgba(255,255,255,.96);border-bottom:1px solid var(--g2);padding:0 5%;height:72px;display:flex;align-items:center;justify-content:space-between;transition:box-shadow .3s}' -replace 'nav\.scrolled\{box-shadow:0 4px 28px rgba\(26,143,227,\.13\)\}', 'nav.scrolled{box-shadow:0 4px 28px rgba(26,143,227,.13);backdrop-filter:blur(18px)}'
    
    # 5. Corrigir reveal animation
    $content = $content -replace '(?s)\.reveal\{opacity:1;transform:none\}.*\.d4\{transition-delay:\.4s\}', '.reveal{opacity:0;transform:translateY(24px);transition:opacity .55s ease,transform .55s ease}' + "`n" + '.reveal.visible{opacity:1;transform:none}' + "`n" + '.d1{transition-delay:.1s}.d2{transition-delay:.2s}.d3{transition-delay:.3s}.d4{transition-delay:.4s}' + "`n" + '`n@media(prefers-reduced-motion:reduce){`n  *,*::before,*::after{animation:none!important;transition:none!important}`n  .reveal{opacity:1;transform:none;transition:none}`n}'
    
    # 6. Adicionar role="navigation" na nav
    $content = $content -replace '<nav id="nav">', '<nav id="nav" role="navigation" aria-label="Main navigation">'
    
    # 7. Corrigir emails da Cloudflare
    $content = $content -replace '(?s)<a href="/cdn-cgi/l/email-protection[^>]*>[^<]*</a>', '<a href="mailto:contato@proradiologia.odo.br">contato@proradiologia.odo.br</a>' -replace '<span class="__cf_email__" data-cfemail="[^"]*">\[email&#160;protected\]</span>', 'contato@proradiologia.odo.br'
    
    # 8. Remover script da Cloudflare
    $content = $content -replace '<script data-cfasync="false" src="/cdn-cgi/scripts/[^"]*"></script>', ''
    
    Set-Content $file.FullName $content -NoNewline
    Write-Host "Fixed: $($file.Name)"
}
Write-Host "All files fixed!"