# Formal Appendix | 公理化附录

> **Module**: `spec/formal-appendix`  
> **Purpose**: MVM 核心概念的形式化定义与符号约定  
> **Status**: Living Document (持续更新)

---

## 概述

本附录为 MVM 的核心概念提供**半形式化**定义。我们有意保持一定的开放性——这不是一套封闭的公理系统，而是一个**可扩展的形式化接口**，欢迎研究者在此基础上提出更严格的数学形式。

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  设计原则                                                                    │
│                                                                             │
│  1. 语义优先：定义应捕捉概念的核心含义，而非追求纯粹的形式完备                   │
│  2. 可扩展性：留出接口供不同数学框架（集合论、范畴论、信息论）接入               │
│  3. 可实现性：定义应能映射到 poc/mvm_simulator.py 中的代码结构                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. 基础符号约定

| 符号 | 读法 | 类型 | 含义 |
|------|------|------|------|
| $\rho_S$ | rho-S | 结构 | 非存在张力结构 / 潜能场 |
| $\omega$ | omega | 参数 | 意识频谱 |
| $\theta$ | theta | 参数 | 意识路径 |
| $O$ | observation | 算子 | 观察行为 |
| $S$ | snapshot | 输出 | 五维现实快照 |
| $M$ | manifestation | 算子 | 显现/映射算子 |
| $\otimes$ | tensor/convolve | 算子 | 非线性张力卷积 |
| $\mathcal{I}$ | interface-set | 集合 | 潜能接口图谱 |

---

## 2. 非存在张力结构 (ρ_S)

### 定义

```
Axiom M.0: Non-Existence ≠ Nothingness
          非存在是结构化的潜能，而非空无
```

**形式化**：

$$
\rho_S := \langle \mathcal{I}, \mathcal{R}, \tau \rangle
$$

其中：
- $\mathcal{I}$ = 潜能接口集合（所有可被激活的"节点"）
- $\mathcal{R} \subseteq \mathcal{I} \times \mathcal{I}$ = 接口间的关系/邻接结构
- $\tau: \mathcal{I} \to \mathbb{R}^+$ = 张力函数（每个接口的"激活势能"）

### 性质

```
Axiom M.1: 潜能场具有内在的"接口图谱"结构
          ∀i ∈ I, ∃ neighborhood(i) ⊆ I
```

```
Axiom M.2: 潜能场的张力分布是非均匀的
          ∃ i, j ∈ I : τ(i) ≠ τ(j)
```

### 代码对应

```python
# poc/mvm_simulator.py
class PotentialityField:
    interfaces: Dict[str, PotentialityInterface]  # I
    # R 隐含在 coordinates 的空间邻近关系中
    tension_state: float  # τ 的全局扰动因子
```

---

## 3. 意识频谱 (ω)

### 定义

```
Axiom C.0: ω 决定意识能够"感知/处理"的潜能层级和细节分辨率
```

**形式化**：

$$
\omega \in \Omega = \{\omega_l, \omega_m, \omega_h, ...\}
$$

或连续版本：

$$
\omega: [0, 1] \to \text{ResolutionSpace}
$$

### 层级定义

| 层级 | 符号 | 特征 | 可访问内容 |
|------|------|------|------------|
| 低频 | $\omega_l$ | 物质/能量层 | 物理定律、空间结构 |
| 中频 | $\omega_m$ | 信息/模式层 | 概念、关系、模式 |
| 高频 | $\omega_h$ | 意义/存在层 | 价值、意义、存在感 |

### 性质

```
Axiom C.1: 更高的 ω 能访问更高密度的潜能接口
          ω₁ < ω₂ ⟹ Accessible(ω₁) ⊆ Accessible(ω₂)
```

```
Axiom C.2: ω 的转换需要跨越能量阈值
          Shift(ω_l → ω_m) requires threshold crossing
```

### 代码对应

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

## 4. 意识路径 (θ)

### 定义

```
Axiom C.3: θ 决定意识"访问哪里"和"选择什么"
          θ 是带有历史依赖的概率分布
```

**形式化**：

$$
\theta: \mathcal{H} \times \mathcal{I} \to [0, 1]
$$

其中 $\mathcal{H}$ 是历史状态空间，$\theta(h, i)$ 表示在历史 $h$ 下访问接口 $i$ 的概率。

或路径空间版本：

$$
\theta \in \Theta = \{(i_1, i_2, ..., i_n) \mid i_k \in \mathcal{I}, i_{k+1} \in \text{neighborhood}(i_k)\}
$$

### 性质

```
Axiom C.4: θ 具有历史依赖性
          P(i_n | i_1, ..., i_{n-1}) ≠ P(i_n)
```

```
Axiom C.5: θ 的选择概率受注意力权重调制
          θ(h, i) ∝ attention(h, i) × density(i)
```

### 路径策略

| 策略 | 形式化 | 描述 |
|------|--------|------|
| 随机游走 | $\theta(h, i) = \text{uniform}$ | 无偏好探索 |
| 历史偏好 | $\theta(h, i) \propto \text{momentum}(h)$ | 沿历史方向继续 |
| 注意力聚焦 | $\theta(h, i) \propto \tau(i)$ | 向高密度区域收敛 |
| 探索扩散 | $\theta(h, i) \propto \text{novelty}(h, i)$ | 偏好未访问区域 |

### 代码对应

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

## 5. 观察行为 (O)

### 定义

```
Axiom S.2: O 将潜在态"坍缩"为确定的快照
          O 是从概率分布到确定状态的确认算子
```

**形式化**：

$$
O: \text{Distribution}(\mathcal{I}) \to \mathcal{I}
$$

或带阈值版本：

$$
O(p, i) = \begin{cases} 
\text{confirm}(i) & \text{if } p(i) > \text{threshold} \\
\text{reject} & \text{otherwise}
\end{cases}
$$

### 性质

```
Axiom S.2.1: O 的确认是不可逆的
             Once O(i) = confirm, state is locked
```

```
Axiom S.2.2: 未被 O 确认的状态保持叠加
             States not observed remain in superposition
```

### 代码对应

```python
# poc/mvm_simulator.py
class Observation:
    confirmation_threshold: float
    
    def observe(self, interface, omega, theta) -> bool:
        probability = compute_confirmation_probability(...)
        return random.random() < probability
```

---

## 6. 显现算子 (M) 与核心公式

### 核心公式

$$
S := M(\rho_S \otimes (\omega, \theta, O))
$$

### 展开形式

$$
S = M\Big(\rho_S, \omega, \theta(h), O\Big) = \text{Snapshot}\Big(
  \underbrace{\text{select}(\theta, \rho_S)}_{\text{路径选择接口}},
  \underbrace{\text{resolve}(\omega, i)}_{\text{频谱确定分辨率}},
  \underbrace{O(p_i)}_{\text{观察确认状态}}
\Big)
$$

### 张力卷积算子 (⊗)

```
Axiom F.1: ⊗ 是非线性的
          M(ρ ⊗ (ω₁ + ω₂)) ≠ M(ρ ⊗ ω₁) + M(ρ ⊗ ω₂)
```

```
Axiom F.2: ⊗ 具有扰动效应
          ρ' = ρ ⊗ θ ⟹ tension_distribution(ρ') ≠ tension_distribution(ρ)
```

### 代码对应

```python
# poc/mvm_simulator.py
class ManifestationOperator:
    def generate_snapshot(self) -> Optional[Snapshot]:
        # Step 1: θ 采样位置
        position = self.path.sample_next_position(self.field)
        
        # Step 2: 查询 ω 兼容的接口
        interfaces = self.field.query_interfaces(position, self.spectrum.level)
        
        # Step 3: O 确认
        if self.observer.observe(selected, self.spectrum, self.path):
            return Snapshot(...)
        return None
```

---

## 7. 快照 (S) 结构

### 定义

```
Axiom S.1: 现实由离散的快照序列组成，而非连续流
```

**形式化**：

$$
S := \langle \vec{x}, t, \sigma, C, \text{meta} \rangle
$$

其中：
- $\vec{x} = (x, y, z)$ — 空间坐标
- $t \in \mathbb{Z}^+$ — 时间序号（离散）
- $\sigma$ — 意识维度签名
- $C$ — 快照内容（结构化数据）
- $\text{meta}$ — 元数据（ω, θ_hash, O_confirmed）

### 快照链

$$
\text{Chain} := (S_1, S_2, ..., S_n) \text{ where } t_{k+1} = t_k + 1
$$

```
Axiom S.4: 时间是快照链的序号差
          Δt = t_j - t_i (而非连续流逝)
```

```
Axiom S.5: 因果是结构耦合而非线性传递
          S_i → S_j 不意味着 i < j
```

### 代码对应

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

## 8. 公理索引

### 元虚空公理 (M.x)

| ID | 公理 | 文档引用 |
|----|------|----------|
| M.0 | Non-Existence ≠ Nothingness | [tension-structure.md](../core/meta-void/tension-structure.md) |
| M.1 | 潜能场具有内在接口图谱结构 | [tension-structure.md](../core/meta-void/tension-structure.md) |
| M.2 | 潜能场张力分布非均匀 | [potentiality-field.md](../core/meta-void/potentiality-field.md) |
| M.3 | 显现前存在"前震"酝酿期 | [potentiality-field.md](../core/meta-void/potentiality-field.md) |

### 意识公理 (C.x)

| ID | 公理 | 文档引用 |
|----|------|----------|
| C.0 | ω 决定感知的层级和分辨率 | [spectrum-omega.md](../core/consciousness/spectrum-omega.md) |
| C.1 | 更高 ω 访问更高密度接口 | [spectrum-omega.md](../core/consciousness/spectrum-omega.md) |
| C.2 | ω 转换需跨越阈值 | [spectrum-omega.md](../core/consciousness/spectrum-omega.md) |
| C.3 | θ 决定访问位置和选择 | [path-theta.md](../core/consciousness/path-theta.md) |
| C.4 | θ 具有历史依赖性 | [path-theta.md](../core/consciousness/path-theta.md) |
| C.5 | θ 受注意力权重调制 | [path-theta.md](../core/consciousness/path-theta.md) |

### 快照公理 (S.x)

| ID | 公理 | 文档引用 |
|----|------|----------|
| S.1 | 现实由离散快照序列组成 | [discrete-generation.md](../engine/snapshot-service/discrete-generation.md) |
| S.2 | O 将潜在态坍缩为确定态 | [discrete-generation.md](../engine/snapshot-service/discrete-generation.md) |
| S.4 | 时间是快照链的序号差 | [snapshot-chains.md](../engine/snapshot-service/snapshot-chains.md) |
| S.5 | 因果是结构耦合 | [snapshot-chains.md](../engine/snapshot-service/snapshot-chains.md) |

### 公式公理 (F.x)

| ID | 公理 | 文档引用 |
|----|------|----------|
| F.1 | ⊗ 算子是非线性的 | [formula-S.md](../engine/mapping-logic/formula-S.md) |
| F.2 | ⊗ 具有扰动效应 | [formula-S.md](../engine/mapping-logic/formula-S.md) |

---

## 9. 开放形式化方向

以下是我们欢迎研究者探索的形式化方向：

| 方向 | 数学框架 | 潜在收益 |
|------|----------|----------|
| 范畴论重构 | Category Theory | 将 M 定义为函子，ρ_S 为范畴 |
| 测度论版本 | Measure Theory | 将 θ 定义为概率测度 |
| 信息论量化 | Information Theory | 用熵量化 ω 的分辨率 |
| 拓扑空间 | Topology | 将 I 赋予拓扑结构 |
| 量子形式 | Quantum Mechanics | 将 O 对应波函数坍缩 |

→ 欢迎通过 [Formalization Issue 模板](../../issues/new?template=formalization.md) 提交您的形式化尝试

---

## Navigation | 导航

| 方向 | 链接 |
|------|------|
| ⬅️ 返回 | [spec/](../) |
| 🔗 系统概览 | [system-overview.md](system-overview.md) |
| 🔗 元虚空 | [tension-structure.md](../core/meta-void/tension-structure.md) |
| 🔗 意识频谱 | [spectrum-omega.md](../core/consciousness/spectrum-omega.md) |
| 🔗 POC 模拟器 | [mvm_simulator.py](../poc/mvm_simulator.py) |

---

<div align="center">

*"形式化不是终点，而是更精确对话的起点。"*

</div>

