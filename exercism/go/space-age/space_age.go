package space

// Planet string type
type Planet string

const earthSeconds = 365.25 * 24 * 60 * 60

var planets = map[Planet]float64{
	"Earth":   1,
	"Mercury": 0.2408467,
	"Venus":   0.61519726,
	"Mars":    1.8808158,
	"Jupiter": 11.862615,
	"Saturn":  29.447498,
	"Uranus":  84.016846,
	"Neptune": 164.79132,
}

// Age calculate how old someone would be in other planet
func Age(s float64, p Planet) float64 {
	if val, ok := planets[p]; ok {
		return s / (val * earthSeconds)
	}
	return 0
}
