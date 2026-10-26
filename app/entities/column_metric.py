# 用于定义字段指标关系的业务实体类
from dataclasses import dataclass

@dataclass
class ColumnMetric:
  column_id: str  # 列编号
  metric_id: str  # 指标编号
