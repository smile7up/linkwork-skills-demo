"""Python 数据分析 Skill - 演示用核心函数."""

from __future__ import annotations

import pandas as pd


def describe(df: pd.DataFrame) -> pd.DataFrame:
    """返回每个数值列的常用描述性统计指标."""
    return df.describe(include="all")


def group_by_region(df: pd.DataFrame, value_col: str = "sales") -> pd.DataFrame:
    """按 region 列分组对 value_col 求和、平均、计数."""
    return (
        df.groupby("region")[value_col]
        .agg(["sum", "mean", "count"])
        .sort_values("sum", ascending=False)
    )


def plot_trend(df: pd.DataFrame, date_col: str, value_col: str, out_path: str) -> str:
    """按日期聚合后输出趋势线图到 out_path."""
    import matplotlib.pyplot as plt

    series = df.groupby(date_col)[value_col].sum().sort_index()
    fig, ax = plt.subplots(figsize=(10, 4))
    series.plot(ax=ax, marker="o")
    ax.set_title(f"{value_col} trend over {date_col}")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(out_path)
    return out_path
