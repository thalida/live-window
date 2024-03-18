from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from window import create_window_svg
from window.constants import DEFAULT_LANG, DEFAULT_LOCATION, DEFAULT_UNITS
from window.types import LangEnum, UnitEnum

app = FastAPI(
    title="Live Window API",
    version="1.0.0",
    contact={
        "url": "hhttps://github.com/thalida/live-window",
        "email": "livewindow@thalida.com",
    },
    license_info={
        "name": "GNU Affero General Public License v3.0",
        "url": "https://github.com/thalida/live-window/blob/main/LICENSE",
    },
    docs_url=None,
    redoc_url=None,
)


@app.get("/api/")
def generate_image(
    units: UnitEnum = DEFAULT_UNITS,
    location: str = f"{DEFAULT_LOCATION['lat']},{DEFAULT_LOCATION['lng']}",
    lang: LangEnum = DEFAULT_LANG,
) -> HTMLResponse:
    lat_str, lon_str = location.split(",")

    lat = float(lat_str) if lat_str else None
    lon = float(lon_str) if lon_str else None

    if lat is None or lon is None:
        lat, lon = DEFAULT_LOCATION["lat"], DEFAULT_LOCATION["lng"]

    svg = create_window_svg(units, lat, lon, lang)
    return HTMLResponse(
        content=svg,
        status_code=200,
        media_type="image/svg+xml",
        headers={
            "Content-Type": "image/svg+xml",
            "Cache-Control": "no-cache, max-age=0",
            "Expires": "Thu, 01 Jan 1970 00:00:00 GMT",
        },
    )


@app.get("/", include_in_schema=False)
def index():
    return HTMLResponse(
        content=f"""
            <!doctype html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <title>{app.title}</title>
                <!-- Embed elements Elements via Web Component -->
                <script src="https://unpkg.com/@stoplight/elements/web-components.min.js"></script>
                <link rel="stylesheet" href="https://unpkg.com/@stoplight/elements/styles.min.css">
                <style>
                    .wrapper {{
                        display: block;
                        height: 100%;
                        padding: 1rem;
                        }}

                    @media screen and (min-width: 1200px) {{
                        .wrapper {{
                            display: block;
                            height: 100vh;
                            padding: 0;
                        }}
                    }}
                </style>

            </head>
            <body>
                <div class="wrapper">
                    <elements-api
                        id="docs"
                        apiDescriptionUrl="{app.openapi_url}"
                        router="hash"
                        layout="stacked" />
                </div>
                <script>
                    const doc = document.querySelector('#docs');

                    function throttle(fn, delay) {{
                        let lastCall = 0;
                        return function (...args) {{
                            const now = (new Date).getTime();
                            if (now - lastCall < delay) {{
                                return;
                            }}
                            lastCall = now;
                            return fn(...args);
                        }}
                    }}

                    function updateLayout() {{
                        doc.layout = window.innerWidth >= 1200 ? 'sidebar' : 'stacked';
                    }}

                    let trottledUpdateLayout = throttle(updateLayout, 250);

                    window.addEventListener('resize', trottledUpdateLayout);
                    trottledUpdateLayout();
                </script>
            </body>
            </html>
            """,
        status_code=200,
        media_type="text/html",
    )
