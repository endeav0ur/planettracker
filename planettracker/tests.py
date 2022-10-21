import math
import ephem

from planet_tracker import PlanetTracker


def test_calc_az_about_moon():
    convert = math.pi / 180
    moon = ephem.Moon()
    greenwich = ephem.Observer()
    greenwich.lat = "51.4769"
    greenwich.lon = "-0.0005"

    moon.compute(greenwich)
    az_deg, alt_deg = moon.az * convert, moon.alt * convert
    print(f"Moons' current azimuth and elevation {az_deg:.2f}, {alt_deg:.2f}")


def test_calc_jupiter():
    tracker = PlanetTracker()
    tracker.lat = "51.4769"
    tracker.lon = "-0.0005"
    result = tracker.calc_planet("jupiter")
    print(result)


if __name__ == "__main__":
    test_calc_az_about_moon()
    test_calc_jupiter()

