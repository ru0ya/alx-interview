#!/usr/bin/node

const axios = require('axios');

const filmId = process.argv[2];

if (!filmId) {
  console.log('Please provide a film ID as a command-line argument.');
  process.exit(1);
}

axios.get(`https://swapi-api.alx-tools.com/api/films/${filmId}`)
  .then(response => {
    const film = response.data;
    const characterUrls = film.characters;
    const characterPromises = characterUrls.map(url => {
      return axios.get(url)
        .then(response => response.data.name)
        .catch(error => {
          throw new Error(`Error fetching character data: ${error.message}`);
        });
    });

    return Promise.all(characterPromises);
  })
  .then(characters => {
    console.log(characters.join('\n'));
  })
  .catch(error => {
    console.error('Error:', error.message);
  });
