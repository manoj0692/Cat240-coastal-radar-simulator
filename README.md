# CAT-240 Coastal Radar Data Simulator

Professional CAT-240 marine radar video simulator for generating realistic coastal surveillance radar traffic over UDP.

Designed for:
- Radar system development
- ASTERIX CAT-240 testing
- Coastal surveillance simulation
- Network packet validation
- Maritime radar research
- Visualization and decoder testing

---

## Features

- Real-time CAT-240 UDP packet transmission
- Simulated rotating radar sweep
- Marine radar video generation
- Dynamic ship targets
- Coastal clutter simulation
- Sea clutter/noise generation
- ASTERIX CAT-240 compliant packet structure
- Configurable radar parameters
- Lightweight Python implementation

---

## Radar Simulation

The simulator generates realistic radar returns including:

### 🌊 Sea Clutter
Background radar noise to emulate ocean reflections.

### 🚢 Ship Targets
Dynamic high-intensity radar echoes representing marine vessels.

### 🏝 Coastal Reflections
Strong static returns simulating shoreline and landmass echoes.

### 🔄 Rotating Antenna Sweep
Continuous azimuth rotation from 0° to 359°.

---

## Supported CAT-240 Fields

| FRN | Item | Description |
|---|---|---|
| 1 | I240/010 | Data Source Identifier |
| 2 | I240/000 | Message Type |
| 3 | I240/020 | Video Record Header |
| 6 | I240/041 | Video Header Femto |
| 7 | I240/049 | Video Counters |
| 10 | I240/051 | Video Block Medium |
| 12 | I240/140 | Time of Day |

---

## Technology Stack

- Python 3
- UDP Networking
- Binary Packet Encoding
- ASTERIX CAT-240 Protocol

---

## Project Structure

```text
cat240-coastal-radar-simulator/
│
├── simulator.py
├── README.md
├── requirements.txt
├── captures/
├── docs/
└── screenshots/
