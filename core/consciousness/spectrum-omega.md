# 维度参数 ω (Spectrum) 规范

> **Module:** `core/consciousness/spectrum-omega`

---

## 公理定义 (Axioms)

```
┌─────────────────────────────────────────────────────────────────────────┐
│  AXIOM 2.0  Spectrum Definition                                        │
│  ═══════════════════════════════════════════════════════════════════   │
│  意识频谱 ω 决定显现的质感与解析度。                                       │
│  ω 值越高，渲染的精细度越高，但能量消耗也越大。                             │
│                                                                         │
│  Resolution(Snapshot) ∝ ω                                              │
│  EnergyConsumption ∝ ω²                                                │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│  AXIOM 2.1  Spectrum Continuity                                        │
│  ═══════════════════════════════════════════════════════════════════   │
│  ω 是一个连续谱，从低频感官到高频顿悟形成无断裂的梯度。                     │
│                                                                         │
│  ω ∈ [ω_min, ω_max]                                                    │
│  ∀ω₁, ω₂: ∃ω₃ such that ω₁ < ω₃ < ω₂                                  │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│  AXIOM 2.2  Spectrum Independence                                      │
│  ═══════════════════════════════════════════════════════════════════   │
│  ω 与 θ 相互独立：路径选择与频谱设定是两个正交的维度参数。                  │
│                                                                         │
│  ∂ω/∂θ = 0                                                             │
│  ∂θ/∂ω = 0                                                             │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 符号定义

| 符号 | 名称 | 类型 | 定义域 |
|:----:|------|------|--------|
| $\omega$ | Spectrum（频谱） | 标量 | $[\omega_{min}, \omega_{max}]$ |

---

## 功能

决定显现的**质感**与**解析度**。

参见 [术语表：意识维度](../../assets/glossary.md#consciousness-dimension意识维度)

---

## 频谱层级模型

```
    ω_max ─┬─────────────────────────────────────────┐
           │                                         │
           │     ▲  顿悟 / 直觉洞见                   │  高频
           │     │  (Intuitive Insight)              │
           │     │                                   │
           │     │  语言 / 符号系统                   │  中频
           │     │  (Symbolic Processing)            │
           │     │                                   │
           │     │  基础感官                          │  低频
           │     │  (Sensory Perception)             │
           │                                         │
    ω_min ─┴─────────────────────────────────────────┘
```

| ω 层级 | 显现类型 | 特征 |
|:------:|----------|------|
| 低频 | 基础感官（触觉、视觉） | 高稳定性，低信息密度 |
| 中频 | 语言与符号系统 | 中等稳定性，可编码传输 |
| 高频 | 顿悟与直觉洞见 | 低稳定性，高信息密度 |

---

## 实现注释

```python
# core/consciousness/spectrum-omega.py (概念伪代码)

class Spectrum:
    """
    意识频谱参数
    
    Axiom 2.0: 决定显现解析度
    Axiom 2.1: 连续谱，无断裂
    Axiom 2.2: 与 θ 正交独立
    """
    
    OMEGA_MIN = 0.0    # 感官下限
    OMEGA_MAX = 1.0    # 顿悟上限
    
    def __init__(self, value: float):
        assert self.OMEGA_MIN <= value <= self.OMEGA_MAX
        self.value = value
    
    @property
    def resolution(self) -> float:
        """渲染解析度"""
        return self.value
    
    @property
    def energy_cost(self) -> float:
        """能量消耗 ∝ ω²"""
        return self.value ** 2
    
    def get_layer(self) -> str:
        """获取频谱层级"""
        if self.value < 0.3:
            return "sensory"      # 感官
        elif self.value < 0.7:
            return "symbolic"     # 符号
        else:
            return "intuitive"    # 顿悟
```

---

**相关模块：**
- [`core/consciousness/path-theta`](path-theta.md) — θ 路径（正交参数）
- [`core/consciousness/distributed-network`](distributed-network.md) — 分布式意识
- [`engine/mapping-logic/formula-S`](../../engine/mapping-logic/formula-S.md) — 生成公式
