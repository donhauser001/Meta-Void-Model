# Meta-Void-Model (MVM)

**从意识维度出发的非存在宇宙观：一个离散现实渲染的逻辑框架**

<div align="center">

<img src="assets/diagrams/banner-v2.jpg" alt="Meta-Void-Model Banner" width="100%"/>

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
[![Release](https://img.shields.io/github/v/release/donhauser001/Meta-Void-Model?label=Release&color=03624C)](https://github.com/donhauser001/Meta-Void-Model/releases/tag/v3.0.0)

### 🌐 Language | 语言

[![简体中文](https://img.shields.io/badge/简体中文-文档-blue?style=for-the-badge)](zh/)
[![English](https://img.shields.io/badge/English-Docs-blue?style=for-the-badge)](en/)

</div>

---

## TL;DR — 10 秒介绍

| 问题 | 回答 |
|------|------|
| **MVM 是什么** | 一个将现实视为"意识对潜能场的离散渲染"的宇宙观模型 |
| **不是什么** | 不是宗教、不是物理学替代品，而是一套"显现逻辑接口" |
| **核心公式** | `S := M(ρ_S ⊗ (ω, θ, O))` — 快照 = 映射(潜能场 ⊗ 意识参数) |
| **能用来做什么** | 思想实验、世界观设计、交互艺术、AI 模型对照、游戏宇宙构建... |

---

## 📁 项目结构

```
Meta-Void-Model/
├── zh/                    # 📖 中文文档
│   ├── spec/              # 系统规范
│   ├── core/              # 核心机制
│   ├── engine/            # 渲染引擎
│   ├── modules/           # 扩展模块
│   ├── lab/               # 实验前瞻
│   ├── poc/               # 概念验证
│   └── archive/           # 完整原稿
│
├── en/                    # 📖 English Documentation
│   ├── spec/              # System Specification
│   ├── core/              # Core Mechanisms
│   ├── engine/            # Rendering Engine
│   ├── modules/           # Extension Modules
│   ├── lab/               # Experimental Research
│   ├── poc/               # Proof of Concept
│   └── archive/           # Archive
│
├── LICENSE                # 分层授权协议
└── README.md              # 本文件
```

---

## 🚀 快速开始

<table>
<tr>
<td width="50%">

### 📖 中文读者

**[→ 进入中文文档](zh/)**

- [系统概览](zh/spec/system-overview.md)
- [核心公式](zh/engine/mapping-logic/formula-S.md)
- [术语表](zh/assets/glossary.md)
- [完整原稿](zh/archive/v3-完稿.md)

</td>
<td width="50%">

### 📖 English Readers

**[→ Enter English Docs](en/)**

- [System Overview](en/spec/system-overview.md)
- [Core Formula](en/engine/mapping-logic/formula-S.md)
- [Glossary](en/assets/glossary.md)
- [Release Notes](en/RELEASE_NOTES.md)

</td>
</tr>
</table>

---

## 核心公式

$$
S := M(\rho_S \otimes (\omega, \theta, O))
$$

其中：
- **S**: 五维现实快照
- **M**: 显现/映射算子
- **ρ_S**: 非存在张力结构 (潜能场)
- **ω**: 意识频谱 (深度/分辨率)
- **θ**: 意识路径 (选择/历史)
- **O**: 观察行为 (确认/锁定)

---

## 🧪 运行模拟器

```bash
cd zh/poc && python mvm_simulator.py
```

```python
from mvm_simulator import MVMSimulator, MVMConfig, SpectrumLevel, PathStrategy

config = MVMConfig(
    path_strategy=PathStrategy.HISTORY_BIASED,
    initial_omega=SpectrumLevel.OMEGA_MEDIUM,
    snapshot_count=50
)
sim = MVMSimulator(config)
chain = sim.run()
print(chain.to_json())
```

---

## 📜 许可证

本项目采用**分层授权**策略：

| 范围 | 许可证 |
|------|--------|
| 文档 (`.md`) | CC BY-NC-ND 4.0 |
| 代码 (`poc/`) | MIT |
| 模板配置 | CC0 |

详见 [LICENSE](LICENSE)

---

<div align="center">

*"在这场关于显现的集体沉思中，我不提供真理，只提供一种观察真理的接口。"*

**[English Version →](en/)**

</div>
