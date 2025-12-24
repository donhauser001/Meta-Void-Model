# 🧪 Proof of Concept | 概念验证模拟器

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

```bash
# 进入 poc 目录
cd poc

# 运行模拟器
python mvm_simulator.py

# 运行测试
python -m pytest test_mvm.py -v
```

---

## 📁 File Structure | 文件结构

```
poc/
├── README.md           # 本说明文件
├── mvm_simulator.py    # 核心模拟器
├── test_mvm.py         # 单元测试
└── examples/           # 示例场景
    └── emergence.py    # 涌现现象模拟
```

---

## 🔬 Simulation Components | 模拟组件

| 组件 | 类名 | 描述 |
|------|------|------|
| 潜能场 | `PotentialityField` | 未显现的可能性空间 |
| 意识路径 | `ConsciousnessPath` | θ 参数的概率采样器 |
| 意识频谱 | `SpectrumOmega` | ω 参数的层级控制器 |
| 观察行为 | `Observation` | O 参数的状态确认器 |
| 快照 | `Snapshot` | S 的数据结构 |
| 显现算子 | `ManifestationOperator` | M 的计算逻辑 |

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
- [ ] 添加可视化界面
- [ ] 与神经网络集成

---

## 📖 References | 参考

- [核心公式 →](../engine/mapping-logic/formula-S.md)
- [快照机制 →](../engine/snapshot-service/discrete-generation.md)
- [AI 显现研究 →](../lab/research/ai-manifestation.md)

