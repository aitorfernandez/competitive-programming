function isPalindrome(str: string): boolean {
	function isAplpha(s: string): boolean {
		return (
			(s >= "a" && s <= "z") || (s >= "A" && s <= "Z") || (s >= "0" && s <= "9")
		);
	}

	const s = str
		.split("")
		.filter((v) => isAplpha(v))
		.join("")
		.toLowerCase();

	let l = 0;
	let r = s.length - 1;

	while (r > l) {
		if (s[l] !== s[r]) {
			return false;
		}
		l += 1;
		r -= 1;
	}

	return true;
}

console.assert(isPalindrome("A man, a plan, a canal: Panama"));

console.assert(!isPalindrome("race a car"));
console.assert(!isPalindrome("0P"));
