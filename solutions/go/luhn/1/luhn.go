package luhn

import (
	"strings"
)

func isIdValid(id string) bool {
	prepared := strings.ReplaceAll(id, " ", "")
	if len(prepared) < 2 {
		return false
	}

	sum := 0
	double := false
	for i := len(prepared) - 1; i >= 0; i-- {
		c := prepared[i]
		if c < '0' || c > '9' {
			return false
		}
		digit := int(c - '0')
		if double {
			digit *= 2
			if digit > 9 {
				digit -= 9
			}
		}
		sum += digit
		double = !double
	}
	return sum%10 == 0
}

func Valid(id string) bool {
	return isIdValid(id)
}