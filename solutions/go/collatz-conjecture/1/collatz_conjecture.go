package collatzconjecture

import "errors"


func CollatzConjecture(n int) (int, error) {
	steps := 0
	if n <= 0 {
		return 0, errors.New("Input must be greater than 0")
	}
	for n != 1 {
		if n%2 == 0 {
			n /= 2
			steps++
		} else {
			n = 3*n + 1
			steps++
		}
	}
	return steps, nil
}
