function lonelyInteger(numbers: number[]): number {
	const count: { [k: number]: number } = {};

	for (const n of numbers) {
		count[n] = (count[n] ?? 0) + 1;
	}

	for (const [k, v] of Object.entries(count)) {
		if (v === 1) {
			return Number(k);
		}
	}

	return 0;
}

console.assert(lonelyInteger([1, 2, 3, 4, 3, 2, 1]) === 4);
