function isPalindrome(s: string, left: number, right: number): boolean {
	let l = left;
	let r = right;

	while (r > l) {
		if (s[l] !== s[r]) {
			return false;
		}
		l += 1;
		r -= 1;
	}
	return true;
}

function palindromeIndex(s: string): number {
	let l = 0;
	let r = s.length - 1;

	while (r > l) {
		if (s[l] !== s[r]) {
			if (isPalindrome(s, l + 1, r)) {
				return l;
			}
			if (isPalindrome(s, l, r - 1)) {
				return r;
			}
		}
		l += 1;
		r -= 1;
	}

	return -1;
}

console.assert(palindromeIndex("aaab") === 3);

console.assert(palindromeIndex("aaaa") === -1);
