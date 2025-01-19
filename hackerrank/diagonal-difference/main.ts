function diagonalDifference(arr: number[][]): number {
	let d1 = 0;
	for (let i = 0; i < arr.length; i += 1) {
		d1 += arr[i][i];
	}

	let d2 = 0;
	for (let r = 0, c = arr.length - 1; r < arr.length; r += 1, c -= 1) {
		d2 += arr[r][c];
	}

	return Math.abs(d1 - d2);
}

console.assert(
	diagonalDifference([
		[1, 2, 3],
		[4, 5, 6],
		[9, 8, 9],
	]) === 2,
);
