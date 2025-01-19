function countingSort(arr: number[]): number[] {
	const res = new Array(Math.max(...arr) + 1).fill(0);

	for (const n of arr) {
		res[n] += 1;
	}

	return res;
}

console.assert(
	JSON.stringify(countingSort([1, 1, 3, 2, 1])) ===
		JSON.stringify([0, 3, 1, 1]),
);
