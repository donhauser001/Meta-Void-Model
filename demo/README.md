# 🎨 Demo | 可视化演示

> 本目录包含 MVM 的交互式可视化演示。

---

## 快照链可视化器

**文件**: `snapshot-visualizer.html`

### 打开方式

```bash
# 方法1: 直接在浏览器打开
open demo/snapshot-visualizer.html

# 方法2: 使用本地服务器
cd demo && python -m http.server 8080
# 然后访问 http://localhost:8080/snapshot-visualizer.html
```

### 功能

- 调整 θ 路径策略（随机/历史偏好/注意力聚焦/探索）
- 调整 ω 频谱层级（低频/中频/高频）
- 调整快照数量和张力扰动强度
- 实时可视化快照链的生成
- 点击节点查看详细 JSON 数据

### 技术栈

- D3.js v7 (可视化)
- 原生 JavaScript (MVM 简化模拟器)
- 纯 CSS (无框架依赖)

---

## 许可证

MIT License

