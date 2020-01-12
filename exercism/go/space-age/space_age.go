package space

// Planet string type
type Planet string

const earthSeconds = 365.25 * 24 * 60 * 60

// Age calculate how old someone would be in other planet
func Age(s float64, p Planet) float64 {
	o := orbitalPeriod(p)
	return s / (o * earthSeconds)
}

func orbitalPeriod(p Planet) float64 {
	switch p {
	case "Earth":
		return 1
	case "Mercury":
		return 0.2408467
	case "Venus":
		return 0.61519726
	case "Mars":
		return 1.8808158
	case "Jupiter":
		return 11.862615
	case "Saturn":
		return 29.447498
	case "Uranus":
		return 84.016846
	case "Neptune":
		return 164.79132
	default:
		return 0
	}
}
