from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from window import create_window_svg

app = FastAPI()


@app.get("/api/")
def read_item(
    units: str | None = None,
    lat: float | None = None,
    lon: float | None = None,
    lang: str | None = None,
):
    svg = create_window_svg(units, lat, lon, lang)
    return HTMLResponse(
        content=svg,
        status_code=200,
        media_type="image/svg+xml",
        headers={"content-type": "image/svg+xml"},
    )
