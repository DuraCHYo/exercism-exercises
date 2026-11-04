// Package weather to work with weather.
package weather

var (
    // CurrentCondition uses for getting condition.
	CurrentCondition string 
    // CurrentLocation uses to get weather for current location.
	CurrentLocation  string 
)
// Forecast returns condition for currentlocation.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
