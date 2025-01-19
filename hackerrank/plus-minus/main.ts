function plusMinus(nums: number[]): void {
	const count: number[] = Array(3).fill(0);

	for (const n of nums) {
		if (n > 0) {
			count[0] += 1;
		} else if (n < 0) {
			count[1] += 1;
		} else {
			count[2] += 1;
		}
	}

	for (const n of count) {
		console.log((n / nums.length).toFixed(6));
	}
}

plusMinus([-4, 3, -9, 0, 4, 1]);

plusMinus([1, -2, -7, 9, 1, -8, -5]);
