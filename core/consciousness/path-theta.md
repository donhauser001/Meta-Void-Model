# 维度参数 θ (Path) 路径模型

> **Module:** `core/consciousness/path-theta`

---

## 公理定义 (Axioms)

```
┌─────────────────────────────────────────────────────────────────────────┐
│  AXIOM 3.0  Path Definition                                            │
│  ═══════════════════════════════════════════════════════════════════   │
│  意识路径 θ 决定接入元虚空张力结构的特定位置。                              │
│  每个意识节点都是元虚空的一个唯一接入点。                                   │
│                                                                         │
│  θ: Consciousness → MetaVoid.Region                                    │
│  θ₁ ≠ θ₂ ⟹ Region(θ₁) ≠ Region(θ₂)                                    │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│  AXIOM 3.1  Path Locality                                              │
│  ═══════════════════════════════════════════════════════════════════   │
│  每条 θ 路径只能接入元虚空的局部区域，而非全域。                            │
│  这解释了为何不同意识体验"不同的现实切片"。                                 │
│                                                                         │
│  ∀θ: |Region(θ)| << |MetaVoid|                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│  AXIOM 3.2  Path Mutability                                            │
│  ═══════════════════════════════════════════════════════════════════   │
│  θ 路径可以随时间演化，但演化受到连续性约束。                               │
│  路径不能瞬间跳跃到完全不相邻的区域（除非通过特殊机制）。                    │
│                                                                         │
│  dθ/dt is continuous (一般情况)                                         │
│  Δθ_jump requires special mechanism (跨链跃迁)                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 符号定义

| 符号 | 名称 | 类型 | 几何意义 |
|:----:|------|------|----------|
| $\theta$ | Path（路径） | 流形上的坐标 | [元虚空](../../assets/glossary.md#meta-void元虚空)中的接入位置 |

---

## 功能

决定意识接入元虚空张力结构的**特定路径**。

你是显现结构的接入节点。

参见 [术语表：意识维度](../../assets/glossary.md#consciousness-dimension意识维度)

---

## 路径拓扑模型

```
                    ┌─────────────────────────────────┐
                    │         META-VOID               │
                    │                                 │
    θ₁ ─────────────┼──►  ●  Region₁                 │
                    │                                 │
    θ₂ ─────────────┼──────────►  ●  Region₂         │
                    │                                 │
    θ₃ ─────────────┼────►  ●  Region₃               │
                    │                                 │
                    │      (不同路径接入不同区域)       │
                    └─────────────────────────────────┘
```

---

## API 类比

| MVM 概念 | API 类比 | 说明 |
|----------|----------|------|
| θ 路径 | API Endpoint | 指定资源位置 |
| 路径权限 | Authentication | 决定可访问范围 |
| 路径演化 | Session State | 随交互而变化 |
| 跨链跃迁 | Redirect | 非连续跳转 |

---

## 实现注释

```python
# core/consciousness/path-theta.py (概念伪代码)

class Path:
    """
    意识路径参数
    
    Axiom 3.0: 唯一接入点映射
    Axiom 3.1: 局部性约束
    Axiom 3.2: 连续性演化（一般情况）
    """
    
    def __init__(self, coordinates: Manifold.Point):
        self.coordinates = coordinates
        self.history = [coordinates]  # 路径演化历史
    
    def query_region(self, meta_void: MetaVoid) -> Region:
        """
        Axiom 3.0: 路径 → 区域映射
        """
        return meta_void.get_region(self.coordinates)
    
    def evolve(self, delta: Vector, continuous: bool = True):
        """
        Axiom 3.2: 路径演化
        """
        if continuous:
            # 连续演化：小步移动
            self.coordinates += delta
        else:
            # 跨链跃迁：需要特殊机制
            self._validate_jump(delta)
            self.coordinates = delta
        
        self.history.append(self.coordinates)
    
    def _validate_jump(self, target: Vector):
        """验证跨链跃迁的合法性"""
        # 详见 engine/snapshot-service/snapshot-chains.md
        pass
```

---

**相关模块：**
- [`core/consciousness/spectrum-omega`](spectrum-omega.md) — ω 频谱（正交参数）
- [`core/consciousness/distributed-network`](distributed-network.md) — 多路径网络
- [`engine/mapping-logic/api-mapping`](../../engine/mapping-logic/api-mapping.md) — API 类比详解
