;(function () {
  var SITE_URL = 'https://proradiologia.odo.br'

  var UNITS = {
    presidentePrudente: {
      name: 'Presidente Prudente',
      type: 'Matriz',
      slug: 'presidente-prudente',
      address: 'Av. Washington Luiz, 874, 7\u00ba andar, Conjunto 71, Jardim Paulista, Presidente Prudente - SP',
      postalCode: '19015-150',
      phone: '+55 18 3222-9225',
      phoneDisplay: '(18) 3222-9225',
      whatsapp: '+55 18 98153-0505',
      whatsappDisplay: '(18) 98153-0505',
      email: 'contato@proradiologia.odo.br',
      mapQuery: 'Av.+Washington+Luiz+874+Presidente+Prudente',
      mapEmbed: 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3695.156!2d-51.39166!3d-22.12538!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9494480cdf6291f1%3A0x5f61b81c52d1e4e5!2sAv.%20Washington%20Lu%C3%ADs%2C%20874%20-%20Presidente%20Prudente%2C%20SP!5e0!3m2!1spt-BR!2sbr!4v1',
      openingHours: { weekdays: '08:00\u201318:00', saturday: '08:00\u201312:00', sunday: null },
      exams: ['documentacao-ortodontica', 'radiografia-panoramica', 'radiografia-periapical', 'radiografia-interproximal', 'tomografia-cone-beam', 'telerradiografia', 'scanner-intraoral'],
      neighborhoods: ['Jardim Paulista', 'Vila Maristela', 'Centro', 'Jardim Bongiovani', 'Parque Furquim']
    },
    presidenteEpitacio: {
      name: 'Presidente Epit\u00e1cio',
      type: 'Unidade',
      slug: 'presidente-epitacio',
      address: 'Av. Presidente Vargas, 06-29, Centro, Presidente Epit\u00e1cio - SP',
      postalCode: '19470-000',
      phone: '+55 18 3281-7455',
      phoneDisplay: '(18) 3281-7455',
      whatsapp: 'PENDING_VERIFICATION',
      whatsappDisplay: '(18) 3281-7455',
      email: 'contato@proradiologia.odo.br',
      mapQuery: 'Av+Presidente+Vargas+Presidente+Epit%C3%A1cio+SP',
      mapEmbed: 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3701.5!2d-52.11053!3d-21.76548!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9490660e3fc3c559%3A0x1234567890abcdef!2sAv.%20Pres.%20Vargas%20-%20Presidente%20Epit%C3%A1cio%2C%20SP!5e0!3m2!1spt-BR!2sbr!4v1',
      openingHours: { weekdays: '08:00\u201318:00', saturday: '08:00\u201312:00', sunday: null },
      exams: ['documentacao-ortodontica', 'radiografia-panoramica', 'radiografia-periapical', 'radiografia-interproximal', 'tomografia-cone-beam', 'telerradiografia', 'scanner-intraoral'],
      neighborhoods: ['Centro', 'Vila Nova', 'Jardim Europa']
    },
    teodoroSampaio: {
      name: 'Teodoro Sampaio',
      type: 'Unidade',
      slug: 'teodoro-sampaio',
      address: 'PENDING_VERIFICATION',
      postalCode: 'PENDING_VERIFICATION',
      phone: '+55 18 98122-3107',
      phoneDisplay: '(18) 98122-3107',
      whatsapp: '+55 18 98122-3107',
      whatsappDisplay: '(18) 98122-3107',
      email: 'contato@proradiologia.odo.br',
      mapQuery: 'Teodoro+Sampaio+SP',
      mapEmbed: 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3697.5!2d-52.16970!3d-22.53185!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94906b123456789%3A0xabcdef1234567890!2sTeodoro%20Sampaio%2C%20SP!5e0!3m2!1spt-BR!2sbr!4v1',
      openingHours: { weekdays: '08:00\u201318:00', saturday: '08:00\u201312:00', sunday: null },
      exams: ['documentacao-ortodontica', 'radiografia-panoramica', 'radiografia-periapical', 'radiografia-interproximal', 'tomografia-cone-beam', 'telerradiografia', 'scanner-intraoral'],
      neighborhoods: ['Centro']
    }
  }

  var EXAMS = {
    'documentacao-ortodontica': {
      name: 'Documenta\u00e7\u00e3o Ortod\u00f4ntica',
      shortName: 'Documenta\u00e7\u00e3o Ortod\u00f4ntica',
      slug: 'documentacao-ortodontica',
      icon: 'documentation',
      description: 'Conjunto completo de exames para planejamento ortod\u00f4ntico, incluindo radiografia panor\u00e2mica, telerradiografia e fotografias intra e extraorais.',
      summary: 'Conjunto completo para planejamento ortod\u00f4ntico'
    },
    'radiografia-panoramica': {
      name: 'Radiografia Panor\u00e2mica',
      shortName: 'Panor\u00e2mica',
      slug: 'radiografia-panoramica',
      icon: 'panoramic',
      description: 'Imagem completa de toda a arcada dent\u00e1ria em \u00fanica tomada. Ideal para avalia\u00e7\u00e3o geral, dentes do siso, implantes e ortopedia facial.',
      summary: 'Imagem completa da arcada dent\u00e1ria'
    },
    'radiografia-periapical': {
      name: 'Radiografia Periapical',
      shortName: 'Periapical',
      slug: 'radiografia-periapical',
      icon: 'periapical',
      description: 'S\u00e9rie de radiografias individuais para avalia\u00e7\u00e3o detalhada de cada dente, ra\u00edzes e osso alveolar. Essencial em endodontia.',
      summary: 'Avalia\u00e7\u00e3o detalhada dente a dente'
    },
    'radiografia-interproximal': {
      name: 'Radiografia Interproximal (Bite-wing)',
      shortName: 'Interproximal',
      slug: 'radiografia-interproximal',
      icon: 'interproximal',
      description: 'Detecta c\u00e1ries entre os dentes e avalia a crista \u00f3ssea alveolar. Ideal para check-ups preventivos peri\u00f3dicos.',
      summary: 'Detec\u00e7\u00e3o de c\u00e1ries interproximais'
    },
    'tomografia-cone-beam': {
      name: 'Tomografia Cone Beam (CBCT)',
      shortName: 'Tomografia 3D',
      slug: 'tomografia-cone-beam',
      icon: 'ctscan',
      description: 'Imagem tridimensional de alta resolu\u00e7\u00e3o para implantes, cirurgias e diagn\u00f3sticos complexos. Tecnologia 3D de \u00faltima gera\u00e7\u00e3o.',
      summary: 'Imagem 3D de alta resolu\u00e7\u00e3o'
    },
    'telerradiografia': {
      name: 'Telerradiografia',
      shortName: 'Telerradiografia',
      slug: 'telerradiografia',
      icon: 'xray',
      description: 'Radiografia lateral da face para an\u00e1lise cefalom\u00e9trica. Essencial para planejamento ortod\u00f4ntico e cirurgia ortogn\u00e1tica.',
      summary: 'An\u00e1lise cefalom\u00e9trica facial'
    },
    'scanner-intraoral': {
      name: 'Scanner Intraoral 3D',
      shortName: 'Scanner Intraoral',
      slug: 'scanner-intraoral',
      icon: 'scanner',
      description: 'Moldagem digital sem material de impress\u00e3o. Escaneamento \u00f3ptico intraoral de alta precis\u00e3o para m\u00e1ximo conforto.',
      summary: 'Moldagem digital sem desconforto'
    }
  }

  var UNITS_ARRAY = [UNITS.presidentePrudente, UNITS.presidenteEpitacio, UNITS.teodoroSampaio]
  var EXAMS_ARRAY = Object.keys(EXAMS).map(function (k) { return EXAMS[k] })

  window.PRO_DATA = {
    SITE_URL: SITE_URL,
    UNITS: UNITS,
    UNITS_ARRAY: UNITS_ARRAY,
    EXAMS: EXAMS,
    EXAMS_ARRAY: EXAMS_ARRAY,
    getExamUrl: function (slug) { return '/exames/' + slug + '/' },
    getUnitUrl: function (slug) { return '/unidades/' + slug + '/' },
    getUnitBySlug: function (slug) { return UNITS[slug] || UNITS.presidentePrudente },
    getExamBySlug: function (slug) { return EXAMS[slug] },
    getWhatsappLink: function (unitSlug, msg) {
      var unit = UNITS[unitSlug] || UNITS.presidentePrudente
      var number = unit.whatsapp.startsWith('PENDING') ? '5518981530505' : unit.whatsapp.replace(/[^0-9]/g, '')
      var text = msg || 'Ol\u00e1, encontrei a PRO Radiologia pelo site e gostaria de informa\u00e7\u00f5es sobre agendamento na unidade de ' + unit.name + '.'
      return 'https://wa.me/' + number + '?text=' + encodeURIComponent(text)
    },
    getPhoneLink: function (unitSlug) {
      var unit = UNITS[unitSlug] || UNITS.presidentePrudente
      return 'tel:' + unit.phone.replace(/[^0-9+]/g, '')
    },
    formatPhone: function (value) {
      var cleaned = value.replace(/\D/g, '')
      if (cleaned.length <= 2) return cleaned
      if (cleaned.length <= 6) return '(' + cleaned.slice(0, 2) + ') ' + cleaned.slice(2)
      if (cleaned.length <= 10) return '(' + cleaned.slice(0, 2) + ') ' + cleaned.slice(2, 6) + '-' + cleaned.slice(6)
      return '(' + cleaned.slice(0, 2) + ') ' + cleaned.slice(2, 7) + '-' + cleaned.slice(7, 11)
    }
  }
})()
