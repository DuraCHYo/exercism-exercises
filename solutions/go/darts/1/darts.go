package darts
import "math"

func Score(x, y float64) int {
    hit := math.Sqrt(x*x+y*y)
	if hit > 10 {
        return 0
    }
    if hit > 5 && hit <= 10 {
        return 1
    }
    if hit > 1 && hit <= 5 {
        return 5
    }
    return 10
}
