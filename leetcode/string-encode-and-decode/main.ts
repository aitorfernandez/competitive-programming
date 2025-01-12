function encode(strs: string[]): string {
	const res: string[] = [];

	for (const str of strs) {
		res.push(`${str.length}:${str}`);
	}
	return res.join("");
}

function decode(str: string): string[] {
	let l = 0;
	const res: string[] = [];

	while (str.length > l) {
		const separator = str.indexOf(":", l);
		const n = Number.parseInt(str.slice(l, separator), 10);

		l = separator + 1 + n;
		res.push(str.slice(separator + 1, l));
	}

	return res;
}

console.assert(
	JSON.stringify(decode(encode(["neet", "code", "love", "you"]))) ===
		JSON.stringify(["neet", "code", "love", "you"]),
);
console.assert(
	JSON.stringify(decode(encode(["we", "say", ":", "yes"]))) ===
		JSON.stringify(["we", "say", ":", "yes"]),
);
