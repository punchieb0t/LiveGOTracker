# LiveGOTracker

Real-time GO Transit train tracker using the Metrolinx Open Data API.

![GO Transit Train Tracker](screenshot.png)

## Features

- 🚂 Live train positions on an interactive map
- 🎨 Color-coded dots matching GO Transit line colors
- 🔄 Auto-refreshes every 60 seconds
- 📍 Click any train for details (trip number, delay, next stop)

## Running

```bash
cd gotracker
python3 server.py
```

Then open http://localhost:3030

## Line Colors

| Line | Color |
|------|-------|
| Lakeshore West (LW) | Dark Red |
| Lakeshore East (LE) | Bright Red |
| Milton (MI) | Orange |
| Kitchener (KI) | Green |
| Richmond Hill (RH) | Light Blue |
| Barrie (BR) | Dark Blue |
| Stouffville (ST) | Brown |

## API

Uses the [Metrolinx Open Data API](https://api.openmetrolinx.com/OpenDataAPI/Help).
