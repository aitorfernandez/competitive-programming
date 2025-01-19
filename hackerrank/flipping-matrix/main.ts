function flippingMatrix(matrix: number[][]): number {
	const n = matrix.length / 2;
	let total = 0;

	for (let r = 0; r < n; r += 1) {
		for (let c = 0; c < n; c += 1) {
			total += Math.max(
				matrix[r][c],
				matrix[r][matrix.length - 1 - c],
				matrix[matrix.length - 1 - r][c],
				matrix[matrix.length - 1 - r][matrix.length - 1 - c],
			);
		}
	}

	return total;
}

console.assert(
	flippingMatrix([
		[112, 42, 83, 119],
		[56, 125, 56, 49],
		[15, 78, 101, 43],
		[62, 98, 114, 108],
	]) === 414,
);
