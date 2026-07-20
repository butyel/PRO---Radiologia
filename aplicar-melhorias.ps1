# Aplica melhorias basicas em todos os HTML files
$files = Get-ChildItem "C:\Users\Raphael Fernandes\Desktop\PRO RADIOLOGIA PP\*.html"

foreach ($file in $files) {
    $path = $file.FullName
    $c = Get-Content $path -Raw
    
    # 1. Corrigir UTF-8
    $c = $c -replace 'charset="UTF-8"', 'charset="UTF-8"'
    
    # 2. Corrigir viewport
    $c = $c -replace 'content="width=device-width,initial-scale=1.0"', 'content="width=device-width, initial-scale=1.0"'
    
    # 3. Adicionar preconnect se não existir
    if ($c -notmatch 'rel="preconnect"') {
        $c = $c -replace '(?m)(<link href="https://fonts.googleapis.com/)', "<link rel=""preconnect"" href=""https://fonts.googleapis.com"">`n<link rel=""preconnect"" href=""https://fonts.gstatic.com"" crossorigin>`n`$1"
    }
    
    # 4. Corrigir nav - backdrop-filter apenas no scroll
    $c = $c -replace 'nav\{position:fixed;top:0;left:0;right:0;z-index:200;background:rgba\(255,255,255,\.96\);backdrop-filter:blur\(18px\);border-bottom:1px solid var\(--g2\);padding:0 5%;height:72px;display:flex;align-items:center;justify-content:space-between;transition:box-shadow \.3s\}', 'nav{position:fixed;top:0;left:0;right:0;z-index:200;background:rgba(255,255,255,.96);border-bottom:1px solid var(--g2);padding:0 5%;height:72px;display:flex;align-items:center;justify-content:space-between;transition:box-shadow .3s}'
    $c = $c -replace 'nav\.scrolled\{box-shadow:0 4px 28px rgba\(26,143,227,\.13\)\}', 'nav.scrolled{box-shadow:0 4px 28px rgba(26,143,227,.13);backdrop-filter:blur(18px)}'
    
    # 5. Corrigir reveal
    $c = $c -replace '(?s)\.reveal\{opacity:1;transform:none\}.*\.d4\{transition-delay:\.4s\}', ".reveal{opacity:0;transform:translateY(24px);transition:opacity .55s ease,transform .55s ease}`n.reveal.visible{opacity:1;transform:none}`n.d1{transition-delay:.1s}.d2{transition-delay:.2s}.d3{transition-delay:.3s}.d4{transition-delay:.4s}`n`n@media(prefers-reduced-motion:reduce){`n  *,*::before,*::after{animation:none!important;transition:none!important}`n  .reveal{opacity:1;transform:none;transition:none}`n}"
    
    Set-Content $path $c -NoNewline
    Write-Host "Processado: $($file.Name)"
}
Write-Host "Concluido!"