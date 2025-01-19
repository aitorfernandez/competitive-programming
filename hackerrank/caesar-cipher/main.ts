function caesarCipher(s: string, k: number): string {
	function isLetter(c: string) {
		return (c >= "a" && c <= "z") || (c >= "A" && c <= "Z");
	}

	function isUppercase(c: string) {
		return c === c.toUpperCase();
	}

	const alphabet = "abcdefghijklmnopqrstuvwxyz".split("");

	const positions: { [k: string]: number } = {};
	for (const [i, c] of alphabet.entries()) {
		positions[c] = i;
	}

	const res: string[] = [];

	for (const c of s) {
		if (isLetter(c)) {
			if (isUppercase(c)) {
				const pos = (positions[c.toLowerCase()] + k) % alphabet.length;
				res.push(alphabet[pos].toUpperCase());
			} else {
				const pos = (positions[c] + k) % alphabet.length;
				res.push(alphabet[pos]);
			}
		} else {
			res.push(c);
		}
	}

	console.log(res.join(""));
	return res.join("");
}

console.assert(caesarCipher("middle-Outz", 2) === "okffng-Qwvb");
