import os

from dotenv import load_dotenv
import requests
from rich import print

load_dotenv()


# New York City
DEFAULT_LOCATION = {
    "lat": 40.7128,
    "lng": -74.0060,
}
OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")


def get_weather_svg(
    units: str | None = "metric",
    lat: float | None = DEFAULT_LOCATION["lat"],
    lon: float | None = DEFAULT_LOCATION["lng"],
    lang: str | None = "en",
):
    units = units or "metric"
    lat = lat or DEFAULT_LOCATION["lat"]
    lon = lon or DEFAULT_LOCATION["lng"]
    lang = lang or "en"

    weather_data = get_weather_data(units, lat, lon, lang)
    weather_icon = weather_data["weather"][0]["icon"]
    celestial_body_svg = get_celestial_body_svg(weather_icon)
    weather_icon_svg = get_weather_icon_svg(weather_icon)

    return f"""
    <svg width="444" height="528" viewBox="0 0 444 528" fill="none" xmlns="http://www.w3.org/2000/svg">
        <g clip-path="url(#clip0_303_174)">
            <g id="outside" clip-path="url(#clip1_303_174)">
                <rect id="outside__sky" x="32" width="380" height="512" fill="url(#paint0_linear_303_174)"/>
                {celestial_body_svg if celestial_body_svg else ""}
                {weather_icon_svg if weather_icon_svg else ""}
            </g>
            <g id="window__glass" clip-path="url(#clip3_303_174)">
                <path d="M38.5 152.5L95.2577 56L479.654 440.396L393.795 526.255L38.5 152.5Z" fill="#CCD7DE" fill-opacity="0.05"/>
                <rect x="-5" y="234.166" width="50.4153" height="449.031" transform="rotate(-45 -5 234.166)" fill="#CCD7DE" fill-opacity="0.05"/>
            </g>
            <g id="window__frame" clip-path="url(#clip4_303_174)">
                <path d="M404 190V504H40V190C40 89.4842 121.484 8 222 8C322.516 8 404 89.4842 404 190Z" stroke="#36334D" stroke-width="16"/>
                <rect x="32" y="187" width="380" height="16" fill="#36334D"/>
                <rect x="220" width="8" height="203" fill="#36334D"/>
                <rect x="353.88" y="53.289" width="8" height="189.334" transform="rotate(45 353.88 53.289)" fill="#36334D"/>
                <rect x="88" y="56.8284" width="8" height="189.334" transform="rotate(-45 88 56.8284)" fill="#36334D"/>
                <g filter="url(#filter0_i_303_174)">
                    <path d="M0 512C0 503.163 7.16344 496 16 496H428C436.837 496 444 503.163 444 512V520C444 524.418 440.418 528 436 528H8C3.58172 528 0 524.418 0 520V512Z" fill="#36334D"/>
                </g>
            </g>
        </g>
        <defs>
            <filter id="filter0_i_303_174" x="0" y="496" width="444" height="32" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
                <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                <feOffset dy="-8"/>
                <feComposite in2="hardAlpha" operator="arithmetic" k2="-1" k3="1"/>
                <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"/>
            <feBlend mode="normal" in2="shape" result="effect1_innerShadow_303_174"/>
            </filter>
            <linearGradient id="paint0_linear_303_174" x1="32" y1="-7" x2="412" y2="520.5" gradientUnits="userSpaceOnUse">
                <stop stop-color="#142372"/>
                <stop offset="1" stop-color="#09123F"/>
            </linearGradient>
            <linearGradient id="paint1_linear_303_174" x1="178.485" y1="308.737" x2="178.485" y2="288.795" gradientUnits="userSpaceOnUse">
                <stop stop-color="#22A6B3"/>
                <stop offset="0.26" stop-color="#35B0BC"/>
                <stop offset="0.8" stop-color="#68CBD4"/>
                <stop offset="1" stop-color="#7ED6DF"/>
            </linearGradient>
            <linearGradient id="paint2_linear_303_174" x1="220.272" y1="308.737" x2="220.272" y2="109" gradientUnits="userSpaceOnUse">
                <stop stop-color="#22A6B3"/>
                <stop offset="0.26" stop-color="#35B0BC"/>
                <stop offset="0.8" stop-color="#68CBD4"/>
                <stop offset="1" stop-color="#7ED6DF"/>
            </linearGradient>
            <linearGradient id="paint3_linear_303_174" x1="260.445" y1="308.737" x2="260.445" y2="109" gradientUnits="userSpaceOnUse">
                <stop stop-color="#22A6B3"/>
                <stop offset="0.26" stop-color="#35B0BC"/>
                <stop offset="0.8" stop-color="#68CBD4"/>
                <stop offset="1" stop-color="#7ED6DF"/>
            </linearGradient>
            <linearGradient id="paint4_linear_303_174" x1="314.904" y1="146.476" x2="272.247" y2="189.188" gradientUnits="userSpaceOnUse">
                <stop stop-color="#5F27CD"/>
                <stop offset="0.13" stop-color="#5024BB" stop-opacity="0.97"/>
                <stop offset="0.28" stop-color="#4421AB" stop-opacity="0.94"/>
                <stop offset="0.46" stop-color="#3A209F" stop-opacity="0.92"/>
                <stop offset="0.67" stop-color="#351F99" stop-opacity="0.9"/>
            <stop offset="1" stop-color="#341F97" stop-opacity="0.9"/>
            </linearGradient>
            <linearGradient id="paint5_linear_303_174" x1="289.01" y1="161.243" x2="165.869" y2="284.544" gradientUnits="userSpaceOnUse">
                <stop stop-color="white"/>
                <stop offset="0.22" stop-color="#FCFCFC"/>
                <stop offset="0.4" stop-color="#F3F3F3" stop-opacity="0.99"/>
                <stop offset="0.57" stop-color="#E4E4E4" stop-opacity="0.97"/>
                <stop offset="0.72" stop-color="#D0D0D0" stop-opacity="0.95"/>
                <stop offset="0.87" stop-color="#B5B5B5" stop-opacity="0.93"/>
                <stop offset="1" stop-color="#999999" stop-opacity="0.9"/>
            </linearGradient>
            <linearGradient id="paint6_linear_303_174" x1="218.058" y1="198.905" x2="137.634" y2="279.434" gradientUnits="userSpaceOnUse">
                <stop stop-color="white"/>
                <stop offset="0.22" stop-color="#FCFCFC"/>
                <stop offset="0.4" stop-color="#F3F3F3" stop-opacity="0.99"/>
                <stop offset="0.57" stop-color="#E4E4E4" stop-opacity="0.97"/>
                <stop offset="0.72" stop-color="#D0D0D0" stop-opacity="0.95"/>
                <stop offset="0.87" stop-color="#B5B5B5" stop-opacity="0.93"/>
                <stop offset="1" stop-color="#999999" stop-opacity="0.9"/>
            </linearGradient>
            <clipPath id="clip0_303_174">
                <rect width="444" height="528" fill="white"/>
            </clipPath>
            <clipPath id="clip1_303_174">
                <path d="M32 190C32 85.0659 117.066 0 222 0V0C326.934 0 412 85.0659 412 190V512H32V190Z" fill="white"/>
            </clipPath>
            <clipPath id="clip2_303_174">
                <rect width="240" height="199.737" fill="white" transform="translate(110 109)"/>
            </clipPath>
            <clipPath id="clip3_303_174">
                <rect width="380" height="512" fill="white" transform="translate(32)"/>
            </clipPath>
            <clipPath id="clip4_303_174">
                <rect width="444" height="528" fill="white"/>
            </clipPath>
        </defs>
    </svg>
    """


def get_weather_data(
    units: str = "metric",
    lat: float = DEFAULT_LOCATION["lat"],
    lon: float = DEFAULT_LOCATION["lng"],
    lang: str = "en",
):
    return requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={
            "units": units,
            "lat": lat,
            "lon": lon,
            "lang": lang,
            "appid": OPEN_WEATHER_API_KEY,
        },
    ).json()


def get_celestial_body_svg(icon: str):
    icon_suffix = icon[-1]
    celestial_body = "moon" if icon_suffix == "n" else "sun"
    file_path = f"weather/svgs/{celestial_body}.svg"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read()
    else:
        return None


def get_weather_icon_svg(icon: str):
    icon_without_suffix = icon[:-1]
    file_path = f"weather/svgs/weather-{icon_without_suffix}.svg"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read()
    else:
        return None
