#!/usr/bin/node
const request = require('request');

const getStarWarsFilms = () =>
  new Promise((resolve, reject) => {
    request('https://swapi-api.alx-tools.com/api/films', (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const { results } = JSON.parse(body);
        resolve(results);
      }
    });
  });

const getCharactersByFilm = (film) =>
  new Promise((resolve, reject) => {
    const characterPromises = film.characters.map(url =>
      new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            const { name } = JSON.parse(body);
            resolve(name);
          }
        });
      })
    );

    Promise.all(characterPromises)
      .then(characters => resolve({ film: film.title, characters }))
      .catch(reject);
  });

const filmId = process.argv[2];

if (!filmId) {
  console.log('Please provide a film ID as a command-line argument.');
  process.exit(1);
}

getStarWarsFilms()
  .then(films => {
    const film = films.find(film => film.episode_id === Number(filmId));
    if (!film) {
      throw new Error(`Film with ID ${filmId} not found.`);
    }
    return getCharactersByFilm(film);
  })
  .then(({ characters }) => {
    console.log(characters.join('\n'));
  })
  .catch(error => {
    console.error('Error:', error);
  });
