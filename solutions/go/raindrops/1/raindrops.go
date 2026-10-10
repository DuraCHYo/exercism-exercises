package raindrops

// import "fmt"
import "strconv"
func Convert(number int) string {
    var result string
    var is_divisable bool = false
    if number % 3 == 0 {
        result += "Pling"
        is_divisable = true
    }
    if number % 5 == 0 {
        result += "Plang"
        is_divisable = true
    }
    if number % 7 == 0 {
        result += "Plong"
        is_divisable = true
    }
    if is_divisable != false {
        return result
    } else {
        return strconv.Itoa(number)
    }
}
