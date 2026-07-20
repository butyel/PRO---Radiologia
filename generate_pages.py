#!/usr/bin/env python3
"""Generate all remaining HTML pages for PRO Radiologia."""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def read_shared_assets():
    """Read the shared assets to embed."""
    return

def make_page(**kwargs):
    """Build a full HTML page from common parts."""
    title = kwargs.get('title', 'PRO Radiologia Odontol\u00f3gica')
    description = kwargs.get('description', 'Exames de radiologia odontol\u00f3gica no Oeste Paulista.')
    canonical = kwargs.get('canonical', 'https://proradiologia.odo.br')
    og_title = kwargs.get('og_title', title)
    og_desc = kwargs.get('og_desc', description)
    h1 = kwargs.get('h1', '')
    breadcrumb = kwargs.get('breadcrumb', '')
    content = kwargs.get('content', '')
    body_class = kwargs.get('body_class', '')
    noindex = kwargs.get('noindex', False)
    jsonld = kwargs.get('jsonld', '')

    robots = 'noindex, nofollow' if noindex else 'index, follow'

    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="{robots}">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{canonical}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/styles.css">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
{jsonld}
<script src="/assets/data.js" defer></script>
<script src="/assets/icons.js" defer></script>
<script src="/assets/scripts.js" defer></script>
</head>
<body class="{body_class}">

<a class="skip-link" href="#main">Ir para o conte\u00fado principal</a>

<nav id="nav" role="navigation" aria-label="Navega\u00e7\u00e3o principal">
  <a class="nav-logo" href="/" aria-label="PRO Radiologia - P\u00e1gina inicial">
    <img class="nav-logo-icon" src="/imagens/logo-pro.png" alt="PRO Radiologia" width="42" height="42">
    <div class="nav-logo-text">
      <strong>PRO Radiologia</strong>
      <span>Centro de Radiologia Odontol\u00f3gica</span>
    </div>
  </a>
  <ul class="nav-links" role="menubar">
    <li role="none"><a href="/" role="menuitem">Home</a></li>
    <li role="none">
      <a href="#" role="menuitem" aria-haspopup="true" aria-expanded="false">
        Exames <span class="chevron" aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="14" height="14"><path d="M6 9l6 6 6-6"/></svg></span>
      </a>
      <ul class="dropdown" role="menu">
        <li role="none"><a href="/exames/documentacao-ortodontica/" role="menuitem">Documenta\u00e7\u00e3o Ortod\u00f4ntica</a></li>
        <li role="none"><a href="/exames/radiografia-panoramica/" role="menuitem">Radiografia Panor\u00e2mica</a></li>
        <li role="none"><a href="/exames/radiografia-periapical/" role="menuitem">Radiografia Periapical</a></li>
        <li role="none"><a href="/exames/radiografia-interproximal/" role="menuitem">Radiografia Interproximal</a></li>
        <li role="none"><a href="/exames/tomografia-cone-beam/" role="menuitem">Tomografia Cone Beam</a></li>
        <li role="none"><a href="/exames/telerradiografia/" role="menuitem">Telerradiografia</a></li>
        <li role="none"><a href="/exames/scanner-intraoral/" role="menuitem">Scanner Intraoral 3D</a></li>
      </ul>
    </li>
    <li role="none">
      <a href="#" role="menuitem" aria-haspopup="true" aria-expanded="false">
        Unidades <span class="chevron" aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="14" height="14"><path d="M6 9l6 6 6-6"/></svg></span>
      </a>
      <ul class="dropdown" role="menu">
        <li role="none"><a href="/unidades/presidente-prudente/" role="menuitem">Presidente Prudente</a></li>
        <li role="none"><a href="/unidades/presidente-epitacio/" role="menuitem">Presidente Epit\u00e1cio</a></li>
        <li role="none"><a href="/unidades/teodoro-sampaio/" role="menuitem">Teodoro Sampaio</a></li>
      </ul>
    </li>
    <li role="none"><a href="/para-dentistas/" role="menuitem">Para Dentistas</a></li>
    <li role="none"><a href="/para-pacientes/" role="menuitem">Para Pacientes</a></li>
    <li role="none"><a href="/blog/" role="menuitem">Blog</a></li>
    <li role="none"><a href="/contato/" role="menuitem">Contato</a></li>
  </ul>
  <div class="nav-actions">
    <a href="tel:1832229225" class="btn-outline" aria-label="Ligar para (18) 3222-9225">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
      (18) 3222-9225
    </a>
    <button class="btn-primary" onclick="openModal()" aria-label="Agendar Exame">Agendar Exame &rarr;</button>
  </div>
  <button class="nav-toggle" aria-label="Abrir menu" aria-expanded="false">
    <span></span><span></span><span></span>
  </button>
</nav>

<main id="main">
<section class="ph">
  <div class="ph-inner">
    {breadcrumb}
    {h1}
  </div>
</section>

<div class="page-body-full">
  {content}
</div>

</main>

<footer role="contentinfo">
  <div class="fg-grid">
    <div>
      <img class="fli" src="/imagens/logo-white.png" alt="PRO Radiologia" width="44" height="44">
      <div class="flogo"><strong>PRO Radiologia</strong><span>Centro de Radiologia Odontol\u00f3gica</span></div>
      <p class="fabout">H\u00e1 mais de 40 anos, a PRO Radiologia apoia dentistas e pacientes com exames de imagem em 3 unidades no Oeste Paulista.</p>
      <div class="fsoc">
        <a href="#" class="fsb" aria-label="Instagram" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg></a>
        <a href="#" class="fsb" aria-label="Facebook" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
      </div>
    </div>
    <div class="fcol">
      <h4>Exames</h4>
      <ul class="flinks">
        <li><a href="/exames/documentacao-ortodontica/">Documenta\u00e7\u00e3o Ortod\u00f4ntica</a></li>
        <li><a href="/exames/radiografia-panoramica/">Radiografia Panor\u00e2mica</a></li>
        <li><a href="/exames/radiografia-periapical/">Radiografia Periapical</a></li>
        <li><a href="/exames/tomografia-cone-beam/">Tomografia Cone Beam</a></li>
        <li><a href="/exames/scanner-intraoral/">Scanner Intraoral 3D</a></li>
      </ul>
    </div>
    <div class="fcol">
      <h4>Unidades</h4>
      <ul class="flinks">
        <li><a href="/unidades/presidente-prudente/">Presidente Prudente</a></li>
        <li><a href="/unidades/presidente-epitacio/">Presidente Epit\u00e1cio</a></li>
        <li><a href="/unidades/teodoro-sampaio/">Teodoro Sampaio</a></li>
      </ul>
      <h4 style="margin-top:20px">Links</h4>
      <ul class="flinks">
        <li><a href="/para-dentistas/">Para Dentistas</a></li>
        <li><a href="/para-pacientes/">Para Pacientes</a></li>
        <li><a href="/requisicao-de-exames/">Requisi\u00e7\u00e3o de Exames</a></li>
        <li><a href="/blog/">Blog</a></li>
      </ul>
    </div>
    <div class="fcol">
      <h4>Contato</h4>
      <div class="fci-list">
        <div class="fci">
          <svg class="fci-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" width="16" height="16"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          <div><strong>Matriz</strong><span>Av. Washington Luiz, 874, 7\u00ba andar</span></div>
        </div>
        <div class="fci">
          <svg class="fci-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" width="16" height="16"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <div><strong>Telefone</strong><span>(18) 3222-9225</span></div>
        </div>
        <div class="fci">
          <svg class="fci-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" width="16" height="16"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
          <div><strong>WhatsApp</strong><span>(18) 98153-0505</span></div>
        </div>
        <div class="fci">
          <svg class="fci-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" width="16" height="16"><polyline points="22 6 12 13 2 6"/><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/></svg>
          <div><strong>E-mail</strong><span>contato@proradiologia.odo.br</span></div>
        </div>
      </div>
    </div>
  </div>
  <div class="fbot">
    <p>&copy; <span class="current-year">2026</span> PRO Radiologia. Todos os direitos reservados.</p>
    <p><a href="/politica-de-privacidade/" style="color:rgba(255,255,255,.35);text-decoration:none">Pol\u00edtica de Privacidade</a> &middot; <a href="/termos-de-uso/" style="color:rgba(255,255,255,.35);text-decoration:none">Termos de Uso</a></p>
  </div>
</footer>

<div class="movl" role="dialog" aria-modal="true" aria-label="Agendamento de exame">
  <div class="modal">
    <div class="mh">
      <div>
        <h3>Agendar Exame</h3>
        <p>Preencha os dados e entraremos em contato.</p>
      </div>
      <button class="mcl" onclick="closeModal()" aria-label="Fechar">&times;</button>
    </div>
    <div class="mb">
      <form id="bookingForm" novalidate>
        <div class="mfrow">
          <div class="mfg">
            <label for="modalNome">Nome *</label>
            <input type="text" id="modalNome" name="nome" required placeholder="Seu nome completo">
            <span class="error-msg" role="alert">Campo obrigat\u00f3rio</span>
          </div>
          <div class="mfg">
            <label for="modalTelefone">Telefone / WhatsApp *</label>
            <input type="tel" id="modalTelefone" name="telefone" required placeholder="(18) 99999-0000">
            <span class="error-msg" role="alert">Telefone inv\u00e1lido</span>
          </div>
        </div>
        <div class="mfrow">
          <div class="mfg">
            <label for="modalExame">Tipo de Exame *</label>
            <select id="modalExame" name="exame" required>
              <option value="">Selecione</option>
              <option value="documentacao-ortodontica">Documenta\u00e7\u00e3o Ortod\u00f4ntica</option>
              <option value="radiografia-panoramica">Radiografia Panor\u00e2mica</option>
              <option value="radiografia-periapical">Radiografia Periapical</option>
              <option value="radiografia-interproximal">Radiografia Interproximal</option>
              <option value="tomografia-cone-beam">Tomografia Cone Beam</option>
              <option value="telerradiografia">Telerradiografia</option>
              <option value="scanner-intraoral">Scanner Intraoral 3D</option>
            </select>
            <span class="error-msg" role="alert">Selecione um exame</span>
          </div>
          <div class="mfg">
            <label for="modalUnidade">Unidade *</label>
            <select id="modalUnidade" name="unidade" required>
              <option value="">Selecione</option>
              <option value="presidente-prudente">Presidente Prudente</option>
              <option value="presidente-epitacio">Presidente Epit\u00e1cio</option>
              <option value="teodoro-sampaio">Teodoro Sampaio</option>
            </select>
            <span class="error-msg" role="alert">Selecione uma unidade</span>
          </div>
        </div>
        <div class="mfg">
          <label for="modalEmail">E-mail</label>
          <input type="email" id="modalEmail" name="email" placeholder="email@exemplo.com">
        </div>
        <div class="mfg">
          <label for="modalMensagem">Mensagem</label>
          <textarea id="modalMensagem" name="mensagem" rows="3" placeholder="Hor\u00e1rio de prefer\u00eancia, d\u00favidas..." style="padding:12px 16px;border-radius:var(--rs);border:1.5px solid var(--g2);font-family:var(--font-sans);font-size:14px;color:var(--g9);background:var(--g1);transition:all .2s;outline:none;width:100%;resize:vertical;min-height:80px"></textarea>
        </div>
        <button class="msub" type="submit">Enviar Agendamento</button>
      </form>
      <div class="msucc">
        <h4>Agendamento enviado!</h4>
        <p>Recebemos sua solicita\u00e7\u00e3o e retornaremos em breve.</p>
        <p style="margin-top:16px;font-size:13px">Se preferir, fale conosco pelo <a href="https://wa.me/5518981530505" target="_blank">WhatsApp</a>.</p>
      </div>
    </div>
  </div>
</div>

<a class="waf" href="https://wa.me/5518981530505" target="_blank" rel="noopener noreferrer" aria-label="Fale pelo WhatsApp">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="28" height="28"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
</a>

</body>
</html>'''


def write_file(path, content):
    full_path = os.path.join(BASE_DIR, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created: {path}')


def make_breadcrumb(items):
    """items is a list of (title, url) tuples. Last item is current page (no link)."""
    parts = []
    for title, url in items[:-1]:
        parts.append(f'<a href="{url}">{title}</a><span>\u203a</span>')
    parts.append(f'<span>{items[-1][0]}</span>')
    return f'<nav class="breadcrumb" aria-label="Breadcrumb">{"".join(parts)}</nav>'


def make_ptag(text):
    return f'<div class="ptag">{text}</div>'


def make_ptitle(h1_text, span_text=''):
    if span_text:
        return f'<h1 class="ptitle">{h1_text} <span>{span_text}</span></h1>'
    return f'<h1 class="ptitle">{h1_text}</h1>'


# EXAM PAGES
EXAM_PAGES = {
    'exames/documentacao-ortodontica.html': {
        'title': 'Documenta\u00e7\u00e3o Ortod\u00f4ntica Completa | PRO Radiologia',
        'description': 'Documenta\u00e7\u00e3o ortod\u00f4ntica completa com panor\u00e2mica, telerradiografia e fotografias. Agende na PRO Radiologia no Oeste Paulista.',
        'canonical': 'https://proradiologia.odo.br/exames/documentacao-ortodontica/',
        'tag': 'Ortodontia',
        'h1': 'Documenta\u00e7\u00e3o Ortod\u00f4ntica',
        'h1_span': 'planejamento completo',
        'content': '''
<div class="article">
<h2>O que \u00e9 a Documenta\u00e7\u00e3o Ortod\u00f4ntica?</h2>
<p>A <strong>Documenta\u00e7\u00e3o Ortod\u00f4ntica</strong> \u00e9 um conjunto de exames que fornece ao ortodontista todas as informa\u00e7\u00f5es necess\u00e1rias para o diagn\u00f3stico e planejamento do tratamento ortod\u00f4ntico. Ela permite avaliar a estrutura \u00f3ssea, a posi\u00e7\u00e3o dos dentes e as rela\u00e7\u00f5es entre as arcadas dent\u00e1rias.</p>

<p>Uma documenta\u00e7\u00e3o bem elaborada \u00e9 a base para um tratamento ortod\u00f4ntico previs\u00edvel e seguro.</p>

<h2>Exames que comp\u00f5em a Documenta\u00e7\u00e3o</h2>
<ul>
<li><strong>Radiografia Panor\u00e2mica:</strong> Vis\u00e3o geral de todos os dentes, estruturas \u00f3sseas e seios maxilares.</li>
<li><strong>Telerradiografia (Rx lateral):</strong> An\u00e1lise cefalom\u00e9trica para avaliar crescimento facial e rela\u00e7\u00f5es esquel\u00e9ticas.</li>
<li><strong>Fotografias intra e extraorais:</strong> Registro visual da condi\u00e7\u00e3o inicial do paciente.</li>
<li><strong>Modelos digitais (opcional):</strong> Escaneamento intraoral 3D para planejamento digital.</li>
</ul>

<h2>Para quem \u00e9 indicada?</h2>
<ul>
<li>Pacientes que iniciar\u00e3o tratamento ortod\u00f4ntico (aparelhos fixos ou alinhadores)</li>
<li>Avalia\u00e7\u00e3o de crescimento facial em crian\u00e7as e adolescentes</li>
<li>Planejamento de cirurgia ortogn\u00e1tica combinada com ortodontia</li>
<li>Pacientes com assimetrias faciais ou problemas de mordida</li>
</ul>

<div class="hbox"><p>A documenta\u00e7\u00e3o ortod\u00f4ntica \u00e9 um ato m\u00e9dico-odontol\u00f3gico que deve ser solicitado por cirurgi\u00e3o-dentista habilitado.</p></div>

<h2>Como \u00e9 realizada?</h2>
<p>O paciente realiza os exames na unidade em \u00fanica visita. A captura das imagens \u00e9 r\u00e1pida e n\u00e3o invasiva. As fotografias s\u00e3o obtidas com equipamento espec\u00edfico para documenta\u00e7\u00e3o odontol\u00f3gica.</p>

<h2>Unidades que realizam o exame</h2>
<p>A documenta\u00e7\u00e3o ortod\u00f4ntica est\u00e1 dispon\u00edvel em todas as unidades da PRO Radiologia: <a href="/unidades/presidente-prudente/">Presidente Prudente</a>, <a href="/unidades/presidente-epitacio/">Presidente Epit\u00e1cio</a> e <a href="/unidades/teodoro-sampaio/">Teodoro Sampaio</a>.</p>

<div class="cta-inline">
<h3>Agende sua Documenta\u00e7\u00e3o Ortod\u00f4ntica</h3>
<p>Realize seus exames com qualidade e agilidade.</p>
<button onclick="openModal()" class="hbtn-main" style="display:inline-flex;margin:0 auto 12px;text-decoration:none;font-size:14px;padding:12px 28px">Agendar Agora</button>
</div>

<div class="wbox"><p>As informa\u00e7\u00f5es neste site t\u00eam car\u00e1ter educativo e n\u00e3o substituem a consulta com um profissional de sa\u00fade.</p></div>
</div>'''
    },
    'exames/radiografia-panoramica.html': {
        'title': 'Radiografia Panor\u00e2mica Digital | PRO Radiologia',
        'description': 'Radiografia panor\u00e2mica digital: imagem completa da arcada dent\u00e1ria. R\u00e1pida, confort\u00e1vel e com baixa dose de radia\u00e7\u00e3o.',
        'canonical': 'https://proradiologia.odo.br/exames/radiografia-panoramica/',
        'tag': 'Exame',
        'h1': 'Radiografia Panor\u00e2mica',
        'h1_span': 'vis\u00e3o completa da arcada dent\u00e1ria',
        'content': '''
<div class="article">
<h2>O que \u00e9 a Radiografia Panor\u00e2mica?</h2>
<p>A <strong>Radiografia Panor\u00e2mica</strong> (tamb\u00e9m conhecida como ortopantomografia) \u00e9 um exame de imagem que captura toda a arcada dent\u00e1ria, mand\u00edbula, maxila, seios maxilares e articula\u00e7\u00f5es temporomandibulares em uma \u00fanica imagem bidimensional.</p>

<h2>Principais aplica\u00e7\u00f5es</h2>
<ul>
<li>Avalia\u00e7\u00e3o geral da sa\u00fade bucal</li>
<li>Planejamento de extra\u00e7\u00f5es de dentes do siso</li>
<li>Avalia\u00e7\u00e3o pr\u00e9-prot\u00e9tica e pr\u00e9-implantod\u00f4ntica</li>
<li>Diagn\u00f3stico de cistos, tumores e les\u00f5es \u00f3sseas</li>
<li>Avalia\u00e7\u00e3o periodontal</li>
<li>Check-up odontol\u00f3gico geral</li>
</ul>

<h2>Como \u00e9 realizado?</h2>
<p>O paciente posiciona-se em p\u00e9 ou sentado, com o queixo apoiado em um suporte. O equipamento gira ao redor da cabe\u00e7a capturando a imagem. O exame dura aproximadamente 20 segundos e \u00e9 indolor.</p>

<h2>Preparo necess\u00e1rio</h2>
<p>N\u00e3o \u00e9 necess\u00e1rio preparo especial. Recomenda-se remover brincos, piercings orais e pr\u00f3teses remov\u00edveis antes do exame.</p>

<div class="cta-inline">
<h3>Agende sua Radiografia Panor\u00e2mica</h3>
<p>Dispon\u00edvel em todas as unidades. Entrega digital.</p>
<button onclick="openModal()" class="hbtn-main" style="display:inline-flex;margin:0 auto 12px;text-decoration:none;font-size:14px;padding:12px 28px">Agendar Agora</button>
</div>
</div>'''
    },
    'exames/radiografia-periapical.html': {
        'title': 'Radiografia Periapical | PRO Radiologia',
        'description': 'Radiografia periapical digital para avalia\u00e7\u00e3o detalhada de dentes e ra\u00edzes. Essencial para endodontia e diagn\u00f3stico odontol\u00f3gico.',
        'canonical': 'https://proradiologia.odo.br/exames/radiografia-periapical/',
        'tag': 'Exame',
        'h1': 'Radiografia Periapical',
        'h1_span': 'avalia\u00e7\u00e3o detalhada dente a dente',
        'content': '''
<div class="article">
<h2>O que \u00e9 a Radiografia Periapical?</h2>
<p>A <strong>Radiografia Periapical</strong> \u00e9 um exame de imagem intraoral que captura um ou mais dentes individualmente, incluindo toda a extens\u00e3o da raiz e o osso alveolar ao redor. \u00c9 o exame mais utilizado na pr\u00e1tica odontol\u00f3gica para diagn\u00f3stico localizado.</p>

<h2>Principais aplica\u00e7\u00f5es</h2>
<ul>
<li>Diagn\u00f3stico de c\u00e1ries e les\u00f5es periapicais</li>
<li>Avalia\u00e7\u00e3o de tratamentos de canal (endodontia)</li>
<li>Identifica\u00e7\u00e3o de abscessos e cistos</li>
<li>Planejamento de implantes unit\u00e1rios</li>
<li>Avalia\u00e7\u00e3o de traumas dentais</li>
</ul>

<h2>Como \u00e9 realizado?</h2>
<p>O sensor digital \u00e9 posicionado dentro da boca do paciente, atr\u00e1s do dente a ser examinado. O equipamento de raio-X \u00e9 posicionado externamente e a imagem \u00e9 capturada em segundos. O resultado \u00e9 imediato e visualizado em computador.</p>

<div class="cta-inline">
<h3>Dispon\u00edvel em todas as unidades</h3>
<button onclick="openModal()" class="hbtn-main" style="display:inline-flex;margin:0 auto 12px;text-decoration:none;font-size:14px;padding:12px 28px">Agendar Agora</button>
</div>
</div>'''
    },
    'exames/radiografia-interproximal.html': {
        'title': 'Radiografia Interproximal (Bite-wing) | PRO Radiologia',
        'description': 'Radiografia interproximal para detec\u00e7\u00e3o de c\u00e1ries entre os dentes. Exame preventivo essencial para check-ups odontol\u00f3gicos peri\u00f3dicos.',
        'canonical': 'https://proradiologia.odo.br/exames/radiografia-interproximal/',
        'tag': 'Exame',
        'h1': 'Radiografia Interproximal (Bite-wing)',
        'h1_span': 'detec\u00e7\u00e3o precoce de c\u00e1ries',
        'content': '''
<div class="article">
<h2>O que \u00e9 a Radiografia Interproximal?</h2>
<p>A <strong>Radiografia Interproximal</strong> (tamb\u00e9m conhecida como bite-wing) \u00e9 um exame intraoral espec\u00edfico para visualizar as coroas dos dentes superiores e inferiores em uma mesma imagem, permitindo a detec\u00e7\u00e3o de c\u00e1ries nas faces interproximais (entre os dentes) e avalia\u00e7\u00e3o da crista \u00f3ssea alveolar.</p>

<h2>Principais aplica\u00e7\u00f5es</h2>
<ul>
<li>Detec\u00e7\u00e3o precoce de c\u00e1ries interproximais</li>
<li>Avalia\u00e7\u00e3o da perda \u00f3ssea periodontal</li>
<li>Verifica\u00e7\u00e3o de adapta\u00e7\u00e3o de restaura\u00e7\u00f5es e pr\u00f3teses</li>
<li>Check-up odontol\u00f3gico preventivo</li>
</ul>

<div class="hbox"><p>Exame r\u00e1pido e indolor, essencial para a preven\u00e7\u00e3o e diagn\u00f3stico precoce de c\u00e1ries.</p></div>
</div>'''
    },
    'exames/tomografia-cone-beam.html': {
        'title': 'Tomografia Cone Beam (CBCT) | PRO Radiologia',
        'description': 'Tomografia Cone Beam odontol\u00f3gica 3D para implantes, cirurgias e diagn\u00f3sticos complexos. Exame de alta precis\u00e3o no Oeste Paulista.',
        'canonical': 'https://proradiologia.odo.br/exames/tomografia-cone-beam/',
        'tag': 'Tecnologia',
        'h1': 'Tomografia Cone Beam (CBCT)',
        'h1_span': 'imagem 3D de alta resolu\u00e7\u00e3o',
        'content': '''
<div class="article">
<h2>O que \u00e9 a Tomografia Cone Beam?</h2>
<p>A <strong>Tomografia Computadorizada de Feixe C\u00f4nico</strong> (CBCT) \u00e9 um exame de imagem tridimensional desenvolvido especificamente para odontologia. Diferente da tomografia m\u00e9dica convencional, o CBCT utiliza baixa dose de radia\u00e7\u00e3o e oferece alta resolu\u00e7\u00e3o para estruturas dentomaxilofaciais.</p>

<h2>Principais aplica\u00e7\u00f5es</h2>
<ul>
<li><strong>Implantodontia:</strong> Planejamento preciso de implantes com avalia\u00e7\u00e3o do volume \u00f3sseo</li>
<li><strong>Cirurgia bucomaxilofacial:</strong> Planejamento de cirurgias ortogn\u00e1ticas e remo\u00e7\u00e3o de dentes inclusos</li>
<li><strong>Endodontia:</strong> Diagn\u00f3stico de fraturas radiculares e anatomia de canais complexos</li>
<li><strong>Ortodontia:</strong> Avalia\u00e7\u00e3o de vias a\u00e9reas e planejamento de mini-implantes</li>
<li><strong>Periodontia:</strong> Avalia\u00e7\u00e3o 3D de defeitos \u00f3sseos</li>
</ul>

<h2>Como \u00e9 realizado?</h2>
<p>O paciente permanece sentado enquanto o equipamento realiza uma \u00fanica rota\u00e7\u00e3o ao redor da cabe\u00e7a. O exame dura de 15 a 40 segundos, dependendo do campo de vis\u00e3o selecionado.</p>

<h2>Preparo necess\u00e1rio</h2>
<p>Remover objetos met\u00e1licos da cabe\u00e7a e pesco\u00e7o (brincos, piercings, grampos de cabelo). Informar \u00e0 equipe se houver suspeita de gravidez.</p>

<div class="hbox"><p>A PRO Radiologia segue protocolos de qualidade, seguran\u00e7a e prote\u00e7\u00e3o radiol\u00f3gica aplic\u00e1veis aos servi\u00e7os de radiologia odontol\u00f3gica.</p></div>

<div class="cta-inline">
<h3>Agende sua Tomografia Cone Beam</h3>
<p>Dispon\u00edvel em todas as unidades.</p>
<button onclick="openModal()" class="hbtn-main" style="display:inline-flex;margin:0 auto 12px;text-decoration:none;font-size:14px;padding:12px 28px">Agendar Agora</button>
</div>
</div>'''
    },
    'exames/telerradiografia.html': {
        'title': 'Telerradiografia | PRO Radiologia',
        'description': 'Telerradiografia lateral da face para an\u00e1lise cefalom\u00e9trica. Exame essencial para ortodontia e cirurgia ortogn\u00e1tica no Oeste Paulista.',
        'canonical': 'https://proradiologia.odo.br/exames/telerradiografia/',
        'tag': 'Exame',
        'h1': 'Telerradiografia',
        'h1_span': 'an\u00e1lise cefalom\u00e9trica de precis\u00e3o',
        'content': '''
<div class="article">
<h2>O que \u00e9 a Telerradiografia?</h2>
<p>A <strong>Telerradiografia</strong> \u00e9 uma radiografia lateral da face obtida com uma dist\u00e2ncia padronizada entre o tubo de raio-X e o filme/sensor. Esta padroniza\u00e7\u00e3o permite realizar a <strong>cefalometria</strong>, que \u00e9 a an\u00e1lise de medidas e \u00e2ngulos da estrutura \u00f3ssea e dental da face.</p>

<h2>Principais aplica\u00e7\u00f5es</h2>
<ul>
<li>Planejamento ortod\u00f4ntico</li>
<li>Avalia\u00e7\u00e3o do crescimento facial</li>
<li>Diagn\u00f3stico de assimetrias</li>
<li>Planejamento de cirurgia ortogn\u00e1tica</li>
<li>Avalia\u00e7\u00e3o de vias a\u00e9reas superiores</li>
</ul>

<h2>Como \u00e9 realizada?</h2>
<p>O paciente posiciona-se ao lado do equipamento, com a cabe\u00e7a estabilizada por um posicionador. O raio-X \u00e9 emitido a uma dist\u00e2ncia padronizada, gerando uma imagem lateral da face. O exame \u00e9 r\u00e1pido e indolor.</p>

<div class="cta-inline">
<h3>Dispon\u00edvel em todas as unidades</h3>
<button onclick="openModal()" class="hbtn-main" style="display:inline-flex;margin:0 auto 12px;text-decoration:none;font-size:14px;padding:12px 28px">Agendar Agora</button>
</div>
</div>'''
    },
    'exames/scanner-intraoral.html': {
        'title': 'Scanner Intraoral 3D | PRO Radiologia',
        'description': 'Scanner intraoral 3D para moldagem digital sem material de impress\u00e3o. Conforto, precis\u00e3o e agilidade para o paciente e dentista.',
        'canonical': 'https://proradiologia.odo.br/exames/scanner-intraoral/',
        'tag': 'Tecnologia',
        'h1': 'Scanner Intraoral 3D',
        'h1_span': 'moldagem digital sem desconforto',
        'content': '''
<div class="article">
<h2>O que \u00e9 o Scanner Intraoral 3D?</h2>
<p>O <strong>Scanner Intraoral 3D</strong> \u00e9 um dispositivo \u00f3ptico que captura imagens tridimensionais detalhadas dos dentes e tecidos moles da boca, eliminando a necessidade de moldagens com materiais de impress\u00e3o tradicionais.</p>

<h2>Vantagens</h2>
<ul>
<li>Maior conforto para o paciente (sem engasgos)</li>
<li>Imagens digitais de alta precis\u00e3o</li>
<li>Resultado imediato</li>
<li>Integra\u00e7\u00e3o com planejamento digital</li>
<li>Armazenamento seguro sem degrada\u00e7\u00e3o</li>
</ul>

<h2>Como \u00e9 realizado?</h2>
<p>O dentista desliza suavemente o scanner sobre os dentes do paciente. O equipamento captura milhares de imagens por segundo, gerando um modelo 3D preciso em tempo real.</p>

<div class="cta-inline">
<h3>Agende seu Scanner Intraoral</h3>
<button onclick="openModal()" class="hbtn-main" style="display:inline-flex;margin:0 auto 12px;text-decoration:none;font-size:14px;padding:12px 28px">Agendar Agora</button>
</div>
</div>'''
    }
}

# UNIT PAGES
UNIT_PAGES = {
    'unidades/presidente-prudente.html': {
        'title': 'Radiologia Odontol\u00f3gica em Presidente Prudente | PRO Radiologia',
        'description': 'PRO Radiologia em Presidente Prudente: exames de radiologia odontol\u00f3gica na Av. Washington Luiz, 874. Tomografia, panor\u00e2mica, documenta\u00e7\u00e3o e mais. Agende!',
        'canonical': 'https://proradiologia.odo.br/unidades/presidente-prudente/',
        'tag': 'Unidade Matriz',
        'h1': 'Centro de Radiologia Odontol\u00f3gica em Presidente Prudente',
        'h1_span': 'unidade matriz',
        'content': '''
<div class="article">
<h2>PRO Radiologia Presidente Prudente</h2>
<p>A unidade matriz da PRO Radiologia em Presidente Prudente est\u00e1 localizada no centro da cidade, com f\u00e1cil acesso e estacionamento pr\u00f3ximo. H\u00e1 mais de 40 anos, oferecemos exames de imagem para dentistas e pacientes da regi\u00e3o.</p>

<div style="display:flex;flex-wrap:wrap;gap:12px;margin-bottom:24px">
<a href="tel:1832229225" class="unit-hero-btn"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>Ligar</a>
<a href="https://wa.me/5518981530505" class="unit-hero-btn" target="_blank"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>WhatsApp</a>
<a href="https://maps.google.com/?q=Av.+Washington+Luiz+874+Presidente+Prudente" class="unit-hero-btn" target="_blank"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>Rota</a>
</div>

<h3>Endere\u00e7o</h3>
<p>Av. Washington Luiz, 874, 7\u00ba andar, Conjunto 71<br>Jardim Paulista, Presidente Prudente - SP<br>CEP: 19015-150</p>

<h3>Hor\u00e1rio de Atendimento</h3>
<p>Segunda a sexta: 8h \u00e0s 18h<br>S\u00e1bado: 8h \u00e0s 12h</p>

<h3>Contato</h3>
<p>Telefone: (18) 3222-9225<br>WhatsApp: (18) 98153-0505<br>E-mail: contato@proradiologia.odo.br</p>

<h3>Exames Dispon\u00edveis</h3>
<ul>
<li><a href="/exames/documentacao-ortodontica/">Documenta\u00e7\u00e3o Ortod\u00f4ntica</a></li>
<li><a href="/exames/radiografia-panoramica/">Radiografia Panor\u00e2mica</a></li>
<li><a href="/exames/radiografia-periapical/">Radiografia Periapical</a></li>
<li><a href="/exames/radiografia-interproximal/">Radiografia Interproximal</a></li>
<li><a href="/exames/tomografia-cone-beam/">Tomografia Cone Beam</a></li>
<li><a href="/exames/telerradiografia/">Telerradiografia</a></li>
<li><a href="/exames/scanner-intraoral/">Scanner Intraoral 3D</a></li>
</ul>

<h3>Como Chegar</h3>
<p>A unidade est\u00e1 localizada na Av. Washington Luiz, uma das principais avenidas de Presidente Prudente, pr\u00f3xima ao cal\u00e7ad\u00e3o e \u00e0 Pra\u00e7a 9 de Julho. O edif\u00edcio conta com elevador e estacionamento nas proximidades.</p>

<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3695.156!2d-51.39166!3d-22.12538!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9494480cdf6291f1%3A0x5f61b81c52d1e4e5!2sAv.%20Washington%20Lu%C3%ADs%2C%20874%20-%20Presidente%20Prudente%2C%20SP!5e0!3m2!1spt-BR!2sbr!4v1" width="100%" height="300" style="border:none;border-radius:16px;margin-top:20px" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa da unidade de Presidente Prudente"></iframe>

<div class="cta-inline">
<h3>Agende seu exame em Presidente Prudente</h3>
<button onclick="openModal()" class="hbtn-main" style="display:inline-flex;margin:0 auto 12px;text-decoration:none;font-size:14px;padding:12px 28px">Agendar Agora</button>
</div>
</div>'''
    },
    'unidades/presidente-epitacio.html': {
        'title': 'Radiologia Odontol\u00f3gica em Presidente Epit\u00e1cio | PRO Radiologia',
        'description': 'PRO Radiologia em Presidente Epit\u00e1cio: exames de radiologia odontol\u00f3gica na Av. Presidente Vargas. Agende sua consulta pelo WhatsApp.',
        'canonical': 'https://proradiologia.odo.br/unidades/presidente-epitacio/',
        'tag': 'Unidade',
        'h1': 'Exames de Radiologia Odontol\u00f3gica em Presidente Epit\u00e1cio',
        'h1_span': 'atendimento completo',
        'content': '''
<div class="article">
<h2>PRO Radiologia Presidente Epit\u00e1cio</h2>
<p>A unidade da PRO Radiologia em Presidente Epit\u00e1cio oferece todos os exames de radiologia odontol\u00f3gica com a mesma qualidade e tecnologia da matriz.</p>

<div style="display:flex;flex-wrap:wrap;gap:12px;margin-bottom:24px">
<a href="tel:1832817455" class="unit-hero-btn"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>Ligar</a>
<a href="https://wa.me/551832817455" class="unit-hero-btn" target="_blank"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>WhatsApp</a>
<a href="https://maps.google.com/?q=Av+Presidente+Vargas+Presidente+Epit%C3%A1cio+SP" class="unit-hero-btn" target="_blank"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>Rota</a>
</div>

<h3>Endere\u00e7o</h3>
<p>Av. Presidente Vargas, 06-29, Centro<br>Presidente Epit\u00e1cio - SP<br>CEP: 19470-000</p>

<h3>Hor\u00e1rio de Atendimento</h3>
<p>Segunda a sexta: 8h \u00e0s 18h<br>S\u00e1bado: 8h \u00e0s 12h</p>

<h3>Contato</h3>
<p>Telefone: (18) 3281-7455<br>WhatsApp: (18) 3281-7455 (PENDING_VERIFICATION)<br>E-mail: contato@proradiologia.odo.br</p>

<h3>Exames Dispon\u00edveis</h3>
<ul>
<li><a href="/exames/documentacao-ortodontica/">Documenta\u00e7\u00e3o Ortod\u00f4ntica</a></li>
<li><a href="/exames/radiografia-panoramica/">Radiografia Panor\u00e2mica</a></li>
<li><a href="/exames/radiografia-periapical/">Radiografia Periapical</a></li>
<li><a href="/exames/radiografia-interproximal/">Radiografia Interproximal</a></li>
<li><a href="/exames/tomografia-cone-beam/">Tomografia Cone Beam</a></li>
<li><a href="/exames/telerradiografia/">Telerradiografia</a></li>
<li><a href="/exames/scanner-intraoral/">Scanner Intraoral 3D</a></li>
</ul>

<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3701.5!2d-52.11053!3d-21.76548!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9490660e3fc3c559%3A0x1234567890abcdef!2sAv.%20Pres.%20Vargas%20-%20Presidente%20Epit%C3%A1cio%2C%20SP!5e0!3m2!1spt-BR!2sbr!4v1" width="100%" height="300" style="border:none;border-radius:16px;margin-top:20px" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa da unidade de Presidente Epit\u00e1cio"></iframe>

<div class="wbox"><p>O WhatsApp desta unidade est\u00e1 pendente de confirma\u00e7\u00e3o. Entre em contato pelo telefone fixo para mais informa\u00e7\u00f5es.</p></div>

<div class="cta-inline">
<h3>Agende seu exame em Presidente Epit\u00e1cio</h3>
<button onclick="openModal()" class="hbtn-main" style="display:inline-flex;margin:0 auto 12px;text-decoration:none;font-size:14px;padding:12px 28px">Agendar Agora</button>
</div>
</div>'''
    },
    'unidades/teodoro-sampaio.html': {
        'title': 'Radiologia Odontol\u00f3gica em Teodoro Sampaio | PRO Radiologia',
        'description': 'PRO Radiologia em Teodoro Sampaio: exames de radiologia odontol\u00f3gica. Agende pelo WhatsApp (18) 98122-3107.',
        'canonical': 'https://proradiologia.odo.br/unidades/teodoro-sampaio/',
        'tag': 'Unidade',
        'h1': 'Radiologia Odontol\u00f3gica em Teodoro Sampaio',
        'h1_span': 'atendimento de qualidade',
        'content': '''
<div class="article">
<h2>PRO Radiologia Teodoro Sampaio</h2>
<p>A unidade da PRO Radiologia em Teodoro Sampaio oferece exames de radiologia odontol\u00f3gica para atender dentistas e pacientes da regi\u00e3o.</p>

<div style="display:flex;flex-wrap:wrap;gap:12px;margin-bottom:24px">
<a href="tel:18981223107" class="unit-hero-btn"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>Ligar</a>
<a href="https://wa.me/5518981223107" class="unit-hero-btn" target="_blank"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>WhatsApp</a>
<a href="https://maps.google.com/?q=Teodoro+Sampaio+SP" class="unit-hero-btn" target="_blank"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>Rota</a>
</div>

<h3>Informa\u00e7\u00f5es</h3>
<div class="wbox"><p>O endere\u00e7o completo desta unidade est\u00e1 pendente de confirma\u00e7\u00e3o. Entre em contato pelo WhatsApp para obter informa\u00e7\u00f5es detalhadas.</p></div>

<h3>Hor\u00e1rio de Atendimento</h3>
<p>Segunda a sexta: 8h \u00e0s 18h<br>S\u00e1bado: 8h \u00e0s 12h</p>

<h3>Contato</h3>
<p>WhatsApp: (18) 98122-3107<br>Telefone: (18) 98122-3107<br>E-mail: contato@proradiologia.odo.br</p>

<h3>Exames Dispon\u00edveis</h3>
<ul>
<li><a href="/exames/documentacao-ortodontica/">Documenta\u00e7\u00e3o Ortod\u00f4ntica</a></li>
<li><a href="/exames/radiografia-panoramica/">Radiografia Panor\u00e2mica</a></li>
<li><a href="/exames/radiografia-periapical/">Radiografia Periapical</a></li>
<li><a href="/exames/radiografia-interproximal/">Radiografia Interproximal</a></li>
<li><a href="/exames/tomografia-cone-beam/">Tomografia Cone Beam</a></li>
<li><a href="/exames/telerradiografia/">Telerradiografia</a></li>
<li><a href="/exames/scanner-intraoral/">Scanner Intraoral 3D</a></li>
</ul>

<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3697.5!2d-52.16970!3d-22.53185!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94906b123456789%3A0xabcdef1234567890!2sTeodoro%20Sampaio%2C%20SP!5e0!3m2!1spt-BR!2sbr!4v1" width="100%" height="300" style="border:none;border-radius:16px;margin-top:20px" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa de Teodoro Sampaio"></iframe>

<div class="cta-inline">
<h3>Agende seu exame em Teodoro Sampaio</h3>
<button onclick="openModal()" class="hbtn-main" style="display:inline-flex;margin:0 auto 12px;text-decoration:none;font-size:14px;padding:12px 28px">Agendar Agora</button>
</div>
</div>'''
    }
}

# INFO PAGES
INFO_PAGES = {
    'sobre.html': {
        'title': 'Sobre a PRO Radiologia | Centro de Radiologia Odontol\u00f3gica',
        'description': 'Conhe\u00e7a a hist\u00f3ria da PRO Radiologia. H\u00e1 mais de 40 anos oferecendo exames de imagem odontol\u00f3gica no Oeste Paulista.',
        'canonical': 'https://proradiologia.odo.br/sobre/',
        'h1': 'Sobre a PRO Radiologia',
        'content': '''
<div class="article">
<p>A <strong>PRO Radiologia</strong> atende dentistas e pacientes com exames de imagem para diagn\u00f3stico odontol\u00f3gico, apoiando o planejamento de tratamentos com qualidade e seguran\u00e7a.</p>

<p>Com tr\u00eas unidades no Oeste Paulista \u2014 Presidente Prudente (matriz), Presidente Epit\u00e1cio e Teodoro Sampaio \u2014, oferecemos uma linha completa de exames, incluindo radiografia panor\u00e2mica, periapical, interproximal, tomografia Cone Beam, telerradiografia e scanner intraoral 3D.</p>

<p>Nossa equipe segue protocolos de qualidade e seguran\u00e7a aplic\u00e1veis aos servi\u00e7os de radiologia odontol\u00f3gica.</p>

<h3>Miss\u00e3o</h3>
<p>Oferecer exames de imagem de qualidade para apoiar dentistas e pacientes no diagn\u00f3stico e planejamento de tratamentos odontol\u00f3gicos.</p>

<h3>Valores</h3>
<ul>
<li>Qualidade t\u00e9cnica</li>
<li>Seguran\u00e7a e biosseguran\u00e7a</li>
<li>Atendimento humanizado</li>
<li>Tecnologia a servi\u00e7o do diagn\u00f3stico</li>
<li>Responsabilidade profissional</li>
</ul>
</div>'''
    },
    'para-dentistas.html': {
        'title': 'Para Dentistas | PRO Radiologia',
        'description': 'Portal para dentistas. Solicite exames, acesse imagens e laudos online. Agilize seu fluxo de trabalho com a PRO Radiologia.',
        'canonical': 'https://proradiologia.odo.br/para-dentistas/',
        'h1': 'Para Dentistas',
        'h1_span': 'solicite exames com agilidade',
        'content': '''
<div class="article">
<h2>PRO Dentista</h2>
<p>Nosso portal exclusivo permite que voc\u00ea solicite exames, acompanhe o hist\u00f3rico dos seus pacientes e acesse as imagens em alta resolu\u00e7\u00e3o de qualquer dispositivo.</p>

<h3>Como solicitar exames</h3>
<ol>
<li>Preencha a requisi\u00e7\u00e3o online com os dados do paciente e tipo de exame</li>
<li>O paciente comparece \u00e0 unidade no hor\u00e1rio agendado</li>
<li>As imagens s\u00e3o disponibilizadas digitalmente ap\u00f3s o exame</li>
<li>Voc\u00ea recebe o link de acesso no e-mail cadastrado</li>
</ol>

<h3>Vantagens</h3>
<ul>
<li>Solicita\u00e7\u00e3o online sem sair do consult\u00f3rio</li>
<li>Acesso digital \u00e0s imagens em formato DICOM</li>
<li>Hist\u00f3rico completo dos pacientes</li>
<li>Agilidade no diagn\u00f3stico</li>
</ul>

<div class="cta-inline">
<h3>Solicitar acesso ao portal</h3>
<p>Entre em contato para solicitar seu cadastro no portal PRO Dentista.</p>
<button onclick="openModal()" class="hbtn-main" style="display:inline-flex;margin:0 auto 12px;text-decoration:none;font-size:14px;padding:12px 28px">Solicitar Acesso</button>
</div>

<a href="/requisicao-de-exames/" class="hbtn-sec" style="display:inline-flex;margin-bottom:20px">Requisi\u00e7\u00e3o de Exames</a>
</div>'''
    },
    'para-pacientes.html': {
        'title': 'Para Pacientes | PRO Radiologia',
        'description': 'Orienta\u00e7\u00f5es para pacientes sobre agendamento, preparo e recebimento de exames de radiologia odontol\u00f3gica.',
        'canonical': 'https://proradiologia.odo.br/para-pacientes/',
        'h1': 'Para Pacientes',
        'h1_span': 'tudo que voc\u00ea precisa saber',
        'content': '''
<div class="article">
<h2>Orienta\u00e7\u00f5es para Pacientes</h2>

<h3>Agendamento</h3>
<p>Para agendar seu exame, entre em contato pelo WhatsApp, telefone ou preencha o formul\u00e1rio em nosso site. Tenha em m\u00e3os a solicita\u00e7\u00e3o do seu dentista.</p>

<h3>Documentos necess\u00e1rios</h3>
<ul>
<li>Documento de identidade com foto</li>
<li>Solicita\u00e7\u00e3o do exame (pedido m\u00e9dico ou odontol\u00f3gico)</li>
<li>Cart\u00e3o do conv\u00eanio (se aplic\u00e1vel)</li>
</ul>

<h3>Preparo</h3>
<p>A maioria dos exames n\u00e3o requer preparo especial. Recomenda-se:</p>
<ul>
<li>Remover brincos, piercings e objetos met\u00e1licos</li>
<li>Informar \u00e0 equipe sobre suspeita de gravidez</li>
<li>Manter a higiene bucal normal</li>
</ul>

<h3>Recebimento das imagens</h3>
<p>As imagens s\u00e3o entregues digitalmente. Seu dentista recebe as imagens em formato DICOM. Voc\u00ea pode solicitar uma c\u00f3pia simples para acompanhamento.</p>

<div class="cta-inline">
<h3>Agende seu exame</h3>
<button onclick="openModal()" class="hbtn-main" style="display:inline-flex;margin:0 auto 12px;text-decoration:none;font-size:14px;padding:12px 28px">Agendar Agora</button>
</div>
</div>'''
    },
    'requisicao-de-exames.html': {
        'title': 'Requisi\u00e7\u00e3o de Exames Online | PRO Radiologia',
        'description': 'Solicite exames de radiologia odontol\u00f3gica online pelo formul\u00e1rio de requisi\u00e7\u00e3o. Agilize o agendamento para seus pacientes.',
        'canonical': 'https://proradiologia.odo.br/requisicao-de-exames/',
        'h1': 'Requisi\u00e7\u00e3o de Exames',
        'h1_span': 'solicite online',
        'content': '''
<div class="article">
<h2>Solicitar Exame</h2>
<p>Preencha o formul\u00e1rio para solicitar um exame. Entraremos em contato para confirmar o agendamento.</p>

<form id="reqForm" style="max-width:600px;margin:24px 0" novalidate>
<div class="mfrow">
<div class="mfg">
<label for="reqNome">Nome do Dentista *</label>
<input type="text" id="reqNome" name="nome" required placeholder="Dr(a). Nome Completo">
<span class="error-msg" role="alert">Campo obrigat\u00f3rio</span>
</div>
<div class="mfg">
<label for="reqCRO">CRO *</label>
<input type="text" id="reqCRO" name="cro" required placeholder="SP-00000">
<span class="error-msg" role="alert">Campo obrigat\u00f3rio</span>
</div>
</div>
<div class="mfrow">
<div class="mfg">
<label for="reqWhats">WhatsApp *</label>
<input type="tel" id="reqWhats" name="whatsapp" required placeholder="(18) 99999-0000">
<span class="error-msg" role="alert">Telefone inv\u00e1lido</span>
</div>
<div class="mfg">
<label for="reqEmail">E-mail</label>
<input type="email" id="reqEmail" name="email" placeholder="email@clinica.com.br">
</div>
</div>
<div class="mfg">
<label for="reqPaciente">Nome do Paciente *</label>
<input type="text" id="reqPaciente" name="paciente" required placeholder="Nome completo do paciente">
<span class="error-msg" role="alert">Campo obrigat\u00f3rio</span>
</div>
<div class="mfrow">
<div class="mfg">
<label for="reqExame">Tipo de Exame *</label>
<select id="reqExame" name="exame" required>
<option value="">Selecione</option>
<option value="documentacao-ortodontica">Documenta\u00e7\u00e3o Ortod\u00f4ntica</option>
<option value="radiografia-panoramica">Radiografia Panor\u00e2mica</option>
<option value="radiografia-periapical">Radiografia Periapical</option>
<option value="radiografia-interproximal">Radiografia Interproximal</option>
<option value="tomografia-cone-beam">Tomografia Cone Beam</option>
<option value="telerradiografia">Telerradiografia</option>
<option value="scanner-intraoral">Scanner Intraoral 3D</option>
</select>
<span class="error-msg" role="alert">Selecione um exame</span>
</div>
<div class="mfg">
<label for="reqUnidade">Unidade *</label>
<select id="reqUnidade" name="unidade" required>
<option value="">Selecione</option>
<option value="presidente-prudente">Presidente Prudente</option>
<option value="presidente-epitacio">Presidente Epit\u00e1cio</option>
<option value="teodoro-sampaio">Teodoro Sampaio</option>
</select>
<span class="error-msg" role="alert">Selecione uma unidade</span>
</div>
</div>
<button class="fsub" type="submit" style="margin-top:8px">Enviar Requisi\u00e7\u00e3o</button>
</form>
<div class="fsuccess" id="reqSucc">
<h4>Requisi\u00e7\u00e3o Enviada!</h4>
<p>Nossa equipe retornar\u00e1 em breve com a confirma\u00e7\u00e3o.</p>
</div>
</div>'''
    },
    'contato.html': {
        'title': 'Contato | PRO Radiologia',
        'description': 'Entre em contato com a PRO Radiologia. WhatsApp, telefone, e-mail e formul\u00e1rio de contato. Atendimento em 3 unidades no Oeste Paulista.',
        'canonical': 'https://proradiologia.odo.br/contato/',
        'h1': 'Fale Conosco',
        'content': '''
<div class="article">
<h2>Canais de Atendimento</h2>

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px;margin-bottom:32px">
<a href="https://wa.me/5518981530505" class="ci" target="_blank">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--bp)" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
<div><strong>WhatsApp</strong><span>(18) 98153-0505</span></div>
</a>
<a href="tel:1832229225" class="ci">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--bp)" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
<div><strong>Telefone</strong><span>(18) 3222-9225</span></div>
</a>
<a href="mailto:contato@proradiologia.odo.br" class="ci">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--bp)" stroke-width="2"><polyline points="22 6 12 13 2 6"/><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/></svg>
<div><strong>E-mail</strong><span>contato@proradiologia.odo.br</span></div>
</a>
</div>

<h3>Unidades</h3>
<ul>
<li><a href="/unidades/presidente-prudente/"><strong>Presidente Prudente (Matriz):</strong></a> Av. Washington Luiz, 874, 7\u00ba andar - (18) 3222-9225</li>
<li><a href="/unidades/presidente-epitacio/"><strong>Presidente Epit\u00e1cio:</strong></a> Av. Presidente Vargas, 06-29 - (18) 3281-7455</li>
<li><a href="/unidades/teodoro-sampaio/"><strong>Teodoro Sampaio:</strong></a> WhatsApp (18) 98122-3107</li>
</ul>

<h3>Hor\u00e1rio de Atendimento</h3>
<p>Segunda a sexta: 8h \u00e0s 18h<br>S\u00e1bado: 8h \u00e0s 12h</p>
</div>'''
    },
    'politica-de-privacidade.html': {
        'title': 'Pol\u00edtica de Privacidade | PRO Radiologia',
        'description': 'Pol\u00edtica de privacidade da PRO Radiologia. Saiba como tratamos seus dados pessoais.',
        'canonical': 'https://proradiologia.odo.br/politica-de-privacidade/',
        'h1': 'Pol\u00edtica de Privacidade',
        'content': '''
<div class="article">
<p><strong>\u00daltima atualiza\u00e7\u00e3o:</strong> Julho de 2026</p>

<p>A PRO Radiologia valoriza a sua privacidade. Esta pol\u00edtica descreve como coletamos, usamos e protegemos as informa\u00e7\u00f5es pessoais dos usu\u00e1rios do nosso site.</p>

<h3>Dados coletados</h3>
<p>Coletamos apenas os dados necess\u00e1rios para o agendamento de exames e contato: nome, telefone, e-mail e unidade de interesse. Dados sens\u00edveis (como informa\u00e7\u00f5es de sa\u00fade) n\u00e3o s\u00e3o coletados por este site.</p>

<h3>Uso dos dados</h3>
<p>Os dados fornecidos s\u00e3o utilizados exclusivamente para:</p>
<ul>
<li>Agendamento de exames</li>
<li>Comunica\u00e7\u00e3o sobre os servi\u00e7os solicitados</li>
<li>Melhoria dos nossos servi\u00e7os</li>
</ul>

<h3>Compartilhamento</h3>
<p>N\u00e3o compartilhamos dados pessoais com terceiros, exceto quando exigido por lei.</p>

<h3>Cookies</h3>
<p>Utilizamos cookies para an\u00e1lise de tr\u00e1fego do site. N\u00e3o utilizamos cookies de rastreamento comportamental.</p>

<h3>Seus direitos</h3>
<p>Voc\u00ea pode solicitar a exclus\u00e3o ou corre\u00e7\u00e3o dos seus dados a qualquer momento entrando em contato pelo e-mail contato@proradiologia.odo.br.</p>
</div>'''
    },
    'termos-de-uso.html': {
        'title': 'Termos de Uso | PRO Radiologia',
        'description': 'Termos de uso do site da PRO Radiologia.',
        'canonical': 'https://proradiologia.odo.br/termos-de-uso/',
        'h1': 'Termos de Uso',
        'content': '''
<div class="article">
<p><strong>\u00daltima atualiza\u00e7\u00e3o:</strong> Julho de 2026</p>

<h3>Informa\u00e7\u00f5es Gerais</h3>
<p>O site da PRO Radiologia tem car\u00e1ter informativo e educativo. As informa\u00e7\u00f5es sobre exames e procedimentos n\u00e3o substituem a consulta com um profissional de sa\u00fade habilitado.</p>

<h3>Uso do Site</h3>
<p>Ao utilizar este site, voc\u00ea concorda com os termos aqui descritos. O conte\u00fado do site n\u00e3o pode ser reproduzido sem autoriza\u00e7\u00e3o.</p>

<h3>Responsabilidade</h3>
<p>A PRO Radiologia n\u00e3o se responsabiliza por decis\u00f5es baseadas exclusivamente nas informa\u00e7\u00f5es deste site. Consulte sempre um profissional de sa\u00fade para orienta\u00e7\u00e3o personalizada.</p>

<h3>Contato</h3>
<p>D\u00favidas sobre os termos podem ser enviadas para contato@proradiologia.odo.br.</p>
</div>'''
    },
    'blog/index.html': {
        'title': 'Blog | PRO Radiologia Odontol\u00f3gica',
        'description': 'Artigos sobre radiologia odontol\u00f3gica, tomografia Cone Beam, documenta\u00e7\u00e3o ortod\u00f4ntica e seguran\u00e7a dos exames de imagem.',
        'canonical': 'https://proradiologia.odo.br/blog/',
        'no_ph_section': True,
        'content': '''
<section class="ph">
<div class="ph-inner">
<div class="breadcrumb"><span>Blog</span></div>
<div class="ph-layout" style="grid-template-columns:1fr">
<div>
<div class="ptag">Conte\u00fados</div>
<h1 class="ptitle">Blog da <span>PRO Radiologia</span></h1>
<p class="plead">Artigos educativos sobre radiologia odontol\u00f3gica, exames de imagem e sa\u00fade bucal.</p>
</div>
</div>
</div>
</section>
<div style="max-width:1200px;margin:0 auto;padding:60px 5%">
<div class="blog-listing-grid">
<a href="/blog/tomografia-cone-beam/" class="blog-card">
<div class="blog-card-img" style="background:linear-gradient(135deg,#E8F4FD,#B3DAFA)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="60" height="60"><line x1="12" y1="2" x2="12" y2="6"/><line x1="12" y1="18" x2="12" y2="22"/><line x1="4.93" y1="4.93" x2="7.76" y2="7.76"/><line x1="16.24" y1="16.24" x2="19.07" y2="19.07"/><line x1="2" y1="12" x2="6" y2="12"/><line x1="18" y1="12" x2="22" y2="12"/><line x1="4.93" y1="19.07" x2="7.76" y2="16.24"/><line x1="16.24" y1="7.76" x2="19.07" y2="4.93"/></svg></div>
<div class="blog-card-body">
<div class="blog-card-tag">Tecnologia</div>
<div class="blog-card-title">O que \u00e9 Tomografia Cone Beam e quando ela pode ser solicitada?</div>
<div class="blog-card-excerpt">Guia completo sobre o exame 3D mais importante da odontologia moderna: indica\u00e7\u00f5es, diferen\u00e7as da TC m\u00e9dica e protocolo de seguran\u00e7a.</div>
<div class="bmeta"><span>5 min de leitura</span><span class="brm">Ler artigo &rarr;</span></div>
</div>
</a>
<a href="/blog/radiografia-odontologica-faz-mal/" class="blog-card">
<div class="blog-card-img" style="background:linear-gradient(135deg,#D6EDFA,#1A8FE3)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="60" height="60"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
<div class="blog-card-body">
<div class="blog-card-tag">Seguran\u00e7a</div>
<div class="blog-card-title">Radiografia odontol\u00f3gica faz mal? Entenda seguran\u00e7a e prote\u00e7\u00e3o radiol\u00f3gica</div>
<div class="blog-card-excerpt">Esclarecemos os principais mitos sobre a radia\u00e7\u00e3o em exames odontol\u00f3gicos com informa\u00e7\u00f5es baseadas em protocolos de seguran\u00e7a.</div>
<div class="bmeta"><span>6 min de leitura</span><span class="brm">Ler artigo &rarr;</span></div>
</div>
</a>
<a href="/blog/documentacao-ortodontica/" class="blog-card">
<div class="blog-card-img" style="background:linear-gradient(135deg,#083D6B,#0D5FA3)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" width="60" height="60"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg></div>
<div class="blog-card-body">
<div class="blog-card-tag">Ortodontia</div>
<div class="blog-card-title">Documenta\u00e7\u00e3o ortod\u00f4ntica completa: quais exames podem fazer parte?</div>
<div class="blog-card-excerpt">Entenda quais exames comp\u00f5em uma documenta\u00e7\u00e3o ortod\u00f4ntica e a import\u00e2ncia de cada um para o planejamento do tratamento.</div>
<div class="bmeta"><span>4 min de leitura</span><span class="brm">Ler artigo &rarr;</span></div>
</div>
</a>
</div>
</div>'''
    }
}

def generate_pages():
    """Generate all content pages."""
    for path, data in EXAM_PAGES.items():
        bc = make_breadcrumb([('Home', '/'), ('Exames', '/exames/'), (data['title'].split('|')[0].strip(), '')])
        h1_html = make_ptag(data['tag']) + make_ptitle(data['h1'], data.get('h1_span', ''))
        html = make_page(
            title=data['title'],
            description=data['description'],
            canonical=data['canonical'],
            breadcrumb=bc,
            h1=h1_html,
            content=data['content']
        )
        write_file(path, html)

    for path, data in UNIT_PAGES.items():
        items = [('Home', '/'), ('Unidades', '/unidades/'), (data['h1'].split('em')[0].strip() if 'em' in data['h1'] else data['h1'], '')]
        bc = make_breadcrumb(items)
        h1_html = make_ptag(data['tag']) + make_ptitle(data['h1'], data.get('h1_span', ''))
        html = make_page(
            title=data['title'],
            description=data['description'],
            canonical=data['canonical'],
            breadcrumb=bc,
            h1=h1_html,
            content=data['content']
        )
        write_file(path, html)

    for path, data in INFO_PAGES.items():
        items = [('Home', '/'), (data['title'].split('|')[0].strip(), '')]
        bc = make_breadcrumb(items)
        h1_html = make_ptitle(data['h1']) if not data.get('no_ph_section') else ''
        html = make_page(
            title=data['title'],
            description=data['description'],
            canonical=data.get('canonical', 'https://proradiologia.odo.br/' + path.replace('.html', '/')),
            breadcrumb=bc,
            h1=h1_html,
            content=data['content']
        )
        write_file(path, html)


def generate_404():
    """Generate 404 page."""
    html = make_page(
        title='P\u00e1gina n\u00e3o encontrada | PRO Radiologia',
        description='P\u00e1gina n\u00e3o encontrada.',
        canonical='https://proradiologia.odo.br/404/',
        noindex=True,
        breadcrumb='',
        content='''
<section class="page-404">
<div class="num404" aria-hidden="true">404</div>
<h1>P\u00e1gina n\u00e3o encontrada</h1>
<p>A p\u00e1gina que voc\u00ea procura n\u00e3o existe ou foi movida.</p>
<a href="/" class="hbtn-main" style="display:inline-flex;text-decoration:none">Voltar para a p\u00e1gina inicial</a>
</section>'''
    )
    write_file('404.html', html)


def generate_exames_listing():
    """Generate the /exames/ listing page."""
    items = [('Home', '/'), ('Exames', '')]
    bc = make_breadcrumb(items)
    exam_links = ''
    for slug, info in [
        ('documentacao-ortodontica', 'Documenta\u00e7\u00e3o Ortod\u00f4ntica'),
        ('radiografia-panoramica', 'Radiografia Panor\u00e2mica'),
        ('radiografia-periapical', 'Radiografia Periapical'),
        ('radiografia-interproximal', 'Radiografia Interproximal'),
        ('tomografia-cone-beam', 'Tomografia Cone Beam'),
        ('telerradiografia', 'Telerradiografia'),
        ('scanner-intraoral', 'Scanner Intraoral 3D')
    ]:
        exam_links += f'<li><a href="/exames/{slug}/">{info}</a></li>\n'
    content = f'''
<div class="article">
<h2>Nossos Exames</h2>
<p>Confira a linha completa de exames de radiologia odontol\u00f3gica dispon\u00edveis na PRO Radiologia.</p>
<ul>{exam_links}</ul>
</div>'''
    html = make_page(
        title='Exames de Radiologia Odontol\u00f3gica | PRO Radiologia',
        description='Confira todos os exames de radiologia odontol\u00f3gica dispon\u00edveis na PRO Radiologia: panor\u00e2mica, tomografia, documenta\u00e7\u00e3o e mais.',
        canonical='https://proradiologia.odo.br/exames/',
        breadcrumb=bc,
        h1='<h1 class="ptitle">Exames de <span>radiologia odontol\u00f3gica</span></h1>',
        content=content
    )
    write_file('exames/index.html', html)


def generate_units_listing():
    """Generate the /unidades/ listing page."""
    items = [('Home', '/'), ('Unidades', '')]
    bc = make_breadcrumb(items)
    content = '''
<div class="article">
<h2>Nossas Unidades</h2>
<p>A PRO Radiologia conta com 3 unidades no Oeste Paulista para melhor atender voc\u00ea.</p>
<ul>
<li><a href="/unidades/presidente-prudente/"><strong>Presidente Prudente (Matriz):</strong></a> Av. Washington Luiz, 874 - (18) 3222-9225</li>
<li><a href="/unidades/presidente-epitacio/"><strong>Presidente Epit\u00e1cio:</strong></a> Av. Presidente Vargas, 06-29 - (18) 3281-7455</li>
<li><a href="/unidades/teodoro-sampaio/"><strong>Teodoro Sampaio:</strong></a> WhatsApp (18) 98122-3107</li>
</ul>
</div>'''
    html = make_page(
        title='Unidades | PRO Radiologia Odontol\u00f3gica',
        description='Conhe\u00e7a as 3 unidades da PRO Radiologia: Presidente Prudente (matriz), Presidente Epit\u00e1cio e Teodoro Sampaio.',
        canonical='https://proradiologia.odo.br/unidades/',
        breadcrumb=bc,
        h1='<h1 class="ptitle">Nossas <span>unidades</span></h1>',
        content=content
    )
    write_file('unidades/index.html', html)


if __name__ == '__main__':
    os.chdir(BASE_DIR)
    generate_pages()
    generate_404()
    generate_exames_listing()
    generate_units_listing()
    print('All pages generated successfully!')
