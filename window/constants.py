import os

from dotenv import load_dotenv

from .types import LangEnum, UnitEnum

load_dotenv()

OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")

# New York City
DEFAULT_LOCATION = {
    "lat": 40.7128,
    "lng": -74.0060,
}
DEFAULT_LANG = LangEnum.en
DEFAULT_UNITS = UnitEnum.metric


HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
TIME_COLORS = [
    {"r": 4, "g": 10, "b": 30},
    {"r": 139, "g": 152, "b": 206},
    {"r": 86, "g": 216, "b": 255},
    {"r": 255, "g": 216, "b": 116},
    {"r": 255, "g": 183, "b": 116},
    {"r": 255, "g": 153, "b": 116},
    {"r": 255, "g": 103, "b": 116},
    {"r": 20, "g": 40, "b": 116},
]
SUNRISE_COLOR_IDX = 2
SUNSET_COLOR_IDX = 6
