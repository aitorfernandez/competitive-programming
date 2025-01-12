function threeSum(nums: number[]): number[][] {
	const n = nums.sort((a, b) => a - b);
	const res: number[][] = [];

	for (let i = 0; i < n.length; i += 1) {
		if (i > 0 && n[i] === n[i - 1]) {
			continue;
		}

		let l = i + 1;
		let r = n.length - 1;

		while (r > l) {
			const total = n[i] + n[l] + n[r];

			if (total < 0) {
				l += 1;
			} else if (total > 0) {
				r -= 1;
			} else {
				res.push([n[i], n[l], n[r]]);
				l += 1;
				r -= 1;

				while (n[l] === n[l - 1] && l < r) {
					l += 1;
				}
			}
		}
	}

	return res;
}

console.assert(
	JSON.stringify(threeSum([-1, 0, 1, 2, -1, -4])) ===
		JSON.stringify([
			[-1, -1, 2],
			[-1, 0, 1],
		]),
);
console.assert(JSON.stringify(threeSum([0, 1, 1])) === JSON.stringify([]));
console.assert(
	JSON.stringify(threeSum([0, 0, 0])) === JSON.stringify([[0, 0, 0]]),
);
console.assert(
	JSON.stringify(threeSum([0, 0, 0, 0])) === JSON.stringify([[0, 0, 0]]),
);
console.assert(
	JSON.stringify(threeSum([-2, 0, 0, 2, 2])) === JSON.stringify([[-2, 0, 2]]),
);
