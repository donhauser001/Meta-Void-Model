# Meta-Void-Model (MVM) | 中文文档

[![English](https://img.shields.io/badge/English-Version-blue)](../en/)

---

## 💡 一句话理解 MVM

> **你所经历的世界，从未是你在"观察"，而是你在"生成"。**

MVM（宇宙元模型）是一个将现实视为"意识对潜能场的离散渲染"的理论框架——一场从"构成论"到"显现论"的本体论范式转换。

---

## 🎯 这本书在讲什么？

我们习惯于相信：世界"就在那里"，由粒子堆砌而成，意识只是大脑的副产品。

**但如果这一切都是颠倒的呢？**

MVM 提出：

| 传统观念 | MVM 观点 |
|---------|---------|
| 粒子是宇宙的"砖块" | 粒子是潜能被激活后的投影"像素" |
| 现实是预先存在的 | 现实是被意识一帧帧"渲染"出来的 |
| 意识是大脑产生的 | 意识是宇宙的结构性维度 |
| 时间是连续流动的 | 时间是快照序列的位移感 |
| "你"是被动的观察者 | "你"是宇宙的显现接口 |

---

## ⚡ 核心公式

$$
S := M(\rho_S \otimes (\omega, \theta, O))
$$

**翻译成人话：**

```
你体验到的现实 = 显现算子( 潜能场 ⊗ (你的意识深度, 你的注意方向, 你的观察确认) )
```

| 符号 | 名称 | 直觉理解 |
|:----:|------|----------|
| S | 快照 | 你正在经历的这一刻——一帧"现实" |
| M | 显现算子 | 把可能性"渲染"成现实的过程 |
| ρ_S | 潜能场 | 尚未被激活的全部可能性 |
| ω | 频谱 | 你"看到多深"——意识的分辨率 |
| θ | 路径 | 你"看向哪里"——意识的选择 |
| O | 观察 | 你"确认了"——锁定为现实 |

---

## 🧭 从哪里开始？

<table>
<tr>
<td width="33%">

### 📖 我是哲学爱好者

**目标**: 理解完整理论

1. 先读 [系统概览](spec/system-overview.md)
2. 再看 [范式转换](spec/paradigm-shift.md)
3. 完整原著 → [v3-完稿.md](archive/v3-完稿.md)

</td>
<td width="33%">

### 📐 我是研究者

**目标**: 形式化或证伪模型

1. 从 [公理化附录](spec/formal-appendix.md) 开始
2. 深入 [核心机制](core/) 和 [引擎](engine/)
3. 通过 [Formalization 模板](https://github.com/donhauser001/Meta-Void-Model/issues/new?template=formalization.md) 提交

</td>
<td width="33%">

### 💻 我是开发者

**目标**: 运行或扩展模拟器

1. 进入 [poc/](poc/)，运行 `mvm_simulator.py`
2. 阅读 [快照服务](engine/snapshot-service/)
3. 查看 [poc/README.md](poc/README.md) 获取 API

</td>
</tr>
</table>

---

## 🎬 直觉类比

### 电影的帧结构

想象你正在看一部电影。画面流畅连贯，你完全忘记了它其实是一帧一帧拼接的。

**如果现实也是这样呢？**

不是早已拍好的胶片，而是——在你注视的那一刻，才被投射到屏幕上的动态图样。

### 游戏的地图加载

现代游戏不会预先渲染整个世界，而是在玩家靠近时才加载周围区域。MVM 认为宇宙也可能如此——"现实"在你的意识"接入"时才被渲染。

### API 调用

程序员调用 API 时，不需要知道服务器内部如何实现——发送请求，接收响应。MVM 将现实生成理解为类似过程：你的意识路径向潜能接口发送"调用"，返回的"响应"就是你体验到的现实。

---

## 📚 模块导航

| 模块 | 职责 | 入口 |
|:----:|------|------|
| 📋 **spec/** | 系统规范 | [范式转换](spec/paradigm-shift.md) • [公理化附录](spec/formal-appendix.md) |
| 🔧 **core/meta-void/** | 元虚空定义 | [张力结构](core/meta-void/tension-structure.md) • [潜能场](core/meta-void/potentiality-field.md) |
| 🔧 **core/consciousness/** | 意识维度 | [频谱 ω](core/consciousness/spectrum-omega.md) • [路径 θ](core/consciousness/path-theta.md) |
| ⚙️ **engine/** | 渲染引擎 | [离散生成](engine/snapshot-service/discrete-generation.md) • [核心公式](engine/mapping-logic/formula-S.md) |
| 📦 **modules/** | 扩展模块 | [生命定义](modules/life-definition.md) • [宏观显现体](modules/macro-entities.md) |
| 🔬 **lab/** | 实验前瞻 | [AI 显现](lab/research/ai-manifestation.md) • [量子共振](lab/research/quantum-resonance.md) |
| 🧪 **poc/** | 概念验证 | [模拟器](poc/mvm_simulator.py) |
| 🏷️ **assets/** | 资源 | [术语表](assets/glossary.md) |

---

## 📊 模型架构

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        MVM 快照生成流程                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ┌─────────────┐                                                       │
│   │ 非存在张力   │  ← 潜能接口图谱 (充满可能性的"前显现"状态)              │
│   │ 结构 (ρ_S)  │                                                       │
│   └──────┬──────┘                                                       │
│          │                                                              │
│          ▼                                                              │
│   ┌─────────────┐                                                       │
│   │ 意识介入     │  ← ω 频谱 (看到多深) + θ 路径 (看向哪里)               │
│   │ (ω, θ)      │                                                       │
│   └──────┬──────┘                                                       │
│          │                                                              │
│          ▼                                                              │
│   ┌─────────────┐                                                       │
│   │ 显现张力     │  ← 前震状态 (可能性开始收窄)                           │
│   │ 激活        │                                                       │
│   └──────┬──────┘                                                       │
│          │                                                              │
│          ▼                                                              │
│   ┌─────────────┐                                                       │
│   │ 观察确认     │  ← O 锁定 → 快照 S 生成                                │
│   │ (O → S)     │                                                       │
│   └──────┬──────┘                                                       │
│          │                                                              │
│          ▼                                                              │
│   ┌─────────────┐                                                       │
│   │ 体验呈现     │  ← 你感知到的"现实"                                    │
│   │ (你的当下)   │                                                       │
│   └──────┬──────┘                                                       │
│          │                                                              │
│          └──────────▶ 下一帧 (循环往复)                                  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## ⚠️ 重要声明

MVM 是一部严肃的理论探索著作，旨在激发理性思考与开放讨论。

**本书不是**：
- ❌ 宗教或神秘主义指南
- ❌ 对科学的否定
- ❌ 伪科学宣传
- ❌ 终极答案系统

**本书是**：
- ✅ 一场跨学科的思想实验
- ✅ 一个开放的发问结构
- ✅ 一套可供讨论的概念工具

> 作者明确反对任何将本书观点断章取义、用于伪科学宣传或非理性主张的行为。

---

## 🤝 参与贡献

MVM 是一个开放的**逻辑压力测试场**：

- 🔴 **逻辑证伪**: [提交 Refutation](https://github.com/donhauser001/Meta-Void-Model/issues/new?template=refutation.md)
- 🔵 **数学形式化**: [提交 Formalization](https://github.com/donhauser001/Meta-Void-Model/issues/new?template=formalization.md)
- 🟢 **讨论交流**: [Discussions](https://github.com/donhauser001/Meta-Void-Model/discussions)

详见 [贡献指南](CONTRIBUTING.md)

---

<div align="center">

*"在这场关于显现的集体沉思中，我不提供真理，只提供一种观察真理的接口。"*

### 你并非仅仅生活在这个宇宙之中，在某种意义上，宇宙正是通过你，才得以显现为它自身。

**[开始阅读 →](spec/system-overview.md)**

**[English Version →](../en/)**

</div>
