function timeConversion(s: string): string {
	const values = s.split(":");
	const format = values[2].slice(2, values[2].length);

	values[2] = values[2].slice(0, 2);

	if (format === "AM" && values[0] === "12") {
		values[0] = "00";
	}

	if (format === "PM" && values[0] !== "12") {
		values[0] = `${Number(values[0]) + 12}`;
	}

	return `${values[0]}:${values[1]}:${values[2]}`;
}

console.assert(timeConversion("07:05:45PM") === "19:05:45");

console.assert(timeConversion("12:40:22AM") === "00:40:22");

console.assert(timeConversion("12:45:54PM") === "12:45:54");
