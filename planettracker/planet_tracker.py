import math
import ephem


class PlanetTracker(ephem.Observer):

    def __init__(self):
        super().__init__()
        self.heavenly_bodies = {
            "jupiter": ephem.Jupiter(),
            "saturn": ephem.Saturn(),
            "moon": ephem.Moon(),
        }

    def calc_planet(self, hb_name, when=None):
        convert = math.pi / 180
        if when is None:
            when = ephem.now()
        self.date = when
        if hb_name not in self.heavenly_bodies:
            raise KeyError(f"Couldn't find {hb_name}")
        planet = self.heavenly_bodies[hb_name]
        planet.compute(self)
        return {
            "az": float(planet.az) * convert,
            "alt": float(planet.alt) * convert,
            "name": hb_name
        }
