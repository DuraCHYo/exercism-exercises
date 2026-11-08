package differenceofsquares

func SquareOfSum(n int) int {
	var sm int = 0
	for i := 1; i <= n; i++ {
		sm += i
	}
	return sm * sm
}

func SumOfSquares(n int) int {
	var sm int = 0
	for i := 1; i <= n; i++ {
		sm += (i * i)
	}
	return sm
}

func Difference(n int) int {
	return SquareOfSum(n) - SumOfSquares(n)
}
