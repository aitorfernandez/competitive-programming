function groupAnagrams(strs: string[]): string[][] {
	const res: { [key: string]: string[] } = {};

	for (const str of strs) {
		const k = str.split("").sort().join("");
		if (k in res) {
			res[k].push(str);
		} else {
			res[k] = [str];
		}
	}

	return Object.values(res);
}

console.assert(
	JSON.stringify(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) ===
		JSON.stringify([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
);
console.assert(JSON.stringify(groupAnagrams([""])) === JSON.stringify([[""]]));
console.assert(
	JSON.stringify(groupAnagrams(["a"])) === JSON.stringify([["a"]]),
);
