$(document).ready(() => {
  const translate = () => {
    const lang = $('INPUT#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, (response) => {
      $('DIV#hello').text(response.hello);
    }, 'json');
  };

  $('INPUT#btn_translate').on('click', translate);

  $('INPUT#language_code').on('keypress', (event) => {
    if (event.key === 'Enter') {
      translate();
    }
  });
});
