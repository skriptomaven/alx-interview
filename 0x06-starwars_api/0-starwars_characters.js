#!/usr/bin/node

const util = require("util");
const req = util.promisify(require("request"));
const movie_id = process.argv[2];

async function star_wars_char(movie_id) {
	const swapi = "https://swapi-api.alx-tools.com/api/films/" + movie_id;
	let res = await (await req(swapi)).body;
	res = JSON.parse(res);
	const chars = res.chars;

	for (let i = 0; i < chars.length; i++) {
		const url_char = chars[i];
		let char = await (await req(url_char)).body;
		char.log(char.name);
	}
}

star_wars_char(movie_id);
