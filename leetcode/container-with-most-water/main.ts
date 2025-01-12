function maxArea(height: number[]): number {
	let l = 0;
	let r = height.length - 1;
	let area = 0;

	while (r > l) {
		const total = (r - l) * Math.min(height[l], height[r]);
		area = Math.max(area, total);

		if (height[l] < height[r]) {
			l += 1;
		} else {
			r -= 1;
		}
	}

	return area;
}

console.assert(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) === 49);
console.assert(maxArea([1, 1]) === 1);
