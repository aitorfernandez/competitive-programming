function containsDuplicate(nums: number[]): boolean {
	const set: Set<number> = new Set();

	for (const n of nums) {
		if (set.has(n)) {
			return true;
		}
		set.add(n);
	}

	return false;
}

console.assert(containsDuplicate([1, 2, 3, 1]));

console.assert(!containsDuplicate([1, 2, 3, 4]));
