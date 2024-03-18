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
| lang     | `af`, `al`, `ar`, `az`, `bg`, `ca`, `cz`, `da`, `de`, `el`, `en`, `eu`, `fa`, `fi`, `fr`, `gl`, `he`, `hi`, `hr`, `hu`, `id`, `it`, `ja`, `kr`, `la`, `lt`, `mk`, `no`, `nl`, `pl`, `pt`, `pt_br`, `ro`, `ru`, `sv`, `se`, `sk`, `sl`, `sp`, `es`, `sr`, `th`, `tr`, `ua`, `uk`, `vi`, `zh_cn`, `zh_tw`, `zu` | `en` |
| location | Latitude, Longitude coordinates  | Any lat,lng | `40.7128,-74.0060` (New York City) |


## Examples

| Window | API Request |
|--------|-----------------------|
| <img src="https://livewindow-api.onrender.com/api/?location=40.7128,-74.0060&units=imperial" /> | **New York (°F)** <br /> `https://livewindow-api.onrender.com/api/?location=40.7128,-74.0060&units=imperial` |
| <img src="https://livewindow-api.onrender.com/api/?location=10.6918,61.2225" /> | **Trinidad & Tobago (°C)** <br /> `https://live-window.tunl.sh/api/?location=10.6918,61.2225` /> |
| <img src="https://livewindow-api.onrender.com/api/?units=standard&location=48.8566,2.3522&lang=fr" /> | **Paris, France (K)** <br /> `https://live-window.tunl.sh/api/?units=standard&location=48.8566,2.3522&lang=fr` /> |


## Credits

