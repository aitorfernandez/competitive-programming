function longestConsecutive(nums: number[]): number {
	const set: Set<number> = new Set(nums);
	const res: { [key: number]: number } = {};

	for (const n of set) {
		if (!set.has(n - 1)) {
			res[n] = 1;

			for (let i = 1; i < set.size; i += 1) {
				if (set.has(n + i)) {
					res[n] += 1;
				} else {
					break;
				}
			}
		}
	}

	return Math.max(...Object.values(res));
}

console.assert(longestConsecutive([100, 4, 200, 1, 3, 2]) === 4);
console.assert(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) === 9);
