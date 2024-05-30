$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (response) => {
  response.results.forEach(film => {
    $('UL#list_movies').append('<li>' + film.title + '</li>');
  });
}, 'json');
