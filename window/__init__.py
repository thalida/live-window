from collections import defaultdict
from datetime import datetime, timedelta
from math import floor
import os

import requests

from .constants import (
    DEFAULT_LANG,
    DEFAULT_LOCATION,
    DEFAULT_UNITS,
    OPEN_WEATHER_API_KEY,
    SUNRISE_COLOR_IDX,
    SUNSET_COLOR_IDX,
    TIME_COLORS,
)

from .types import UnitEnum


def create_window_svg(
    units: UnitEnum = DEFAULT_UNITS,
    lat: float = DEFAULT_LOCATION["lat"],
    lon: float = DEFAULT_LOCATION["lng"],
    lang: str = DEFAULT_LANG,
):
    weather_data = get_weather_data(units, lat, lon, lang)

    if units == "metric":
        symbol = "°C"
    elif units == "imperial":
        symbol = "°F"
    else:
        symbol = "K"

    location = weather_data["name"]
    currently = f"{weather_data['main']['temp']}{symbol}, {weather_data['weather'][0]['description']}"

    sunrise_time = datetime.fromtimestamp(weather_data["sys"]["sunrise"])
    sunset_time = datetime.fromtimestamp(weather_data["sys"]["sunset"])

    gradient = getRealisticColorGradient(sunrise_time, sunset_time)
    start_color = f"rgb({gradient['start']['r']}, {gradient['start']['g']}, {gradient['start']['b']})"
    end_color = (
        f"rgb({gradient['end']['r']}, {gradient['end']['g']}, {gradient['end']['b']})"
    )
    text_color = getContrastColor(gradient["end"])

    weather_icon = weather_data["weather"][0]["icon"]
    celestial_body_svg = get_celestial_body_svg(weather_icon)
    weather_icon_svg = get_weather_icon_svg(weather_icon)

    return f"""
    <svg width="642" height="528" viewBox="0 0 642 528" fill="none" xmlns="http://www.w3.org/2000/svg">
        <g clip-path="url(#clip0_331_346)">
            <g clip-path="url(#clip1_331_346)">
                <path d="M506.116 336.61C589.563 263.203 670.707 126.922 575.409 40.1824C503.812 -24.9955 411.312 84.951 331.815 69.8087C265.814 57.1352 194.052 -12.4866 130.85 51.3745C86.5747 95.9786 112.58 160.004 99.5773 214.319C84.435 277.357 -40.8184 371.339 62.2153 422.032C184.671 482.273 358.149 435.693 467.273 366.401C479.781 358.336 492.949 348.296 506.116 336.61Z" fill="url(#paint0_linear_331_346)"/>
                <path opacity="0.62" d="M467.931 356.525C517.473 346.321 531.134 365.907 572.611 351.423C581.169 348.461 625.444 332.824 638.447 296.121C655.07 248.554 610.137 190.947 570.636 163.625C498.051 113.261 408.843 141.077 384.648 148.483C366.708 154.079 290.832 179.755 242.113 257.607C212.322 305.338 170.68 408.042 220.551 469.105C252.647 508.443 318.154 525.56 345.476 503.505C369.012 484.577 346.957 450.342 374.444 410.017C401.436 370.186 453.118 359.488 467.931 356.525Z" fill="#B7D1E8"/>
                <path d="M390.244 144.533C336.259 93.1806 271.574 53.0205 201.13 28.6611C180.556 21.5837 164.426 17.3043 142.7 19.6086C90.1956 25.2047 55.9608 73.4297 54.9732 124.288C54.3149 159.346 66.33 193.252 79.8264 225.511C93.3228 257.771 107.807 292.5 115.872 327.558C122.62 357.513 123.114 396.027 157.019 409.194C194.381 423.678 227.3 396.356 260.711 384.177C339.057 355.867 380.204 463.838 455.587 446.721C571.952 420.222 495.747 275.218 454.105 217.446C435.177 191.277 413.781 166.917 390.244 144.533Z" fill="url(#paint1_linear_331_346)"/>
                <path d="M64.3548 306.325C52.6689 320.48 71.103 345.663 89.7018 333.647C115.378 317.847 82.1306 281.966 64.3548 306.325Z" fill="#E4EEF7"/>
                <path d="M40.6539 253.492C19.0926 288.056 88.056 311.757 85.7518 267.976C85.4226 245.262 53.6566 234.235 40.6539 253.492Z" fill="#E4EEF7"/>
                <path d="M424.15 90.0532C422.175 87.5844 419.871 85.2801 417.237 83.305C413.287 80.507 408.843 78.2027 404.07 77.0506C395.84 74.9109 387.611 77.2152 379.381 75.7339C375.925 75.0755 371.645 73.9233 368.518 72.1129C362.428 68.3273 344.653 33.4341 331.156 50.2223C326.383 55.983 324.408 64.0479 325.889 71.4545C327.206 77.3798 330.992 82.9758 337.575 83.4696C340.702 83.6342 343.994 82.8113 347.121 82.3175C349.59 81.9883 355.845 79.684 358.149 81.1653C364.404 85.4447 374.444 116.223 388.269 126.428C396.169 132.353 406.868 134.657 416.085 130.378C424.973 126.428 430.24 117.54 430.24 107.994C430.24 101.245 427.935 95.1555 424.15 90.0532Z" fill="#D2E2F1" fill-opacity="0.59"/>
                <path d="M590.057 399.648C595.057 399.648 599.11 395.595 599.11 390.596C599.11 385.596 595.057 381.543 590.057 381.543C585.058 381.543 581.005 385.596 581.005 390.596C581.005 395.595 585.058 399.648 590.057 399.648Z" fill="#E4EEF7"/>
                <path d="M559.608 426.806C562.789 426.806 565.369 424.226 565.369 421.045C565.369 417.863 562.789 415.284 559.608 415.284C556.426 415.284 553.847 417.863 553.847 421.045C553.847 424.226 556.426 426.806 559.608 426.806Z" stroke="#E4EEF7" stroke-width="1.2727" stroke-miterlimit="10"/>
                <path d="M389.257 506.632C394.256 506.632 398.309 502.579 398.309 497.579C398.309 492.58 394.256 488.527 389.257 488.527C384.257 488.527 380.204 492.58 380.204 497.579C380.204 502.579 384.257 506.632 389.257 506.632Z" stroke="#E4EEF7" stroke-width="2" stroke-miterlimit="10"/>
                <path d="M380.862 449.19C385.8 450.013 389.092 454.622 388.434 459.559C387.611 464.497 383.002 467.789 378.064 467.13" stroke="#E4EEF7" stroke-width="2" stroke-miterlimit="10"/>
                <path d="M493.772 467.295L483.073 462.357L477.313 472.726L466.614 467.624L461.018 477.993L450.155 473.056L444.559 483.425" stroke="#E4EEF7" stroke-width="3.0845" stroke-miterlimit="10"/>
                <path d="M551.872 392.077L547.099 387.468L542.49 383.025L548.745 381.214L554.999 379.404L553.353 385.823L551.872 392.077Z" stroke="#E4EEF7" stroke-miterlimit="10"/>
                <path d="M9.05248 300.894C14.052 300.894 18.105 296.841 18.105 291.841C18.105 286.842 14.052 282.789 9.05248 282.789C4.05293 282.789 0 286.842 0 291.841C0 296.841 4.05293 300.894 9.05248 300.894Z" fill="#E4EEF7"/>
                <path d="M41.1476 314.884C44.3292 314.884 46.9083 312.305 46.9083 309.123C46.9083 305.942 44.3292 303.363 41.1476 303.363C37.9661 303.363 35.387 305.942 35.387 309.123C35.387 312.305 37.9661 314.884 41.1476 314.884Z" stroke="#E4EEF7" stroke-width="1.2727" stroke-miterlimit="10"/>
                <path d="M26.17 310.276L26.0054 323.443L25.8408 336.61L14.484 329.862L3.29187 323.114L14.6486 316.694L26.17 310.276Z" stroke="#E4EEF7" stroke-width="2.0193" stroke-miterlimit="10"/>
                <path d="M418.883 478.487L413.451 474.701L406.703 474.537L410.489 469.105L410.653 462.357L416.085 466.143L422.833 466.307L419.048 471.739L418.883 478.487Z" fill="#E4EEF7"/>
                <path d="M392.055 33.105C397.054 33.105 401.107 29.052 401.107 24.0525C401.107 19.0529 397.054 15 392.055 15C387.055 15 383.002 19.0529 383.002 24.0525C383.002 29.052 387.055 33.105 392.055 33.105Z" stroke="#E4EEF7" stroke-width="2" stroke-miterlimit="10"/>
                <path d="M425.96 59.7686C421.352 61.9082 416.085 59.9331 413.945 55.3246C411.806 50.7161 413.781 45.4492 418.389 43.3095" stroke="#E4EEF7" stroke-width="2" stroke-miterlimit="10"/>
                <path d="M378.064 56.4768H384.648L390.244 53.0204V59.604L393.865 65.2001H387.117L381.521 68.8211L381.685 62.0729L378.064 56.4768Z" fill="#E4EEF7"/>
            </g>
            <g clip-path="url(#clip2_331_346)">
                <g clip-path="url(#clip3_331_346)">
                    <rect x="114" width="380" height="512" fill="url(#paint2_linear_331_346)"/>
                    {celestial_body_svg if celestial_body_svg else ""}
                    {weather_icon_svg if weather_icon_svg else ""}
                </g>
                <g clip-path="url(#clip5_331_346)">
                    <path d="M120.5 152.5L177.258 56L561.654 440.396L475.795 526.255L120.5 152.5Z" fill="#CCD7DE" fill-opacity="0.05"/>
                    <rect x="77" y="234.166" width="50.4153" height="449.031" transform="rotate(-45 77 234.166)" fill="#CCD7DE" fill-opacity="0.05"/>
                </g>
                <g clip-path="url(#clip6_331_346)">
                    <path d="M486 190V504H122V190C122 89.4842 203.484 8 304 8C404.516 8 486 89.4842 486 190Z" stroke="#36334D" stroke-width="16"/>
                    <rect x="114" y="187" width="380" height="16" fill="#36334D"/>
                    <rect x="302" width="8" height="496" fill="#36334D"/>
                    <rect x="435.88" y="53.289" width="8" height="189.334" transform="rotate(45 435.88 53.289)" fill="#36334D"/>
                    <rect x="170" y="56.8284" width="8" height="189.334" transform="rotate(-45 170 56.8284)" fill="#36334D"/>
                    <g filter="url(#filter0_i_331_346)">
                    <path d="M82 512C82 503.163 89.1634 496 98 496H510C518.837 496 526 503.163 526 512V520C526 524.418 522.418 528 518 528H90C85.5817 528 82 524.418 82 520V512Z" fill="#36334D"/>
                    </g>
                </g>
                <g clip-path="url(#clip5_303_174)">
                    <text class="location-text" x="144" y="450" fill="{text_color}" opacity="0.7">{location}</text>
                    <text class="currently-text" x="144" y="480" fill="{text_color}">{currently}</text>
                </g>
            </g>
        </g>
        <defs>
            <style>
                /* latin-ext */
                @font-face {{
                    font-family: 'Bebas Neue';
                    font-style: normal;
                    font-weight: 400;
                    font-display: swap;
                    src: url(data:font/woff2;base64,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) format('woff2');
                    unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
                }}
                /* latin */
                @font-face {{
                    font-family: 'Bebas Neue';
                    font-style: normal;
                    font-weight: 400;
                    font-display: swap;
                    src: url(data:font/woff2;base64,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) format('woff2');
                    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
                }}
            </style>
            <style>
                .location-text {{
                    font-family: 'Bebas Neue', sans-serif;
                    font-weight: 700;
                    font-size: 24px;
                }}

                .currently-text {{
                    font-family: 'Bebas Neue', sans-serif;
                    font-size: 20px;
                }}
            </style>
            <filter id="filter0_i_331_346" x="82" y="496" width="444" height="32" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
            <feFlood flood-opacity="0" result="BackgroundImageFix"/>
            <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
            <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
            <feOffset dy="-8"/>
            <feComposite in2="hardAlpha" operator="arithmetic" k2="-1" k3="1"/>
            <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"/>
            <feBlend mode="normal" in2="shape" result="effect1_innerShadow_331_346"/>
            </filter>
            <linearGradient id="paint0_linear_331_346" x1="21.7971" y1="234.6" x2="618.508" y2="234.6" gradientUnits="userSpaceOnUse">
            <stop stop-color="#959EC2"/>
            <stop offset="1" stop-color="#D9E5FA"/>
            </linearGradient>
            <linearGradient id="paint1_linear_331_346" x1="-86.4589" y1="140.609" x2="406.576" y2="286.106" gradientUnits="userSpaceOnUse">
            <stop offset="2.34751e-07" stop-color="#E9B7D4"/>
            <stop offset="0.9995" stop-color="#C0B9DB"/>
            </linearGradient>
            <linearGradient id="paint2_linear_331_346" x1="114" y1="-7" x2="494" y2="520.5" gradientUnits="userSpaceOnUse">
            <stop stop-color="{start_color}"/>
            <stop offset="1" stop-color="{end_color}"/>
            </linearGradient>
            <clipPath id="clip0_331_346">
            <rect width="642" height="528" fill="white"/>
            </clipPath>
            <clipPath id="clip1_331_346">
            <rect width="642" height="498.236" fill="white" transform="translate(0 15)"/>
            </clipPath>
            <clipPath id="clip2_331_346">
            <rect width="444" height="528" fill="white" transform="translate(82)"/>
            </clipPath>
            <clipPath id="clip3_331_346">
            <path d="M114 190C114 85.0659 199.066 0 304 0V0C408.934 0 494 85.0659 494 190V512H114V190Z" fill="white"/>
            </clipPath>
            <clipPath id="clip5_331_346">
            <rect width="380" height="512" fill="white" transform="translate(114)"/>
            </clipPath>
            <clipPath id="clip6_331_346">
            <rect width="444" height="528" fill="white" transform="translate(82)"/>
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
    file_path = f"window/svgs/{celestial_body}.svg"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read()
    else:
        return None


def get_weather_icon_svg(icon: str):
    icon_without_suffix = icon[:-1]
    file_path = f"window/svgs/weather-{icon_without_suffix}.svg"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read()
    else:
        return None


def getColorBlend(start_color, end_color, distance):
    blend = defaultdict(int)
    for part in ["r", "g", "b"]:
        blend[part] = round(
            start_color[part] + (end_color[part] - start_color[part]) * distance
        )

    return blend


def getContrastColor(color):
    return (
        "black"
        if (color["r"] * 0.299 + color["g"] * 0.587 + color["b"] * 0.114) > 186
        else "white"
    )


def getRealisticColor(sunrise_time, sunset_time, now):
    print(now)
    if now < sunrise_time:
        color_phase = TIME_COLORS[0 : SUNRISE_COLOR_IDX + 1]
        phase_start_time = datetime(now.year, now.month, now.day, 0, 0, 0, 0)
        phase_end_time = sunrise_time
    elif now >= sunset_time:
        color_phase = TIME_COLORS[SUNSET_COLOR_IDX:]
        color_phase.append(TIME_COLORS[0])
        phase_start_time = sunset_time
        phase_end_time = datetime(
            sunset_time.year, sunset_time.month, sunset_time.day, 23, 59, 59, 999
        )
    else:
        color_phase = TIME_COLORS[SUNRISE_COLOR_IDX : SUNSET_COLOR_IDX + 1]
        phase_start_time = sunrise_time
        phase_end_time = sunset_time

    time_since_start = now - phase_start_time
    time_in_phase = phase_end_time - phase_start_time
    distance = time_since_start / time_in_phase

    print(
        "time_since_start:",
        time_since_start,
        "time_in_phase:",
        time_in_phase,
        "distance:",
        distance,
        "color_phase:",
        color_phase,
    )

    phase_segments = time_in_phase / (len(color_phase) - 1)
    start_color_idx = floor((len(color_phase) - 1) * distance)
    start_color_idx = (
        start_color_idx if start_color_idx < len(color_phase) else len(color_phase) - 1
    )
    end_color_idx = (
        start_color_idx + 1
        if start_color_idx < len(color_phase) - 1
        else len(color_phase) - 1
    )

    start_color_time = phase_start_time + start_color_idx * phase_segments
    end_color_time = phase_start_time + end_color_idx * phase_segments

    time_in_segments = end_color_time - start_color_time
    time_since_segment_start = now - start_color_time
    distance_in_segment = (
        time_since_segment_start / time_in_segments if time_in_segments else 1
    )
    start_color = color_phase[start_color_idx]
    end_color = color_phase[end_color_idx]

    return getColorBlend(start_color, end_color, distance_in_segment)


def getRealisticColorGradient(sunrise_time, sunset_time):
    now = datetime.now()
    hour_ago = now - timedelta(hours=1)

    gradientStart = getRealisticColor(sunrise_time, sunset_time, hour_ago)
    gradientEnd = getRealisticColor(sunrise_time, sunset_time, now)

    if now >= sunset_time:
        gradient = {
            "start": gradientEnd,
            "end": gradientStart,
        }
    else:
        gradient = {
            "start": gradientStart,
            "end": gradientEnd,
        }

    return gradient
