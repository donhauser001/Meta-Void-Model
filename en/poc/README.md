# 🧪 Proof of Concept | Conceptual Verification Simulator

[![中文](https://img.shields.io/badge/中文-版本-blue)](../zh/README.md)

> **License**: MIT (Free to modify, commercial use permitted)  
> **Disclaimer**: This is a **conceptual simulation** demonstrating the logical structure of MVM's core formula, not a precise model of physical reality.

---

## 📐 Core Formula

```
S := M(ρ_S ⊗ (ω, θ, O))

Where:
- S   : Five-dimensional reality snapshot (x, y, z | t | consciousness dimension)
- M   : Manifestation/Mapping operator
- ρ_S : Non-existence tension structure (Potentiality field)
- ω   : Consciousness spectrum (Depth/Resolution)
- θ   : Consciousness path (Selection/History)
- O   : Observation action (Confirmation/Lock)
```

---

## 🚀 Quick Start

### Basic Execution

```bash
cd poc && python mvm_simulator.py
```

### Using MVMConfig (Recommended)

```python
from mvm_simulator import MVMSimulator, MVMConfig, SpectrumLevel, PathStrategy

# Create configuration object
config = MVMConfig(
    field_dimensions=5,        # Potentiality field dimensions
    interface_count=1000,      # Potentiality interface count
    path_strategy=PathStrategy.HISTORY_BIASED,  # θ path strategy
    initial_omega=SpectrumLevel.OMEGA_MEDIUM,   # ω initial spectrum
    snapshot_count=50,         # Target snapshot count
    confirmation_threshold=0.5 # O confirmation threshold
)

# Initialize simulator
sim = MVMSimulator(config=config)

# Run simulation
chain = sim.run()

# Get report
print(sim.report(chain))
```

### Backward-Compatible Initialization

```python
# Direct parameter passing also supported (backward compatible)
sim = MVMSimulator(
    path_strategy=PathStrategy.ATTENTION_FOCUSED,
    initial_omega=SpectrumLevel.OMEGA_HIGH
)
```

---

## 📦 API Reference

### MVMConfig

Configuration dataclass, replacing magic string parameters:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `field_dimensions` | int | 5 | Potentiality field dimensions |
| `interface_count` | int | 1000 | Potentiality interface count |
| `path_strategy` | PathStrategy | HISTORY_BIASED | θ path sampling strategy |
| `initial_omega` | SpectrumLevel | OMEGA_MEDIUM | ω initial spectrum level |
| `snapshot_count` | int | 50 | Target snapshot count |
| `confirmation_threshold` | float | 0.5 | O observation confirmation threshold |

### PathStrategy (θ Path Strategies)

| Strategy | Value | Description |
|----------|-------|-------------|
| `RANDOM` | "random" | Random walk, unbiased exploration |
| `HISTORY_BIASED` | "history" | History bias, follows inertial direction |
| `ATTENTION_FOCUSED` | "focus" | Attention focus, converges toward high density |
| `EXPLORATORY` | "explore" | Exploratory diffusion, prefers unknown regions |

### SpectrumLevel (ω Spectrum Levels)

| Level | Value | Description | Accessible Content |
|-------|-------|-------------|-------------------|
| `OMEGA_LOW` | 1 | Low frequency - Matter/Energy layer | Physical laws, spatial structure |
| `OMEGA_MEDIUM` | 2 | Mid frequency - Information/Pattern layer | Concepts, relations, patterns |
| `OMEGA_HIGH` | 3 | High frequency - Meaning/Existence layer | Values, meaning, sense of being |

### SnapshotChain

Snapshot chain object containing simulation results:

```python
chain.length           # Snapshot count
chain.temporal_span    # Temporal span
chain.snapshots        # Snapshot list
chain.to_dict()        # Convert to dictionary
chain.to_json()        # Export as JSON string
```

---

## 📤 JSON Export

### Export Snapshot Chain

```python
# Export as JSON string
json_str = chain.to_json(indent=2)

# Or convert to dictionary
data = chain.to_dict()
```

### Output Structure

```json
{
  "chain_id": "8ad4eb50",
  "length": 50,
  "temporal_span": 49,
  "snapshots": [
    {
      "index": 0,
      "snapshot_id": "7a8c9722589be3ec",
      "spatial": {"x": 0.67, "y": -0.19, "z": -0.23},
      "temporal_index": 1,
      "omega": "OMEGA_MEDIUM",
      "theta_hash": "e47fdec5",
      "confirmed": true,
      "content": {
        "interface_id": "PI_0152",
        "density": 1.96,
        "coordinates": [...],
        "field_tension": 1.0
      }
    },
    ...
  ]
}
```

---

## 📊 Visualization Example

```python
import matplotlib.pyplot as plt
from mvm_simulator import MVMSimulator, MVMConfig

# Run simulation
config = MVMConfig(snapshot_count=100)
sim = MVMSimulator(config=config)
chain = sim.run()

# Plot tension fluctuation
tensions = [s.content["field_tension"] for s in chain.snapshots]
indices = [s.temporal_index for s in chain.snapshots]

plt.figure(figsize=(10, 4))
plt.plot(indices, tensions, marker='o', markersize=3)
plt.xlabel("Temporal Index (t)")
plt.ylabel("Field Tension (τ)")
plt.title("MVM Simulation: Tension vs Time")
plt.grid(True, alpha=0.3)
plt.savefig("tension_plot.png")
plt.show()
```

---

## 🔧 Component Mapping

| MVM Concept | Python Class | Responsibility |
|-------------|--------------|----------------|
| Potentiality Field ρ_S | `PotentialityField` | Manage potentiality interface collection and tension state |
| Consciousness Path θ | `ConsciousnessPath` | Path sampling and history management |
| Consciousness Spectrum ω | `SpectrumOmega` | Spectrum level and resolution control |
| Observation Action O | `Observation` | Confirmation threshold judgment |
| Manifestation Operator M | `ManifestationOperator` | Core generation logic |
| Snapshot S | `Snapshot` | Single frame reality data |
| Snapshot Chain | `SnapshotChain` | Time series and export |

---

## ⚠️ Limitations

1. **Simplified Model**: Real ρ_S structure is far more complex than this simulation
2. **Numerical Approximation**: Continuous consciousness spectrum is discretized
3. **Single-Machine Execution**: Distributed consciousness network not implemented
4. **No Quantum Effects**: Real quantum randomness not integrated

---

## 🎯 Research Directions

- [ ] Integrate Quantum Random Number Generator (QRNG)
- [ ] Implement multi-node distributed simulation
- [ ] Add Web visualization interface (Three.js)
- [ ] Integrate with LLM to verify AI manifestation hypothesis
- [ ] Export to Unity/Unreal consumable format

---

## 📖 References

- [Core Formula →](../engine/mapping-logic/formula-S.md)
- [Formal Appendix →](../spec/formal-appendix.md)
- [Snapshot Mechanism →](../engine/snapshot-service/discrete-generation.md)
- [AI Manifestation Research →](../lab/research/ai-manifestation.md)

---

<div align="center">

*"Code is the executable form of thought."*

**MIT License** — Fork it. Extend it. Build upon it.

</div>

