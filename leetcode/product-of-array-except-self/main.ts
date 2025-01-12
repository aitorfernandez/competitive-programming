function productExceptSelf(nums: number[]): number[] {
	const res: number[] = new Array(nums.length).fill(0);

	let prefix = 1;
	for (let i = 0; i < nums.length; i += 1) {
		res[i] = prefix;
		prefix *= nums[i];
	}

	let postfix = 1;
	for (let i = nums.length - 1; i >= 0; i -= 1) {
		res[i] *= postfix;
		postfix *= nums[i];
	}

	return res;
}

console.assert(
	JSON.stringify(productExceptSelf([1, 2, 3, 4])) ===
		JSON.stringify([24, 12, 8, 6]),
);
console.assert(
	JSON.stringify(productExceptSelf([-1, 1, 0, -3, 3])) ===
		JSON.stringify([0, 0, 9, 0, 0]),
);
