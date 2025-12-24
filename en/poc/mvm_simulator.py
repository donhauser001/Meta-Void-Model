#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Meta-Void-Model (MVM) Proof of Concept Simulator
================================================

核心公式: S := M(ρ_S ⊗ (ω, θ, O))

本模拟器展示 MVM 的逻辑结构，而非物理现实的精确模型。
它演示了意识如何从潜能场中"显现"现实快照的过程。

Author: MVM Research Community
License: MIT
"""

from __future__ import annotations
import random
import math
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional, Callable
from enum import Enum
import hashlib
import json


# =============================================================================
# 枚举类型定义
# =============================================================================

class SpectrumLevel(Enum):
    """
    意识频谱层级 (ω)
    
    Axiom C.0: ω 决定意识能够"感知/处理"的潜能层级和细节分辨率
    """
    OMEGA_LOW = 1      # ωₗ: 低频 - 物质/能量层
    OMEGA_MEDIUM = 2   # ωₘ: 中频 - 信息/模式层  
    OMEGA_HIGH = 3     # ωₕ: 高频 - 意义/存在层


class PathStrategy(Enum):
    """
    意识路径选择策略 (θ 的采样模式)
    
    Axiom C.3: θ 决定"哪里"和"什么" —— 选择性访问潜能接口
    """
    RANDOM = "random"           # 随机游走
    HISTORY_BIASED = "history"  # 历史偏好
    ATTENTION_FOCUSED = "focus" # 注意力聚焦
    EXPLORATORY = "explore"     # 探索性扩散


# =============================================================================
# 核心数据结构
# =============================================================================

@dataclass
class PotentialityInterface:
    """
    潜能接口 (非存在张力结构中的可激活节点)
    
    Axiom M.1: 潜能场并非混沌,而是具有内在的"接口图谱"
    """
    id: str                          # 接口唯一标识
    coordinates: Tuple[float, ...]   # 在潜能场中的"位置"
    activation_threshold: float      # 激活阈值
    structural_density: float        # 结构密度 ρ
    compatible_omega: List[SpectrumLevel]  # 兼容的频谱层级
    metadata: Dict = field(default_factory=dict)
    
    def __hash__(self):
        return hash(self.id)


@dataclass
class Snapshot:
    """
    五维现实快照 S(x, y, z | t | 意识维)
    
    Axiom S.1: 现实由离散的快照序列组成,而非连续流
    """
    spatial: Tuple[float, float, float]  # (x, y, z) 空间坐标
    temporal_index: int                   # t 时间序号
    consciousness_signature: str          # 意识维度签名
    content: Dict                         # 快照内容
    omega_level: SpectrumLevel           # 生成时的频谱层级
    theta_path_hash: str                 # θ 路径哈希
    observation_confirmed: bool          # O 是否确认
    
    @property
    def snapshot_id(self) -> str:
        """生成快照的唯一标识"""
        data = f"{self.spatial}|{self.temporal_index}|{self.consciousness_signature}"
        return hashlib.sha256(data.encode()).hexdigest()[:16]


@dataclass 
class SnapshotChain:
    """
    快照链 (时间序列)
    
    Axiom S.4: 时间是快照链的序号差,因果是结构耦合
    """
    snapshots: List[Snapshot] = field(default_factory=list)
    chain_id: str = ""
    
    def __post_init__(self):
        if not self.chain_id:
            self.chain_id = hashlib.sha256(str(random.random()).encode()).hexdigest()[:8]
    
    def append(self, snapshot: Snapshot):
        self.snapshots.append(snapshot)
    
    @property
    def length(self) -> int:
        return len(self.snapshots)
    
    @property
    def temporal_span(self) -> int:
        if len(self.snapshots) < 2:
            return 0
        return self.snapshots[-1].temporal_index - self.snapshots[0].temporal_index
    
    def to_dict(self) -> Dict:
        """转换为字典格式（供前端可视化）"""
        return {
            "chain_id": self.chain_id,
            "length": self.length,
            "temporal_span": self.temporal_span,
            "snapshots": [
                {
                    "index": i,
                    "snapshot_id": s.snapshot_id,
                    "spatial": {"x": s.spatial[0], "y": s.spatial[1], "z": s.spatial[2]},
                    "temporal_index": s.temporal_index,
                    "omega": s.omega_level.name,
                    "theta_hash": s.theta_path_hash,
                    "confirmed": s.observation_confirmed,
                    "content": s.content
                }
                for i, s in enumerate(self.snapshots)
            ]
        }
    
    def to_json(self, indent: int = 2) -> str:
        """导出为 JSON 字符串"""
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)


@dataclass
class MVMConfig:
    """
    MVM 模拟器配置
    
    用于替代字符串魔法参数，提供类型安全的配置
    """
    # 潜能场配置
    field_dimensions: int = 5
    interface_count: int = 1000
    
    # 意识参数配置
    path_strategy: PathStrategy = PathStrategy.HISTORY_BIASED
    initial_omega: SpectrumLevel = SpectrumLevel.OMEGA_MEDIUM
    
    # 模拟配置
    snapshot_count: int = 50
    max_attempts_multiplier: int = 3
    
    # 观察配置
    confirmation_threshold: float = 0.5
    
    def to_dict(self) -> Dict:
        return {
            "field_dimensions": self.field_dimensions,
            "interface_count": self.interface_count,
            "path_strategy": self.path_strategy.value,
            "initial_omega": self.initial_omega.name,
            "snapshot_count": self.snapshot_count,
            "confirmation_threshold": self.confirmation_threshold
        }


# =============================================================================
# 核心组件
# =============================================================================

class PotentialityField:
    """
    非存在张力结构 / 潜能场 (ρ_S)
    
    Axiom M.0: Non-Existence ≠ Nothingness
    这里的"非存在"是结构化的潜能,而非空无
    """
    
    def __init__(self, dimensions: int = 5, interface_count: int = 1000):
        self.dimensions = dimensions
        self.interfaces: Dict[str, PotentialityInterface] = {}
        self._initialize_interfaces(interface_count)
        self.tension_state: float = 1.0  # 张力状态
    
    def _initialize_interfaces(self, count: int):
        """初始化潜能接口图谱"""
        for i in range(count):
            coords = tuple(random.gauss(0, 1) for _ in range(self.dimensions))
            interface = PotentialityInterface(
                id=f"PI_{i:04d}",
                coordinates=coords,
                activation_threshold=random.uniform(0.1, 0.9),
                structural_density=random.uniform(0.5, 2.0),
                compatible_omega=[
                    level for level in SpectrumLevel 
                    if random.random() > 0.3
                ] or [SpectrumLevel.OMEGA_LOW]
            )
            self.interfaces[interface.id] = interface
    
    def query_interfaces(
        self, 
        center: Tuple[float, ...], 
        radius: float,
        omega: SpectrumLevel
    ) -> List[PotentialityInterface]:
        """
        查询给定位置周围的兼容接口
        模拟 θ 路径的"选择性访问"
        """
        compatible = []
        for interface in self.interfaces.values():
            # 检查频谱兼容性
            if omega not in interface.compatible_omega:
                continue
            # 计算距离
            dist = math.sqrt(sum(
                (a - b) ** 2 
                for a, b in zip(center, interface.coordinates)
            ))
            if dist <= radius:
                compatible.append(interface)
        return compatible
    
    def perturb(self, intensity: float):
        """
        扰动张力场 (模拟"前震机制")
        
        Axiom M.4: 显现前存在"酝酿期"
        """
        self.tension_state *= (1 + intensity * random.gauss(0, 0.1))
        self.tension_state = max(0.1, min(10.0, self.tension_state))


class ConsciousnessPath:
    """
    意识路径 (θ)
    
    Axiom C.3-C.5: θ 是带有历史依赖的概率分布
    """
    
    def __init__(
        self, 
        strategy: PathStrategy = PathStrategy.HISTORY_BIASED,
        initial_position: Optional[Tuple[float, ...]] = None,
        dimensions: int = 5
    ):
        self.strategy = strategy
        self.dimensions = dimensions
        self.position = initial_position or tuple(0.0 for _ in range(dimensions))
        self.history: List[Tuple[float, ...]] = [self.position]
        self.attention_weights: Dict[str, float] = {}
    
    def sample_next_position(self, field: PotentialityField) -> Tuple[float, ...]:
        """
        采样下一个位置 (θ 的动态演化)
        """
        if self.strategy == PathStrategy.RANDOM:
            delta = tuple(random.gauss(0, 0.5) for _ in range(self.dimensions))
        
        elif self.strategy == PathStrategy.HISTORY_BIASED:
            # 倾向于沿历史方向继续
            if len(self.history) >= 2:
                momentum = tuple(
                    self.history[-1][i] - self.history[-2][i]
                    for i in range(self.dimensions)
                )
                delta = tuple(
                    m * 0.7 + random.gauss(0, 0.3)
                    for m in momentum
                )
            else:
                delta = tuple(random.gauss(0, 0.5) for _ in range(self.dimensions))
        
        elif self.strategy == PathStrategy.ATTENTION_FOCUSED:
            # 向高密度区域聚焦
            nearby = field.query_interfaces(self.position, 2.0, SpectrumLevel.OMEGA_MEDIUM)
            if nearby:
                target = max(nearby, key=lambda x: x.structural_density)
                delta = tuple(
                    (t - p) * 0.3 + random.gauss(0, 0.1)
                    for t, p in zip(target.coordinates, self.position)
                )
            else:
                delta = tuple(random.gauss(0, 0.5) for _ in range(self.dimensions))
        
        else:  # EXPLORATORY
            delta = tuple(random.gauss(0, 1.0) for _ in range(self.dimensions))
        
        new_position = tuple(p + d for p, d in zip(self.position, delta))
        self.position = new_position
        self.history.append(new_position)
        return new_position
    
    @property
    def path_hash(self) -> str:
        """生成路径的哈希签名"""
        data = str(self.history[-10:])  # 最近10步
        return hashlib.md5(data.encode()).hexdigest()[:8]


class SpectrumOmega:
    """
    意识频谱 (ω)
    
    Axiom C.0-C.2: ω 决定显现的"质地"和"分辨率"
    """
    
    def __init__(self, initial_level: SpectrumLevel = SpectrumLevel.OMEGA_MEDIUM):
        self.level = initial_level
        self.intensity: float = 0.5  # 0-1 范围内的强度
    
    def shift(self, delta: int):
        """频谱层级转换"""
        current_value = self.level.value
        new_value = max(1, min(3, current_value + delta))
        self.level = SpectrumLevel(new_value)
    
    def modulate(self, factor: float):
        """调制强度"""
        self.intensity = max(0.0, min(1.0, self.intensity * factor))
    
    @property
    def resolution(self) -> float:
        """当前分辨率 (0-1)"""
        base = self.level.value / 3.0
        return base * self.intensity


class Observation:
    """
    观察行为 (O)
    
    Axiom S.2: O 将潜在态"坍缩"为确定的快照
    """
    
    def __init__(self, confirmation_threshold: float = 0.5):
        self.confirmation_threshold = confirmation_threshold
        self.observation_count: int = 0
    
    def observe(
        self, 
        interface: PotentialityInterface,
        omega: SpectrumOmega,
        theta: ConsciousnessPath
    ) -> bool:
        """
        执行观察,判断是否确认显现
        
        Returns:
            bool: 是否确认生成快照
        """
        self.observation_count += 1
        
        # 计算确认概率
        # 基于: 接口密度、频谱分辨率、路径历史长度
        density_factor = interface.structural_density / 2.0
        resolution_factor = omega.resolution
        history_factor = min(1.0, len(theta.history) / 100.0)
        
        confirmation_probability = (
            density_factor * 0.4 +
            resolution_factor * 0.4 +
            history_factor * 0.2
        )
        
        return random.random() < confirmation_probability


# =============================================================================
# 显现算子 (核心引擎)
# =============================================================================

class ManifestationOperator:
    """
    显现/映射算子 M
    
    实现核心公式: S := M(ρ_S ⊗ (ω, θ, O))
    """
    
    def __init__(
        self,
        potentiality_field: PotentialityField,
        consciousness_path: ConsciousnessPath,
        spectrum: SpectrumOmega,
        observer: Observation
    ):
        self.field = potentiality_field
        self.path = consciousness_path
        self.spectrum = spectrum
        self.observer = observer
        self.current_temporal_index: int = 0
    
    def generate_snapshot(self) -> Optional[Snapshot]:
        """
        生成单个快照
        
        执行: S := M(ρ_S ⊗ (ω, θ, O))
        """
        # Step 1: θ 采样新位置
        position = self.path.sample_next_position(self.field)
        
        # Step 2: 查询兼容的潜能接口
        interfaces = self.field.query_interfaces(
            position, 
            radius=1.0 + self.spectrum.resolution,
            omega=self.spectrum.level
        )
        
        if not interfaces:
            return None  # 无可激活接口
        
        # Step 3: 选择最佳接口 (基于密度和兼容性)
        selected = max(interfaces, key=lambda x: x.structural_density)
        
        # Step 4: 执行观察 (O)
        confirmed = self.observer.observe(selected, self.spectrum, self.path)
        
        if not confirmed:
            # 前震阶段,扰动张力场但不生成快照
            self.field.perturb(0.1)
            return None
        
        # Step 5: 生成快照
        self.current_temporal_index += 1
        
        snapshot = Snapshot(
            spatial=(position[0], position[1], position[2]),
            temporal_index=self.current_temporal_index,
            consciousness_signature=f"C_{self.path.path_hash}_{self.spectrum.level.name}",
            content={
                "interface_id": selected.id,
                "density": selected.structural_density,
                "coordinates": selected.coordinates,
                "field_tension": self.field.tension_state
            },
            omega_level=self.spectrum.level,
            theta_path_hash=self.path.path_hash,
            observation_confirmed=True
        )
        
        return snapshot
    
    def generate_chain(self, max_snapshots: int = 100) -> SnapshotChain:
        """
        生成快照链
        """
        chain = SnapshotChain()
        attempts = 0
        max_attempts = max_snapshots * 3
        
        while chain.length < max_snapshots and attempts < max_attempts:
            attempts += 1
            snapshot = self.generate_snapshot()
            if snapshot:
                chain.append(snapshot)
        
        return chain


# =============================================================================
# 模拟运行器
# =============================================================================

class MVMSimulator:
    """
    MVM 模拟器主类
    
    支持两种初始化方式:
    1. MVMSimulator(config=MVMConfig(...))  # 推荐
    2. MVMSimulator(path_strategy=..., initial_omega=...)  # 向后兼容
    """
    
    def __init__(
        self,
        config: Optional[MVMConfig] = None,
        # 向后兼容的参数
        field_dimensions: int = 5,
        interface_count: int = 1000,
        path_strategy: PathStrategy = PathStrategy.HISTORY_BIASED,
        initial_omega: SpectrumLevel = SpectrumLevel.OMEGA_MEDIUM
    ):
        # 如果提供了 config，使用 config；否则使用单独参数
        if config is not None:
            self.config = config
        else:
            self.config = MVMConfig(
                field_dimensions=field_dimensions,
                interface_count=interface_count,
                path_strategy=path_strategy,
                initial_omega=initial_omega
            )
        
        self.field = PotentialityField(
            self.config.field_dimensions, 
            self.config.interface_count
        )
        self.path = ConsciousnessPath(
            self.config.path_strategy, 
            dimensions=self.config.field_dimensions
        )
        self.spectrum = SpectrumOmega(self.config.initial_omega)
        self.observer = Observation(self.config.confirmation_threshold)
        self.operator = ManifestationOperator(
            self.field, self.path, self.spectrum, self.observer
        )
    
    def run(self, snapshot_count: Optional[int] = None) -> SnapshotChain:
        """运行模拟"""
        count = snapshot_count or self.config.snapshot_count
        return self.operator.generate_chain(count)
    
    def report(self, chain: SnapshotChain) -> Dict:
        """生成报告"""
        if not chain.snapshots:
            return {"error": "No snapshots generated"}
        
        omega_distribution: Dict[str, int] = {}
        for s in chain.snapshots:
            level = s.omega_level.name
            omega_distribution[level] = omega_distribution.get(level, 0) + 1
        
        return {
            "chain_id": chain.chain_id,
            "config": self.config.to_dict(),
            "total_snapshots": chain.length,
            "temporal_span": chain.temporal_span,
            "omega_distribution": omega_distribution,
            "path_length": len(self.path.history),
            "observation_attempts": self.observer.observation_count,
            "success_rate": chain.length / max(1, self.observer.observation_count),
            "field_final_tension": self.field.tension_state
        }
    
    def report_json(self, chain: SnapshotChain, indent: int = 2) -> str:
        """生成 JSON 格式报告"""
        return json.dumps(self.report(chain), indent=indent, ensure_ascii=False)


# =============================================================================
# 主程序
# =============================================================================

def main():
    """演示运行"""
    print("=" * 60)
    print("  Meta-Void-Model (MVM) Proof of Concept Simulator")
    print("  核心公式: S := M(ρ_S ⊗ (ω, θ, O))")
    print("=" * 60)
    print()
    
    # 方式1: 使用 MVMConfig (推荐)
    config = MVMConfig(
        field_dimensions=5,
        interface_count=1000,
        path_strategy=PathStrategy.HISTORY_BIASED,
        initial_omega=SpectrumLevel.OMEGA_MEDIUM,
        snapshot_count=50
    )
    simulator = MVMSimulator(config=config)
    
    print("[1] 初始化潜能场 (ρ_S)...")
    print(f"    - 维度: {simulator.field.dimensions}")
    print(f"    - 潜能接口数: {len(simulator.field.interfaces)}")
    print()
    
    print("[2] 配置意识参数...")
    print(f"    - 路径策略 (θ): {simulator.path.strategy.value}")
    print(f"    - 频谱层级 (ω): {simulator.spectrum.level.name}")
    print()
    
    print("[3] 运行显现过程...")
    chain = simulator.run()
    print(f"    - 生成快照数: {chain.length}")
    print()
    
    print("[4] 模拟报告")
    print("-" * 40)
    report = simulator.report(chain)
    for key, value in report.items():
        if key == "config":
            print(f"    {key}: <MVMConfig>")
        elif isinstance(value, float):
            print(f"    {key}: {value:.4f}")
        else:
            print(f"    {key}: {value}")
    print()
    
    print("[5] 快照链样本 (前5个)")
    print("-" * 40)
    for i, snapshot in enumerate(chain.snapshots[:5]):
        print(f"    [{i+1}] ID: {snapshot.snapshot_id}")
        print(f"        时间序号: t={snapshot.temporal_index}")
        print(f"        空间坐标: {tuple(round(x, 2) for x in snapshot.spatial)}")
        print(f"        频谱层级: {snapshot.omega_level.name}")
        print()
    
    # 演示 JSON 导出
    print("[6] JSON 导出示例 (首个快照)")
    print("-" * 40)
    if chain.snapshots:
        sample_json = json.dumps(chain.to_dict()["snapshots"][0], indent=2, ensure_ascii=False)
        print(sample_json)
    print()
    
    print("=" * 60)
    print("  模拟完成 | Simulation Complete")
    print("  提示: 使用 chain.to_json() 导出完整快照链")
    print("=" * 60)


if __name__ == "__main__":
    main()

