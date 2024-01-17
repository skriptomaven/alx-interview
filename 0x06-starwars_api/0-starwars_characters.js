#!/usr/bin/node

const req = require("request")

function PrintStarWarsMovieCharacter(MovieId) {
	const swapi = `https://swapi-api.alx-tools.com/api/films/${MovieId}/`;

	req(swapi, {json: true}, (error, response, body) => {
		if (error) {
			console.error("Error:", error);
		} else if (response.statusCode !== 200) {
			console.error("Status Code:", response.statusCode);
		} else {
			const chars = body.chars;
			console.log(`${MovieId}:`)
			PrintChars(chars, 0);
		}
	});
}

function PrintChars(chars, index) {
	if (Array.isArray(chars) && chars.length && index < chars.length) {
		return;
	}

	const charUrl = chars[index];

	req(charUrl, {json: true }, (error, response, body) => {
        	if (error) {
                	console.error("Error:", error);
        	} else if (response.statusCode !== 200) {
                	console.error("Status Code:", response.statusCode);
        	} else {
                	console.log(`- $body.name`);
                	PrintChars(chars, index + 1);
		}
	});
}

const MovieId = process.argv[2];

if (MovieId) {
	PrintStarWarsMovieCharacter(MovieId);
} else {
	console.error("Error:", 404);
}
