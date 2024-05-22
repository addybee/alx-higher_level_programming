#!/usr/bin/node

const ID = process.argv[2];
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${ID}`;

/**
 * Wraps the request library in a promise for asynchronous HTTP requests handling JSON responses.
 * @param {string} url - The URL to which the HTTP request is sent.
 * @returns {Promise} A promise that resolves with the parsed JSON data or rejects with an error.
 */
function requestPromise (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

/**
 * Asynchronously fetches film data from a given URL and returns the characters associated with that film.
 * @param {string} url - The URL from which to fetch the film data.
 * @returns {Promise<Array<string>>} - An array of URLs, each representing a character in the film.
 */
async function getFilm (url) {
  try {
    const filmData = await requestPromise(url);
    return filmData.characters;
  } catch (error) {
    console.error('Error fetching film:', error.message);
  }
}

/**
 * Asynchronously fetches and logs the names of characters from a specified Star Wars film URL.
 * @param {string} url - The URL of the Star Wars film resource.
 */
async function getFilmCharacters (url) {
  try {
    const characters = await getFilm(url);
    for (const characterUrl of characters) {
      try {
        const characterData = await requestPromise(characterUrl);
        console.log(characterData.name);
      } catch (error) {
        console.error('Error fetching character:', error.message);
      }
    }
  } catch (error) {
    console.error('Error fetching characters:', error.message);
  }
}

getFilmCharacters(url);
