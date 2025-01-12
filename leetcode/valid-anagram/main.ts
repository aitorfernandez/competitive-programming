function isAnagram(s: string, t: string): boolean {
	if (s.length !== t.length) {
		return false;
	}

	const res: { [key: string]: number } = {};

	for (let i = 0; i < s.length; i += 1) {
		res[s[i]] = (res[s[i]] ?? 0) + 1;
		res[t[i]] = (res[t[i]] ?? 0) - 1;
	}

	return Object.values(res).every((v) => v === 0);
}

console.assert(isAnagram("anagram", "nagaram"));

console.assert(!isAnagram("rat", "car"));
