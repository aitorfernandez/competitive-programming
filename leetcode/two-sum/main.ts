function twoSum(nums: number[], target: number): number[] {
	const count: { [key: number]: number } = {};

	for (const [i, n] of nums.entries()) {
		const diff = target - n;
		if (diff in count) {
			return [count[diff], i];
		}
		count[n] = i;
	}

	return [];
}

console.assert(
	JSON.stringify(twoSum([2, 7, 11, 15], 9)) === JSON.stringify([0, 1]),
);
console.assert(JSON.stringify(twoSum([3, 2, 4], 6)) === JSON.stringify([1, 2]));
