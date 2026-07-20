;(function () {
  'use strict'

  var d = document
  var w = window

  function init () {
    initNav()
    initReveal()
    initFAQ()
    initModal()
    initUnitSelector()
    initPhoneMask()
    initYear()
    initScroll()
  }

  /* NAVIGATION */
  function initNav () {
    var nav = d.getElementById('nav')
    var toggle = d.querySelector('.nav-toggle')
    var links = d.querySelector('.nav-links')

    if (toggle && links) {
      toggle.addEventListener('click', function () {
        toggle.classList.toggle('open')
        links.classList.toggle('mobile-open')
        var expanded = toggle.getAttribute('aria-expanded') === 'true' ? 'false' : 'true'
        toggle.setAttribute('aria-expanded', expanded)
      })

      links.querySelectorAll('a').forEach(function (a) {
        a.addEventListener('click', function () {
          toggle.classList.remove('open')
          links.classList.remove('mobile-open')
          toggle.setAttribute('aria-expanded', 'false')
        })
      })
    }

    if (nav) {
      w.addEventListener('scroll', function () {
        if (w.scrollY > 50) { nav.classList.add('scrolled') }
        else { nav.classList.remove('scrolled') }
      }, { passive: true })
    }
  }

  /* SCROLL REVEAL */
  function initReveal () {
    var els = d.querySelectorAll('.reveal')
    if (!els.length || !('IntersectionObserver' in w)) {
      els.forEach(function (el) { el.classList.add('visible') })
      return
    }
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible')
          obs.unobserve(entry.target)
        }
      })
    }, { threshold: 0.1 })
    els.forEach(function (el) { obs.observe(el) })
  }

  /* FAQ */
  function initFAQ () {
    d.querySelectorAll('.faq-item, .ifaq-item').forEach(function (item) {
      var trigger = item.querySelector('.fq, .ifq')
      if (!trigger) return
      trigger.addEventListener('click', function () {
        item.classList.toggle('open')
      })
      trigger.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault()
          item.classList.toggle('open')
        }
      })
    })
  }

  /* MODAL */
  var modalOpen = false
  var prevFocus = null

  function initModal () {
    var overlay = d.querySelector('.movl')
    if (!overlay) return
    var closeBtn = overlay.querySelector('.mcl')
    var modal = overlay.querySelector('.modal')

    w.openModal = function () {
      prevFocus = d.activeElement
      overlay.classList.add('open')
      modalOpen = true
      d.body.style.overflow = 'hidden'
      if (closeBtn) closeBtn.focus()
      sendEvent('open_booking_form', { cta_position: 'modal' })
    }

    w.closeModal = function () {
      overlay.classList.remove('open')
      modalOpen = false
      d.body.style.overflow = ''
      if (prevFocus) prevFocus.focus()
    }

    if (closeBtn) {
      closeBtn.addEventListener('click', w.closeModal)
    }

    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) w.closeModal()
    })

    d.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && modalOpen) w.closeModal()
    })

    /* Modal form handling */
    var form = overlay.querySelector('form')
    if (form) {
      var submitBtn = form.querySelector('.msub')
      var successEl = overlay.querySelector('.msucc')

      form.addEventListener('submit', function (e) {
        e.preventDefault()
        if (submitBtn) { submitBtn.disabled = true; submitBtn.textContent = 'Enviando...' }

        var data = {}
        var inputs = form.querySelectorAll('input, select, textarea')
        inputs.forEach(function (inp) {
          if (inp.name) data[inp.name] = inp.value
        })
        data.type = 'agendamento'

        var action = form.getAttribute('action') || '/api/submit'

        fetch(action, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data)
        }).then(function (r) {
          if (!r.ok) throw new Error('Network error')
          return r.json()
        }).then(function () {
          if (successEl) successEl.style.display = 'block'
          if (form) form.style.display = 'none'
          sendEvent('submit_booking_success', {})
        }).catch(function () {
          if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = 'Tentar novamente' }
          sendEvent('submit_booking_error', {})
          alert('Ocorreu um erro ao enviar. Tente novamente ou entre em contato pelo WhatsApp.')
        })
      })
    }
  }

  /* UNIT SELECTOR */
  function initUnitSelector () {
    var btns = d.querySelectorAll('.unit-btn')
    if (!btns.length) return
    btns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        btns.forEach(function (b) { b.classList.remove('active') })
        btn.classList.add('active')
        var slug = btn.getAttribute('data-unit')
        if (slug) {
          var data = w.PRO_DATA
          if (!data) return
          var unit = data.getUnitBySlug(slug)
          sendEvent('select_unit', { unit_slug: slug })
          updateWhatsAppFloating(unit)
        }
      })
    })
  }

  function updateWhatsAppFloating (unit) {
    var waBtn = d.querySelector('.waf')
    if (!waBtn || !unit) return
    var num = unit.whatsapp.startsWith('PENDING') ? '5518981530505' : unit.whatsapp.replace(/[^0-9]/g, '')
    waBtn.href = 'https://wa.me/' + num + '?text=' + encodeURIComponent('Ol\u00e1, encontrei a PRO Radiologia pelo site e gostaria de informa\u00e7\u00f5es sobre agendamento na unidade de ' + unit.name + '.')
  }

  /* PHONE MASK */
  function initPhoneMask () {
    d.querySelectorAll('input[type="tel"]').forEach(function (inp) {
      inp.addEventListener('input', function () {
        var cleaned = this.value.replace(/\D/g, '')
        if (cleaned.length <= 2) { this.value = cleaned }
        else if (cleaned.length <= 6) { this.value = '(' + cleaned.slice(0, 2) + ') ' + cleaned.slice(2) }
        else if (cleaned.length <= 10) { this.value = '(' + cleaned.slice(0, 2) + ') ' + cleaned.slice(2, 6) + '-' + cleaned.slice(6) }
        else { this.value = '(' + cleaned.slice(0, 2) + ') ' + cleaned.slice(2, 7) + '-' + cleaned.slice(7, 11) }
      })
    })
  }

  /* YEAR */
  function initYear () {
    var els = d.querySelectorAll('.current-year')
    els.forEach(function (el) { el.textContent = new Date().getFullYear() })
  }

  /* SCROLL */
  function initScroll () {
    d.querySelectorAll('a[href^="#"]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        var href = this.getAttribute('href')
        if (href === '#') return
        var target = d.querySelector(href)
        if (target) {
          e.preventDefault()
          var offset = 80
          var pos = target.getBoundingClientRect().top + w.scrollY - offset
          w.scrollTo({ top: pos, behavior: 'smooth' })
        }
      })
    })
  }

  /* ANALYTICS EVENT */
  function sendEvent (action, params) {
    if (w.gtag && typeof w.gtag === 'function') {
      w.gtag('event', action, params)
    }
  }

  w.sendAnalyticsEvent = sendEvent

  if (d.readyState === 'loading') { d.addEventListener('DOMContentLoaded', init) }
  else { init()
 }
})()
