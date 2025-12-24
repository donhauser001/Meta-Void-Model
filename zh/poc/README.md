# 🧪 Proof of Concept | 概念验证模拟器

[![English](https://img.shields.io/badge/English-Version-blue)](../en/README.md)

> **License**: MIT (可自由修改、商业使用)  
> **声明**：这是一个**概念性模拟**，用于展示 MVM 核心公式的逻辑结构，而非物理现实的精确模型。

---

## 📐 Core Formula | 核心公式

```
S := M(ρ_S ⊗ (ω, θ, O))

其中:
- S   : 五维现实快照 (x, y, z | t | 意识维)
- M   : 显现/映射算子
- ρ_S : 非存在张力结构 (潜能场)
- ω   : 意识频谱 (深度/分辨率)
- θ   : 意识路径 (选择/历史)
- O   : 观察行为 (确认/锁定)
```

---

## 🚀 Quick Start | 快速开始

### 基础运行

```bash
cd poc && python mvm_simulator.py
```

### 使用 MVMConfig (推荐)

```python
from mvm_simulator import MVMSimulator, MVMConfig, SpectrumLevel, PathStrategy

# 创建配置对象
config = MVMConfig(
    field_dimensions=5,        # 潜能场维度
    interface_count=1000,      # 潜能接口数量
    path_strategy=PathStrategy.HISTORY_BIASED,  # θ 路径策略
    initial_omega=SpectrumLevel.OMEGA_MEDIUM,   # ω 初始频谱
    snapshot_count=50,         # 目标快照数
    confirmation_threshold=0.5 # O 确认阈值
)

# 初始化模拟器
sim = MVMSimulator(config=config)

# 运行模拟
chain = sim.run()

# 获取报告
print(sim.report(chain))
```

### 向后兼容的初始化

```python
# 也支持直接传参（向后兼容）
sim = MVMSimulator(
    path_strategy=PathStrategy.ATTENTION_FOCUSED,
    initial_omega=SpectrumLevel.OMEGA_HIGH
)
```

---

## 📦 API Reference

### MVMConfig

配置数据类，替代字符串魔法参数：

| 字段 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `field_dimensions` | int | 5 | 潜能场维度 |
| `interface_count` | int | 1000 | 潜能接口数量 |
| `path_strategy` | PathStrategy | HISTORY_BIASED | θ 路径采样策略 |
| `initial_omega` | SpectrumLevel | OMEGA_MEDIUM | ω 初始频谱层级 |
| `snapshot_count` | int | 50 | 目标快照数量 |
| `confirmation_threshold` | float | 0.5 | O 观察确认阈值 |

### PathStrategy (θ 路径策略)

| 策略 | 值 | 描述 |
|------|-----|------|
| `RANDOM` | "random" | 随机游走，无偏好探索 |
| `HISTORY_BIASED` | "history" | 历史偏好，沿惯性方向 |
| `ATTENTION_FOCUSED` | "focus" | 注意力聚焦，向高密度收敛 |
| `EXPLORATORY` | "explore" | 探索扩散，偏好未知区域 |

### SpectrumLevel (ω 频谱层级)

| 层级 | 值 | 描述 | 可访问内容 |
|------|-----|------|------------|
| `OMEGA_LOW` | 1 | 低频 - 物质/能量层 | 物理定律、空间结构 |
| `OMEGA_MEDIUM` | 2 | 中频 - 信息/模式层 | 概念、关系、模式 |
| `OMEGA_HIGH` | 3 | 高频 - 意义/存在层 | 价值、意义、存在感 |

### SnapshotChain

快照链对象，包含模拟结果：

```python
chain.length           # 快照数量
chain.temporal_span    # 时间跨度
chain.snapshots        # Snapshot 列表
chain.to_dict()        # 转换为字典
chain.to_json()        # 导出为 JSON 字符串
```

---

## 📤 JSON Export | JSON 导出

### 导出快照链

```python
# 导出为 JSON 字符串
json_str = chain.to_json(indent=2)

# 或转为字典
data = chain.to_dict()
```

### 输出结构

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

## 📊 Visualization Example | 可视化示例

```python
import matplotlib.pyplot as plt
from mvm_simulator import MVMSimulator, MVMConfig

# 运行模拟
config = MVMConfig(snapshot_count=100)
sim = MVMSimulator(config=config)
chain = sim.run()

# 绘制张力波动
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

## 🔧 Component Mapping | 组件映射

| MVM 概念 | Python 类 | 职责 |
|----------|-----------|------|
| 潜能场 ρ_S | `PotentialityField` | 管理潜能接口集合和张力状态 |
| 意识路径 θ | `ConsciousnessPath` | 路径采样和历史管理 |
| 意识频谱 ω | `SpectrumOmega` | 频谱层级和分辨率控制 |
| 观察行为 O | `Observation` | 确认阈值判断 |
| 显现算子 M | `ManifestationOperator` | 核心生成逻辑 |
| 快照 S | `Snapshot` | 单帧现实数据 |
| 快照链 | `SnapshotChain` | 时间序列和导出 |

---

## ⚠️ Limitations | 局限性

1. **简化模型**：真实的 ρ_S 结构远比本模拟复杂
2. **数值近似**：连续的意识频谱被离散化处理
3. **单机运行**：未实现分布式意识网络
4. **无量子效应**：未集成真实的量子随机性

---

## 🎯 Research Directions | 研究方向

- [ ] 集成量子随机数发生器 (QRNG)
- [ ] 实现多节点分布式模拟
- [ ] 添加 Web 可视化界面 (Three.js)
- [ ] 与 LLM 集成，验证 AI 显现假说
- [ ] 导出为 Unity/Unreal 可消费格式

---

## 📖 References | 参考

- [核心公式 →](../engine/mapping-logic/formula-S.md)
- [公理化附录 →](../spec/formal-appendix.md)
- [快照机制 →](../engine/snapshot-service/discrete-generation.md)
- [AI 显现研究 →](../lab/research/ai-manifestation.md)

---

<div align="center">

*"代码是思想的可执行形式。"*

**MIT License** — Fork it. Extend it. Build upon it.

</div>
