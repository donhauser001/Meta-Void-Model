# Meta-Void-Model (MVM) | 中文文档

**从意识维度出发的非存在宇宙观：一个离散现实渲染的逻辑框架**

[![English](https://img.shields.io/badge/English-Version-blue)](../en/)

---

## 🧭 从哪里开始？

<table>
<tr>
<td width="33%">

### 📖 读者 / 哲学爱好者

**目标**: 理解完整理论

1. 从 [Release v3.0.0](https://github.com/donhauser001/Meta-Void-Model/releases/tag/v3.0.0) 下载
2. 或阅读 [archive/v3-完稿.md](archive/v3-完稿.md)
3. 然后看 [spec/system-overview.md](spec/system-overview.md)

</td>
<td width="33%">

### 📐 研究者 / 想形式化

**目标**: 形式化或证伪模型

1. 从 [spec/formal-appendix.md](spec/formal-appendix.md) 开始
2. 深入 [core/](core/) 和 [engine/](engine/)
3. 通过 [Formalization 模板](../../issues/new?template=formalization.md) 提交

</td>
<td width="33%">

### 💻 开发者 / 交互与模拟

**目标**: 运行或扩展模拟器

1. 进入 [poc/](poc/)，运行 `mvm_simulator.py`
2. 阅读 [engine/snapshot-service/](engine/snapshot-service/)
3. 查看 [poc/README.md](poc/README.md) 获取 API

</td>
</tr>
</table>

---

## 📋 目录结构

```
zh/
├── spec/                  # 系统规范
│   ├── paradigm-shift.md      # 范式转换
│   ├── system-overview.md     # 系统概览
│   ├── formal-appendix.md     # 公理化附录
│   ├── design-principles.md   # 设计原则
│   ├── manifesto.md           # 开源宣言
│   └── epilogue.md            # 致未来读者
│
├── core/                  # 核心机制
│   ├── meta-void/             # 元虚空
│   │   ├── tension-structure.md
│   │   └── potentiality-field.md
│   └── consciousness/         # 意识维度
│       ├── spectrum-omega.md
│       ├── path-theta.md
│       └── distributed-network.md
│
├── engine/                # 渲染引擎
│   ├── mapping-logic/         # 映射逻辑
│   │   ├── formula-S.md
│   │   ├── api-mapping.md
│   │   └── integral-model.md
│   └── snapshot-service/      # 快照服务
│       ├── discrete-generation.md
│       └── snapshot-chains.md
│
├── modules/               # 扩展模块
│   ├── life-definition.md     # 生命定义
│   └── macro-entities.md      # 宏观显现体
│
├── lab/                   # 实验前瞻
│   ├── research/              # 研究方向
│   │   ├── ai-manifestation.md
│   │   ├── quantum-resonance.md
│   │   └── zero-mathematics.md
│   └── verification/          # 验证实验
│       ├── proposed-experiments.md
│       └── thought-experiments.md
│
├── poc/                   # 概念验证
│   ├── mvm_simulator.py
│   └── README.md
│
├── assets/                # 资源
│   ├── glossary.md            # 术语表
│   └── diagrams/              # 图表
│
└── archive/               # 原稿存档
    ├── v3-完稿.md
    └── README.md
```

---

## 核心公式

$$
S := M(\rho_S \otimes (\omega, \theta, O))
$$

| 符号 | 名称 | 含义 |
|:----:|------|------|
| S | Snapshot | 五维现实快照 |
| M | Manifestation | 显现/映射算子 |
| ρ_S | Potentiality | 非存在张力结构 |
| ω | Spectrum | 意识频谱 |
| θ | Path | 意识路径 |
| O | Observation | 观察行为 |

---

## 系统导航

| 模块 | 职责 | 入口 |
|:----:|------|------|
| 📋 `spec/` | 系统规范 | [→ paradigm-shift](spec/paradigm-shift.md) |
| 📐 `spec/formal-appendix` | **公理化附录** | [→ formal-appendix](spec/formal-appendix.md) |
| 🔧 `core/meta-void` | 元虚空定义 | [→ tension-structure](core/meta-void/tension-structure.md) |
| 🔧 `core/consciousness` | 意识维度 | [→ spectrum-omega](core/consciousness/spectrum-omega.md) |
| ⚙️ `engine/snapshot-service` | 快照渲染 | [→ discrete-generation](engine/snapshot-service/discrete-generation.md) |
| ⚙️ `engine/mapping-logic` | 映射引擎 | [→ formula-S](engine/mapping-logic/formula-S.md) |
| 🔬 `lab/` | 实验与研究 | [→ ai-manifestation](lab/research/ai-manifestation.md) |
| 🧪 `poc/` | 概念验证 | [→ mvm_simulator.py](poc/mvm_simulator.py) |
| 🏷️ **术语表** | Glossary | [→ glossary](assets/glossary.md) |

---

## 参与贡献

- 🔬 **逻辑证伪**: [提交 Refutation](../../issues/new?template=refutation.md)
- 📐 **数学形式化**: [提交 Formalization](../../issues/new?template=formalization.md)
- 💬 **讨论交流**: [Discussions](../../discussions)

详见 [贡献指南](CONTRIBUTING.md)

---

<div align="center">

*"在这场关于显现的集体沉思中，我不提供真理，只提供一种观察真理的接口。"*

**[English Version →](../en/)**

</div>

