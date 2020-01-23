// Package leap report if is a leap year.
package leap

// IsLeapYear check if a year is leap.
func IsLeapYear(year int) bool {
	if year%4 != 0 || year%100 == 0 && year%400 != 0 {
		return false
	}
	return true
}
