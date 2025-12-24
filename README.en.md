# Meta-Void-Model (MVM)

**A Non-existence Cosmology from the Dimension of Consciousness: A Logical Framework for Discrete Reality Rendering**

<div align="center">

<img src="assets/diagrams/banner-v2.jpg" alt="Meta-Void-Model Banner" width="100%"/>

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
[![Release](https://img.shields.io/github/v/release/donhauser001/Meta-Void-Model?label=Release&color=03624C)](https://github.com/donhauser001/Meta-Void-Model/releases/tag/v3.0.0)
[![中文](https://img.shields.io/badge/中文-README-blue)](README.md)

</div>

---

## TL;DR — 10-Second Introduction

| Question | Answer |
|----------|--------|
| **What is MVM** | A cosmological model that views reality as "discrete rendering of potentiality field by consciousness" |
| **What it's NOT** | Not religion, not a replacement for physics, but a "manifestation logic interface" |
| **Core Formula** | `S := M(ρ_S ⊗ (ω, θ, O))` — Snapshot = Mapping(Potentiality Field ⊗ Consciousness Parameters) |
| **What can you do with it** | Thought experiments, worldview design, interactive art, AI model alignment, game universe building... |

---

## 🧭 Where Should I Start?

<table>
<tr>
<td width="33%">

### 📖 Reader / Philosophy Enthusiast

**Goal**: Understand the complete theory

1. Download from [Release v3.0.0](https://github.com/donhauser001/Meta-Void-Model/releases/tag/v3.0.0)
2. Or read [archive/v3-完稿.md](archive/) (Chinese)
3. Then see [spec/system-overview.md](spec/system-overview.md)

</td>
<td width="33%">

### 📐 Researcher / Want to Formalize

**Goal**: Formalize or refute the model

1. Start from [spec/formal-appendix.md](spec/formal-appendix.md)
2. Dive into [core/](core/) and [engine/](engine/)
3. Submit via [Formalization template](../../issues/new?template=formalization.md)

</td>
<td width="33%">

### 💻 Developer / Interactive & Simulation

**Goal**: Run or extend the simulator

1. Go to [poc/](poc/), run `mvm_simulator.py`
2. Read [engine/snapshot-service/](engine/snapshot-service/)
3. See [poc/README.md](poc/README.md) for API

</td>
</tr>
</table>

---

## Core Architecture

The model is driven by three core logical components:

### Meta-Void (Non-Existence)

> ⚠️ **Terminology Note**: The "Void" here is NOT physical vacuum or Buddhist "emptiness", but a **structured potentiality field with high information entropy that has not yet been activated by consciousness paths**. It contains all possibilities but has not yet "manifested" into any definite form.

```
Non-Existence ≠ Nothingness
Non-Existence = Structured Potentiality awaiting activation
```

### Consciousness Dimensions (ω, θ)

Consciousness is **axiomatized** as the projection dimension of the universe:

| Symbol | Name | Function | Formal Ref |
|:------:|:----:|----------|------------|
| ω | Spectrum | Determines the **texture** and **resolution** of manifestation | [Axiom C.0-C.2](spec/formal-appendix.md) |
| θ | Path | Determines the **specific path** consciousness uses to access the Meta-Void | [Axiom C.3-C.5](spec/formal-appendix.md) |

### Snapshot (5D Reality Frame)

The **space-time quantized unit** of reality.

Each moment of "now" is a **discrete sampling** and **rendering** of the Meta-Void tension by consciousness at a specific frequency.

---

## Core Formula

$$
S := M(\rho_S \otimes (\omega, \theta, O))
$$

Where:
- **S**: 5-dimensional reality snapshot
- **M**: Manifestation/mapping operator  
- **ρ_S**: Non-existence tension structure (potentiality field)
- **ω**: Consciousness spectrum (depth/resolution)
- **θ**: Consciousness path (selection/history)
- **O**: Observation action (confirmation/locking)

> **Note:** The ⊗ operator represents **nonlinear tension convolution**, implying reality is not simple superposition, but a dynamic perturbation of the background field by consciousness paths.

---

## Proof of Concept

```bash
# Run MVM Simulator
cd poc && python mvm_simulator.py
```

```python
from poc.mvm_simulator import MVMSimulator, MVMConfig, SpectrumLevel, PathStrategy

config = MVMConfig(
    path_strategy=PathStrategy.HISTORY_BIASED,
    initial_omega=SpectrumLevel.OMEGA_MEDIUM,
    snapshot_count=50
)
sim = MVMSimulator(config)
chain = sim.run()

# Export to JSON for visualization
print(chain.to_json())
```

→ [Full Simulator Documentation](poc/README.md)

---

## Why Open Source on GitHub?

Theory should not be a closed fortress, but an evolvable interface.

- 🔬 **Logical Refutation**: Invite cross-disciplinary researchers to point out logical breaks → [Submit Refutation](../../issues/new?template=refutation.md)
- 📐 **Mathematical Formalization**: Seek more rigorous mathematical tools → [Submit Formalization](../../issues/new?template=formalization.md)
- 🌿 **Thought Branches**: Support derivative works based on MVM principles

→ See [spec/manifesto.md](spec/manifesto.md) for our full manifesto

---

## Boundaries & Open Questions

MVM does not claim to have solved everything. Here are the **logical boundaries** we actively disclose:

| Domain | To Be Resolved |
|--------|----------------|
| **θ Discrete Threshold** | Does consciousness path have a minimum quantized unit? |
| **Multi-Agent Sync** | How do different consciousness paths reach consensus in the same "snapshot frame"? |
| **Recursion Paradox** | If consciousness itself is manifestation, who observes consciousness? |
| **Causality Reversal** | How to redefine causality in a non-time-priority framework? |

---

## System Navigation

| Module | Responsibility | Entry |
|:------:|----------------|-------|
| 📋 `spec/` | System specifications | [→ paradigm-shift](spec/paradigm-shift.md) |
| 📐 `spec/formal-appendix` | **Axiomatized Appendix** | [→ formal-appendix](spec/formal-appendix.md) |
| 🔧 `core/meta-void` | Meta-Void definition | [→ tension-structure](core/meta-void/tension-structure.md) |
| 🔧 `core/consciousness` | Consciousness dimensions | [→ spectrum-omega](core/consciousness/spectrum-omega.md) |
| ⚙️ `engine/snapshot-service` | Snapshot rendering | [→ discrete-generation](engine/snapshot-service/discrete-generation.md) |
| ⚙️ `engine/mapping-logic` | Mapping engine | [→ formula-S](engine/mapping-logic/formula-S.md) |
| 🔬 `lab/` | Experiments & Research | [→ ai-manifestation](lab/research/ai-manifestation.md) |
| 🧪 `poc/` | Proof of Concept | [→ mvm_simulator.py](poc/mvm_simulator.py) |
| 📖 **Full Index** | SUMMARY | [→ Navigation](SUMMARY.md) |
| 🏷️ **Release** | v3.0.0 | [→ Releases](https://github.com/donhauser001/Meta-Void-Model/releases/tag/v3.0.0) |

---

## License

This project uses a **layered licensing** strategy:

| Directory/Content | License | Description |
|-------------------|---------|-------------|
| `archive/`, all `.md` docs | **CC BY-NC-ND 4.0** | Protect original text integrity |
| `poc/` code, future demos | **MIT** | Allow free modification and commercial use |
| Issue templates, GitHub configs | **CC0** | Public domain |

---

<div align="center">

*"In this collective meditation on manifestation, I do not offer truth, only an interface to observe truth."*

**[中文版 →](README.md)**

</div>

