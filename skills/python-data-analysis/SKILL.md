# Python 数据分析 Skill

## 描述

提供 Python 数据清洗、统计分析、可视化报表能力。

## 适用场景

- 销售数据 / 用户行为数据 / 日志数据的清洗与统计
- 透视、分组、时序分析
- 输出 matplotlib / plotly 图表与 Markdown 报表

## 调用方式

后端将该 Skill 挂载到 AI 员工 Pod 后，员工可在 Prompt 中引用，调用 `analyze.py` 中的函数。

```python
from analyze import describe, plot_trend, group_by_region
```

## 依赖

- pandas >= 2.0
- matplotlib >= 3.8
- numpy >= 1.26
