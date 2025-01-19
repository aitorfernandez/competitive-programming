function miniMaxSum(arr: number[]): void {
	const nums = arr.sort((a, b) => a - b);

	let min = 0;
	for (let i = 0; i < nums.length - 1; i += 1) {
		min += nums[i];
	}

	let max = 0;
	for (let i = 1; i < nums.length; i += 1) {
		max += nums[i];
	}

	console.log(`${min} ${max}`);
}

miniMaxSum([1, 3, 5, 7, 9]); // 16 24

miniMaxSum([7, 69, 2, 221, 8974]); // 299 9271
