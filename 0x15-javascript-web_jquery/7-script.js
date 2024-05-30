$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (response) => {
  $('DIV#character').text(response.name);
}, 'json');
