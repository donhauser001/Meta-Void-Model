# 系统概览：MVM 的宏观逻辑流

> **Module:** `spec/system-overview`

---

## 架构图

```
┌─────────────────────────────────────────────────────────┐
│                    Meta-Void (元虚空)                    │
│              全频结构场 / Potentiality Map               │
└─────────────────────────────────────────────────────────┘
                            │
                            │ ⊗ 非线性张力卷积
                            ▼
┌─────────────────────────────────────────────────────────┐
│              Consciousness Path (ω, θ)                  │
│         ω: Spectrum (频谱)  │  θ: Path (路径)           │
└─────────────────────────────────────────────────────────┘
                            │
                            │ 映射 / Mapping
                            ▼
┌─────────────────────────────────────────────────────────┐
│                 Snapshot (五维快照)                      │
│                  现实的时空量子化单元                     │
└─────────────────────────────────────────────────────────┘
```

---

## 核心公式

$$
Reality(\text{Snapshot}) = f(\text{MetaVoid} \otimes \text{ConsciousnessPath}_{(\omega, \theta)})
$$

---

## 模块依赖

| 模块 | 职责 |
|------|------|
| `core/meta-void` | 定义底层潜能场 |
| `core/consciousness` | 定义意识维度参数 |
| `engine/snapshot-service` | 实现快照渲染逻辑 |
| `engine/mapping-logic` | 实现映射算法 |

---

**相关模块：**
- [`core/meta-void`](../core/meta-void/tension-structure.md)
- [`core/consciousness`](../core/consciousness/spectrum-omega.md)

