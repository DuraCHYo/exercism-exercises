package isbnverifier

import (
	"strings"
	"strconv"
)

func IsValidISBN(isbn string) bool {
	isbn = strings.ReplaceAll(isbn, "-", "")

	if len(isbn) != 10 {
		return false
	}

	sum := 0
	for i := 0; i < 10; i++ {
		var number int
		if i == 9 && isbn[i] == 'X' {
			number = 10
		} else {
			n, err := strconv.Atoi(string(isbn[i]))
			if err != nil {
				return false
			}
			number = n
		}
		sum += number * (10 - i)
	}
	return sum%11 == 0
}