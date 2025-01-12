function topKFrequent(nums: number[], k: number): number[] {
	const count: { [key: number]: number } = {};

	for (const n of nums) {
		count[n] = (count[n] ?? 0) + 1;
	}

	const freq: [number, number][] = Object.entries(count).map(([k, v]) => [
		Number(k),
		v,
	]);
	freq.sort((a, b) => b[1] - a[1]);

	const res: number[] = [];

	for (let i = 0; i < k; i += 1) {
		res.push(freq[i][0]);
	}

	return res;
}

console.assert(
	JSON.stringify(topKFrequent([1, 1, 1, 2, 2, 3], 2)) ===
		JSON.stringify([1, 2]),
);
console.assert(JSON.stringify(topKFrequent([1], 1)) === JSON.stringify([1]));
console.assert(
	JSON.stringify(topKFrequent([1, 2], 2)) === JSON.stringify([1, 2]),
);
