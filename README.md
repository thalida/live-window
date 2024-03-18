<div align="center">
  <img src="https://github.com/thalida/live-window/assets/3401715/938cbcba-90cc-461c-942c-873c092c8e28" />
  <h1>
    Live Window
  </h1>
  <strong>
    Generate a live window svg with semi-accurate sky color and weather for any location!
  </strong>
</div>

## Usage

Embed the image into your HTML or Markdown Document:
```html
<img src="https://livewindow-api.onrender.com/api/" />
```

### API Options

| Parameter | Description | Options | Default |
|-----------|-------------|---------|---------|
| units     | Temperature units | `imperial` (`°F`), `metric` (`°C`), `standard` (`K`) | `metric` |
| lang     | Description language | `af`, `al`, `ar`, `az`, `bg`, `ca`, `cz`, `da`, `de`, `el`, `en`, `eu`, `fa`, `fi`, `fr`, `gl`, `he`, `hi`, `hr`, `hu`, `id`, `it`, `ja`, `kr`, `la`, `lt`, `mk`, `no`, `nl`, `pl`, `pt`, `pt_br`, `ro`, `ru`, `sv`, `se`, `sk`, `sl`, `sp`, `es`, `sr`, `th`, `tr`, `ua`, `uk`, `vi`, `zh_cn`, `zh_tw`, `zu` | `en` |
| location | Location latitude and longitude coordinates  | Any lat,lng | `40.7128,-74.0060` (New York City) |


## Examples

| Window | API Request |
|--------|-----------------------|
| <img src="https://livewindow-api.onrender.com/api/?location=40.7128,-74.0060&units=imperial" /> | **New York, USA (°F)** <br /> `https://livewindow-api.onrender.com/api/?location=40.7128,-74.0060&units=imperial` |
| <img src="https://livewindow-api.onrender.com/api/?location=10.6603,-61.5086" /> | **Port of Spain, Trinidad & Tobago (°C)** <br /> `https://live-window.tunl.sh/api/?location=10.6603,-61.5086` |
| <img src="https://livewindow-api.onrender.com/api/?units=standard&location=48.8566,2.3522&lang=fr" /> | **Paris, France (K)** <br /> `https://live-window.tunl.sh/api/?units=standard&location=48.8566,2.3522&lang=fr` |


## Help!

<details>
  <summary><strong>How do I find my lat, long coordinates?</strong></summary>

  You can use this tool to find your coordinates:
  https://www.latlong.net/convert-address-to-lat-long.html
</details>

## Credits

<details>
  <summary><strong>Open Weather Map API</strong></summary>

  Weather, sunrise, and sunset times are provided by: [https://openweathermap.org/api](https://openweathermap.org/api)
</details>

<details>
  <summary><strong>3D Weather Icons</strong></summary>
  
  [https://ui8.net/msakta/products/weather-animated-icons](https://ui8.net/msakta/products/weather-animated-icons)
</details>

<details>
  <summary><strong>Gradient Abstract Banners</strong></summary>

  While the window frame is designed by @thalida, the gradient blobs are by:
  [https://ui8.net/msakta/products/weather-animated-icons](https://www.figma.com/community/file/1063549775352406477/gradient-abstract-banners?searchSessionId=ltw9aro0-lwjp697d2fs)https://www.figma.com/community/file/1063549775352406477/gradient-abstract-banners?searchSessionId=ltw9aro0-lwjp697d2fs
</details>



