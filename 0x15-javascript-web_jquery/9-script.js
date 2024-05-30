$(document).ready(() => {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (response) => {
    $('DIV#hello').text(response.hello);
  }, 'json');
});
