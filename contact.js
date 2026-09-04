(function () {
  'use strict';

  const menuToggle = document.querySelector('.menu-toggle');
  const mobileMenu = document.getElementById('mobileMenu');
  const form = document.getElementById('enquiryForm');
  const nameField = document.getElementById('name');
  const emailField = document.getElementById('email');
  const phoneField = document.getElementById('phone');
  const topicField = document.getElementById('topic');
  const messageField = document.getElementById('message');

  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener('click', function () {
      const open = mobileMenu.classList.toggle('open');
      menuToggle.setAttribute('aria-expanded', String(open));
      menuToggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
    });

    mobileMenu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        mobileMenu.classList.remove('open');
        menuToggle.setAttribute('aria-expanded', 'false');
        menuToggle.setAttribute('aria-label', 'Open navigation');
      });
    });
  }

  if (!form || !nameField || !emailField || !phoneField || !topicField || !messageField) return;

  const allowedTopics = new Set([
    'Psychological support',
    'Psychological assessment',
    'Support for a young person',
    'Adult support',
    'Workplace wellbeing',
    'General enquiry'
  ]);

  function clean(value, maxLength) {
    return value.replace(/\r\n?/g, '\n').trim().slice(0, maxLength);
  }

  form.addEventListener('submit', function (event) {
    event.preventDefault();

    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    const name = clean(nameField.value, 100);
    const email = clean(emailField.value, 254);
    const phone = clean(phoneField.value, 40) || 'Not provided';
    const topic = topicField.value;
    const message = clean(messageField.value, 2500);

    if (!name || name.length > 100 || !email || email.length > 254 || !message || message.length > 2500 || !allowedTopics.has(topic)) {
      form.reportValidity();
      return;
    }

    const text = [
      'New website enquiry',
      '',
      'Name: ' + name,
      'Email: ' + email,
      'Contact number: ' + phone,
      'Enquiry type: ' + topic,
      '',
      'Message:',
      message
    ].join('\n');

    const whatsappUrl = 'https://wa.me/353876044744?text=' + encodeURIComponent(text);
    window.open(whatsappUrl, '_blank', 'noopener,noreferrer');
  });
})();
