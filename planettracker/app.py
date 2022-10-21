import asyncio
from aiohttp import web

from planet_tracker import PlanetTracker


routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    return web.FileResponse("./index.html")


@routes.get("/planets/{name}")
async def get_planet_ephmeris(request):
    planet_name = request.match_info['name']
    data = request.query
    try:
        geo_location_data = {
           "lon": str(data["lon"]),
            "lat": str(data["lat"]),
            "elevation": float(data["elevation"])
        }
    except KeyError:
        # default to Greenwich Observatory
        geo_location_data = {
            "lon": "-0.0005",
            "lat": "51.4769",
            "elevation": 0.0
        }
    print(f"get_planet_ephmeris: {planet_name}, {geo_location_data}")
    tracker = PlanetTracker()
    tracker.lon = geo_location_data["lon"]
    tracker.lat = geo_location_data["lat"]
    tracker.elevation = geo_location_data["elevation"]
    planet_data = tracker.calc_planet(planet_name)
    return web.json_response(planet_data)


app = web.Application()
app.add_routes(routes)
web.run_app(app, host="localhost", port=8000)


async def start_app():
    global runner
    runner: web.AppRunner(app)
    await runner.setup()
    _site = web.TCPSite(runner, host="localhost", port=8000)
    await _site.start()
    print(f"Serving up app")
    return runner, _site

loop = asyncio.get_event_loop()
runner, _site = loop.run_until_complete(start_app())
try:
    loop.run_forever()
except KeyboardInterrupt as error:
    loop.run_until_complete(runner.cleanup())


