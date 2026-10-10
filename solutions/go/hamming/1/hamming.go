package hamming

import "errors"

func Distance(a, b string) (int, error) {
    differences := 0
    if len(a) != len(b) {
        return 0, errors.New("строки должны быть одинаковой длины")
    }
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			differences++
		}
	}
	return differences, nil
}