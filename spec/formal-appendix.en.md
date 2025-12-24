# Formal Appendix | Axiomatization Appendix

[![中文](https://img.shields.io/badge/中文-版本-blue)](formal-appendix.md)

> **Module**: `spec/formal-appendix`  
> **Purpose**: Formalized definitions and symbolic conventions for MVM core concepts  
> **Status**: Living Document (continuously updated)

---

## Overview

This appendix provides **semi-formalized** definitions for MVM's core concepts. We intentionally maintain a degree of openness—this is not a closed axiomatic system, but an **extensible formalization interface**, welcoming researchers to propose more rigorous mathematical forms on this foundation.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Design Principles                                                          │
│                                                                             │
│  1. Semantic Priority: Definitions should capture core conceptual meaning,  │
│     not pursue pure formal completeness                                     │
│  2. Extensibility: Leave interfaces for different mathematical frameworks   │
│     (set theory, category theory, information theory) to connect            │
│  3. Implementability: Definitions should map to code structures in          │
│     poc/mvm_simulator.py                                                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Basic Symbolic Conventions

| Symbol | Reading | Type | Meaning |
|--------|---------|------|---------|
| $\rho_S$ | rho-S | Structure | Non-existence tension structure / Potentiality field |
| $\omega$ | omega | Parameter | Consciousness spectrum |
| $\theta$ | theta | Parameter | Consciousness path |
| $O$ | observation | Operator | Observation action |
| $S$ | snapshot | Output | Five-dimensional reality snapshot |
| $M$ | manifestation | Operator | Manifestation/Mapping operator |
| $\otimes$ | tensor/convolve | Operator | Non-linear tension convolution |
| $\mathcal{I}$ | interface-set | Set | Potentiality interface atlas |

---

## 2. Non-Existence Tension Structure (ρ_S)

### Definition

```
Axiom M.0: Non-Existence ≠ Nothingness
          Non-existence is structured potentiality, not void
```

**Formalization**:

$$
\rho_S := \langle \mathcal{I}, \mathcal{R}, \tau \rangle
$$

Where:
- $\mathcal{I}$ = Potentiality interface set (all activatable "nodes")
- $\mathcal{R} \subseteq \mathcal{I} \times \mathcal{I}$ = Relations/adjacency structure between interfaces
- $\tau: \mathcal{I} \to \mathbb{R}^+$ = Tension function (activation potential of each interface)

### Properties

```
Axiom M.1: Potentiality field possesses internal "interface atlas" structure
          ∀i ∈ I, ∃ neighborhood(i) ⊆ I
```

```
Axiom M.2: Potentiality field's tension distribution is non-uniform
          ∃ i, j ∈ I : τ(i) ≠ τ(j)
```

### Code Correspondence

```python
# poc/mvm_simulator.py
class PotentialityField:
    interfaces: Dict[str, PotentialityInterface]  # I
    # R implicit in spatial proximity relations of coordinates
    tension_state: float  # τ's global perturbation factor
```

---

## 3. Consciousness Spectrum (ω)

### Definition

```
Axiom C.0: ω determines the potentiality layer and detail resolution 
          consciousness can "perceive/process"
```

**Formalization**:

$$
\omega \in \Omega = \{\omega_l, \omega_m, \omega_h, ...\}
$$

Or continuous version:

$$
\omega: [0, 1] \to \text{ResolutionSpace}
$$

### Layer Definitions

| Layer | Symbol | Characteristics | Accessible Content |
|-------|--------|-----------------|-------------------|
| Low-frequency | $\omega_l$ | Matter/energy layer | Physical laws, spatial structure |
| Mid-frequency | $\omega_m$ | Information/pattern layer | Concepts, relations, patterns |
| High-frequency | $\omega_h$ | Meaning/existence layer | Values, meaning, sense of being |

### Properties

```
Axiom C.1: Higher ω can access higher density potentiality interfaces
          ω₁ < ω₂ ⟹ Accessible(ω₁) ⊆ Accessible(ω₂)
```

```
Axiom C.2: ω transition requires crossing energy threshold
          Shift(ω_l → ω_m) requires threshold crossing
```

### Code Correspondence

```python
# poc/mvm_simulator.py
class SpectrumLevel(Enum):
    OMEGA_LOW = 1      # ωₗ
    OMEGA_MEDIUM = 2   # ωₘ
    OMEGA_HIGH = 3     # ωₕ

class SpectrumOmega:
    level: SpectrumLevel
    intensity: float  # [0, 1]
    
    @property
    def resolution(self) -> float:
        return (self.level.value / 3.0) * self.intensity
```

---

## 4. Consciousness Path (θ)

### Definition

```
Axiom C.3: θ determines "where consciousness accesses" and "what it selects"
          θ is a probability distribution with history dependence
```

**Formalization**:

$$
\theta: \mathcal{H} \times \mathcal{I} \to [0, 1]
$$

Where $\mathcal{H}$ is history state space, $\theta(h, i)$ represents probability of accessing interface $i$ given history $h$.

Or path space version:

$$
\theta \in \Theta = \{(i_1, i_2, ..., i_n) \mid i_k \in \mathcal{I}, i_{k+1} \in \text{neighborhood}(i_k)\}
$$

### Properties

```
Axiom C.4: θ possesses history dependence
          P(i_n | i_1, ..., i_{n-1}) ≠ P(i_n)
```

```
Axiom C.5: θ's selection probability is modulated by attention weights
          θ(h, i) ∝ attention(h, i) × density(i)
```

### Path Strategies

| Strategy | Formalization | Description |
|----------|---------------|-------------|
| Random Walk | $\theta(h, i) = \text{uniform}$ | Unbiased exploration |
| History Bias | $\theta(h, i) \propto \text{momentum}(h)$ | Continue along historical direction |
| Attention Focus | $\theta(h, i) \propto \tau(i)$ | Converge toward high-density regions |
| Exploratory Diffusion | $\theta(h, i) \propto \text{novelty}(h, i)$ | Prefer unvisited regions |

### Code Correspondence

```python
# poc/mvm_simulator.py
class PathStrategy(Enum):
    RANDOM = "random"
    HISTORY_BIASED = "history"
    ATTENTION_FOCUSED = "focus"
    EXPLORATORY = "explore"

class ConsciousnessPath:
    strategy: PathStrategy
    position: Tuple[float, ...]
    history: List[Tuple[float, ...]]
    attention_weights: Dict[str, float]
```

---

## 5. Observation Action (O)

### Definition

```
Axiom S.2: O "collapses" potential state into determinate snapshot
          O is a confirmation operator from probability distribution to 
          determinate state
```

**Formalization**:

$$
O: \text{Distribution}(\mathcal{I}) \to \mathcal{I}
$$

Or threshold version:

$$
O(p, i) = \begin{cases} 
\text{confirm}(i) & \text{if } p(i) > \text{threshold} \\
\text{reject} & \text{otherwise}
\end{cases}
$$

### Properties

```
Axiom S.2.1: O's confirmation is irreversible
             Once O(i) = confirm, state is locked
```

```
Axiom S.2.2: States not confirmed by O remain in superposition
             States not observed remain in superposition
```

### Code Correspondence

```python
# poc/mvm_simulator.py
class Observation:
    confirmation_threshold: float
    
    def observe(self, interface, omega, theta) -> bool:
        probability = compute_confirmation_probability(...)
        return random.random() < probability
```

---

## 6. Manifestation Operator (M) and Core Formula

### Core Formula

$$
S := M(\rho_S \otimes (\omega, \theta, O))
$$

### Expanded Form

$$
S = M\Big(\rho_S, \omega, \theta(h), O\Big) = \text{Snapshot}\Big(
  \underbrace{\text{select}(\theta, \rho_S)}_{\text{path selects interface}},
  \underbrace{\text{resolve}(\omega, i)}_{\text{spectrum determines resolution}},
  \underbrace{O(p_i)}_{\text{observation confirms state}}
\Big)
$$

### Tension Convolution Operator (⊗)

```
Axiom F.1: ⊗ is non-linear
          M(ρ ⊗ (ω₁ + ω₂)) ≠ M(ρ ⊗ ω₁) + M(ρ ⊗ ω₂)
```

```
Axiom F.2: ⊗ has perturbation effect
          ρ' = ρ ⊗ θ ⟹ tension_distribution(ρ') ≠ tension_distribution(ρ)
```

### Code Correspondence

```python
# poc/mvm_simulator.py
class ManifestationOperator:
    def generate_snapshot(self) -> Optional[Snapshot]:
        # Step 1: θ samples position
        position = self.path.sample_next_position(self.field)
        
        # Step 2: Query ω-compatible interfaces
        interfaces = self.field.query_interfaces(position, self.spectrum.level)
        
        # Step 3: O confirmation
        if self.observer.observe(selected, self.spectrum, self.path):
            return Snapshot(...)
        return None
```

---

## 7. Snapshot (S) Structure

### Definition

```
Axiom S.1: Reality consists of discrete snapshot sequences, not continuous flow
```

**Formalization**:

$$
S := \langle \vec{x}, t, \sigma, C, \text{meta} \rangle
$$

Where:
- $\vec{x} = (x, y, z)$ — Spatial coordinates
- $t \in \mathbb{Z}^+$ — Temporal index (discrete)
- $\sigma$ — Consciousness dimension signature
- $C$ — Snapshot content (structured data)
- $\text{meta}$ — Metadata (ω, θ_hash, O_confirmed)

### Snapshot Chains

$$
\text{Chain} := (S_1, S_2, ..., S_n) \text{ where } t_{k+1} = t_k + 1
$$

```
Axiom S.4: Time is the sequence number difference of snapshot chain
          Δt = t_j - t_i (not continuous flow)
```

```
Axiom S.5: Causality is structural coupling, not linear transmission
          S_i → S_j does not imply i < j
```

### Code Correspondence

```python
# poc/mvm_simulator.py
@dataclass
class Snapshot:
    spatial: Tuple[float, float, float]  # (x, y, z)
    temporal_index: int                   # t
    consciousness_signature: str          # σ
    content: Dict                         # C
    omega_level: SpectrumLevel           # meta
    theta_path_hash: str                 # meta
    observation_confirmed: bool          # meta
```

---

## 8. Axiom Index

### Meta-Void Axioms (M.x)

| ID | Axiom | Document Reference |
|----|-------|-------------------|
| M.0 | Non-Existence ≠ Nothingness | [tension-structure.md](../core/meta-void/tension-structure.md) |
| M.1 | Potentiality field possesses internal interface atlas structure | [tension-structure.md](../core/meta-void/tension-structure.md) |
| M.2 | Potentiality field tension distribution is non-uniform | [potentiality-field.md](../core/meta-void/potentiality-field.md) |
| M.3 | "Foreshock" incubation period exists before manifestation | [potentiality-field.md](../core/meta-void/potentiality-field.md) |

### Consciousness Axioms (C.x)

| ID | Axiom | Document Reference |
|----|-------|-------------------|
| C.0 | ω determines perception layer and resolution | [spectrum-omega.md](../core/consciousness/spectrum-omega.md) |
| C.1 | Higher ω accesses higher density interfaces | [spectrum-omega.md](../core/consciousness/spectrum-omega.md) |
| C.2 | ω transition requires threshold crossing | [spectrum-omega.md](../core/consciousness/spectrum-omega.md) |
| C.3 | θ determines access position and selection | [path-theta.md](../core/consciousness/path-theta.md) |
| C.4 | θ possesses history dependence | [path-theta.md](../core/consciousness/path-theta.md) |
| C.5 | θ is modulated by attention weights | [path-theta.md](../core/consciousness/path-theta.md) |

### Snapshot Axioms (S.x)

| ID | Axiom | Document Reference |
|----|-------|-------------------|
| S.1 | Reality consists of discrete snapshot sequences | [discrete-generation.en.md](../engine/snapshot-service/discrete-generation.en.md) |
| S.2 | O collapses potential state to determinate state | [discrete-generation.en.md](../engine/snapshot-service/discrete-generation.en.md) |
| S.4 | Time is sequence number difference of snapshot chain | [snapshot-chains.en.md](../engine/snapshot-service/snapshot-chains.en.md) |
| S.5 | Causality is structural coupling | [snapshot-chains.en.md](../engine/snapshot-service/snapshot-chains.en.md) |

### Formula Axioms (F.x)

| ID | Axiom | Document Reference |
|----|-------|-------------------|
| F.1 | ⊗ operator is non-linear | [formula-S.en.md](../engine/mapping-logic/formula-S.en.md) |
| F.2 | ⊗ has perturbation effect | [formula-S.en.md](../engine/mapping-logic/formula-S.en.md) |

---

## 9. Open Formalization Directions

Following are formalization directions we welcome researchers to explore:

| Direction | Mathematical Framework | Potential Yield |
|-----------|----------------------|-----------------|
| Category Theory Reconstruction | Category Theory | Define M as functor, ρ_S as category |
| Measure Theory Version | Measure Theory | Define θ as probability measure |
| Information Theory Quantification | Information Theory | Quantify ω's resolution using entropy |
| Topological Space | Topology | Endow I with topological structure |
| Quantum Formalism | Quantum Mechanics | Correspond O to wavefunction collapse |

→ Welcome to submit your formalization attempts via [Formalization Issue template](../../issues/new?template=formalization.md)

---

## Navigation

| Direction | Link |
|-----------|------|
| ⬅️ Return | [spec/](../) |
| 🔗 System Overview | [system-overview.en.md](system-overview.en.md) |
| 🔗 Meta-Void | [tension-structure.md](../core/meta-void/tension-structure.md) |
| 🔗 Consciousness Spectrum | [spectrum-omega.md](../core/consciousness/spectrum-omega.md) |
| 🔗 POC Simulator | [mvm_simulator.py](../poc/mvm_simulator.py) |

---

<div align="center">

*"Formalization is not the endpoint, but the starting point for more precise dialogue."*

</div>

