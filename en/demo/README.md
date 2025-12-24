# 🎨 Demo | Interactive Visualization

[![中文](https://img.shields.io/badge/中文-版本-blue)](../zh/README.md)

> This directory contains interactive visualizations for MVM.

---

## Snapshot Chain Visualizer

**File**: `snapshot-visualizer.html`

### How to Open

```bash
# Method 1: Open directly in browser
open demo/snapshot-visualizer.html

# Method 2: Use local server
cd demo && python -m http.server 8080
# Then visit http://localhost:8080/snapshot-visualizer.html
```

### Features

- Adjust θ path strategy (Random/History-Biased/Attention-Focused/Exploratory)
- Adjust ω spectrum level (Low/Medium/High frequency)
- Adjust snapshot count and tension perturbation intensity
- Real-time visualization of snapshot chain generation
- Click nodes to view detailed JSON data

### Tech Stack

- D3.js v7 (Visualization)
- Vanilla JavaScript (MVM Simplified Simulator)
- Pure CSS (No framework dependencies)

---

## License

MIT License

